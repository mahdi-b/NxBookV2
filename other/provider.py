from pkg_resources import resource_filename, resource_string
from functools import partial
from pathlib import Path, PurePath
from IPython import embed


import yaml
from jinja2 import Template


VuePath = resource_filename("vue", "")
IndexTemplate = resource_string("vuecli", "index.html")
StaticContents = {
    "/loading.gif": resource_string("vuecli", "loading.gif"),
    "/vuepy.js": b"\n".join(
        [
            resource_string("brython", "data/brython.js"),
            resource_string("brython", "data/brython_stdlib.js"),
        ]
    ),
    "/vue.js": resource_string("vuecli", "js/vue.js"),
    "/vuex.js": resource_string("vuecli", "js/vuex.js"),
    "/vue-router.js": resource_string("vuecli", "js/vue-router.js"),
}


class Provider:
    Arguments = {}

    def __init__(self, path=None):
        self.path = Path(path if path else ".")

    @staticmethod
    def _normalize_config(config):
        default_scripts = {
            "vuepy": "vuepy.js",
            "vue": "vue.js",
            "vuex": "vuex.js",
            "vue-router": "vue-router.js",
        }
        scripts = {"vuepy": True, "vue": True}
        custom_scripts = config.get("scripts", {})
        if isinstance(custom_scripts, list):
            custom_scripts = {k: k for k in custom_scripts}
        scripts.update(custom_scripts)
        config["scripts"] = {
            k: default_scripts[k] if v is True else v for k, v in scripts.items() if v
        }

    def _parse_component_config(self, config):
        # if config refers to sub-components
        conponent_config = {}
        if "components" in config:
            for component_path in config["components"]:
                config_file = Path(self.path, component_path, "vuepy.yml")
                if config_file.exists():
                    with open(config_file, "r") as fh:
                        conponent_config = yaml.safe_load(fh.read())
            # add template, templates and scripts to main vuepy.yml config
                if "templates" in conponent_config:
                    # added the prefix to the path
                    for k,v in  conponent_config["templates"].items():
                        conponent_config["templates"][k] = f"{component_path}/{v}"
                    if "templates" in config:
                        config["templates"].update(conponent_config["templates"])
                    else:
                        config["templates"] = conponent_config["templates"]

                if "stylesheets" in conponent_config:
                    for k,v in  conponent_config["templates"].items():
                        conponent_config["templates"][k] = f"{component_path}/{v}"
                    if "stylesheets" in config:
                        config["stylesheets"] = list(set(config["stylesheets"]+ conponent_config["stylesheets"]))
                    else:
                        config["stylesheets"] = conponent_config["stylesheets"]

                if "scripts" in conponent_config:
                    for k,v in  conponent_config["templates"].items():
                        conponent_config["templates"][k] = f"{component_path}/{v}"
                    if "scripts" in config:
                        config["scripts"].update(conponent_config["scripts"])
                    else:
                        config["scripts"] = conponent_config["scripts"]



    def load_config(self):
        config_file = Path(self.path, "vuepy.yml")
        config = {}
        if config_file.exists():
            with open(config_file, "r") as fh:
                config = yaml.safe_load(fh.read())

        # Handle components folders
        self._parse_component_config(config)

        self._normalize_config(config)
        print(f"Config is {config}")
        embed()
        return config

    def render_index(self, config):
        brython_args = config.get("brython_args", {})
        if brython_args:
            joined = ", ".join(f"{k}: {v}" for k, v in brython_args.items())
            brython_args = f"{{ {joined} }}"
        else:
            brython_args = ""

        return Template(IndexTemplate.decode("utf-8")).render(
            stylesheets=config.get("stylesheets", []),
            scripts=config.get("scripts", {}),
            templates={
                id_: Path(self.path, template).read_text("utf-8")
                for id_, template in config.get("templates", {}).items()
            },
            brython_args=brython_args,
        )

    def setup(self):
        config = config = self.load_config()
        self.directory("application", "/", Path(self.path), deep=True)
        self.directory("vuepy", "/vue", VuePath, deep=True)

        entry_point = config.get("entry_point", "app")
        self.content(
            "entry_point", "/__entry_point__.py", lambda: f"import {entry_point}\n"
        )
        self.content("index", "/", lambda: self.render_index(config))
        for route in StaticContents:
            self.content(route, route, partial(StaticContents.get, route))

    def content(self, endpoint, route, content):
        raise NotImplementedError()

    def directory(self, endpoint, route, path, deep=False):
        raise NotImplementedError()

    def deploy(self, **kwargs):
        raise NotImplementedError()
