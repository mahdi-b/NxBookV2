
from vue import VueComponent, VueRouter, VueRoute

class Add(VueComponent):
    template = "<div>Add</div>"

class Edit(VueComponent):
    template = "<div>Edit</div>"

class Delete(VueComponent):
    template = "<div>Delete</div>"

class Router(VueRouter):
    routes = [
        VueRoute("/foo", Add),
        VueRoute("/bar", Edit),
        VueRoute("/fun", Delete),
    ]



class App(VueComponent):
    template = """
        <div>
            <p>
                <router-link to="/foo">Add</router-link>
                <router-link to="/bar">Edit</router-link>
                <router-link to="/fun">Delete</router-link>
            </p>
            <router-view></router-view>
        </div>
    """

App("#app", router=Router())
