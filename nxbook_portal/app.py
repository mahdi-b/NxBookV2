
from vue import VueComponent, VueRouter, VueRoute, VueStore
from vue import computed, mutation

from components.list_item.list_item import TextListItem
from components.custom_list.custom_list import CustomList

from browser import aio as asyncio

TextListItem.register("list-item")
CustomList.register("custom-list")


class Add(VueComponent):
    template = "#add"

    q_title = ""
    q_text = ""
    q_details = ""
    q_instructions = ""
    q_type = "multiple"

    modules = []
    modules_repr = [{"value": 1, "text": 'Loading...'}]
    selected_m = "1"

    @computed
    def answers(self):
        return self.store.answers


    @computed
    def json_representation(self):
        return {"name": self.q_title,
                "text": self.q_text,
		"details": self.q_details,
                "instructions": self.q_instructions,
                "type":self.q_type,
	        "answers": self.answers,
                "hints": self.hints}

    @computed
    def hints(self):
        return self.store.hints

    @computed
    def correct_answers(self):
	return self.store.correct_answers
    @computed
    def answers_explanations(self):
        return self.store.answers_explanations
    
    def mod_selected(self, event):
        print(f"Module {self.selected_m} was selected...")

    def created(self):
        print("getting list of modules")
        asyncio.run(self.get_module_names())

    async def get_module_names(self):
        print("now getting modules")
        req = await asyncio.ajax("POST", 'http://127.0.0.1:5001/modules')
        print(f"Done getting modules {req.data}")
        self.modules = eval(req.data)
        self.modules_repr = [ {"value": x[0], "text": x[1]} for x in self.modules]
    
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


class Store(VueStore):
    answers = {}
    hints = {}
    correct_answers={}
    answers_explanations={}

    @mutation
    def update_param(self, param_name, new_value, name=None):
        print(f"I am updating the {param_name}")
	setattr(self, param_name, new_value)
        
class App(VueComponent):
    template = "#index"

App("#app", router=Router(), store=Store())
