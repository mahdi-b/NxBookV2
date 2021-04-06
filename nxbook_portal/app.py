
from vue import VueComponent, VueRouter, VueRoute, VueStore
from vue import computed, mutation

from components.list_item.text_list_item import TextListItem
#from components.list_item.ineteger_list_item import IntegerListItem
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
    errors = []

    @computed
    def answers(self):
        return self.store.answers


    @computed
    def json_representation(self):
        answers = [{"answer": x["text"], "correct": False } for x in self.answers]
        for c_a in self.correct_answers:
            answers[int(c_a["text"])]["correct"] = True
        for i, expl in enumerate(self.answers_explanations):
            answers[i]["explanation"] = expl["text"]


        return {
        "module_id": self.selected_m,
        "title": self.q_title,
        "text": self.q_text,
		"details": self.q_details,
        "instructions": self.q_instructions,
        "type":self.q_type,
        "answers": answers,
        "hints": self.hints
        }

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

    def submit(self, event):
        self.errors = []
        # 1. A question should have a non empty title and text
        if len(self.q_title) < 5 or len(self.q_text) < 5:
            self.errors.append("A question should have a non-empty title and text")

        # 1. make sure that we have at least 2 answers and none is empty
        if len(self.answers) < 2 or any([len(x["text"]) == 0 for x in self.answers]):
            self.errors.append("At least 2 answers are required and none should be empty")
        # 2. correct answers should non empty ids
        if any([x["text"]=="" for x in self.correct_answers]):
            self.errors.append("Correct answers should not be empty")
        # 3. correct answers should have values that map to valid answers
        answers_ids = [x["id"] for x in self.answers]
        if any([x["text"] not in answers_ids for x in self.correct_answers]):
            self.errors.append("Correct answers should have values that map to valid answers")
        # 4. There shoudl be the same number of answers_explanations as answers.
        if len(self.answers_explanations) != len(self.answers):
            self.errors.append("Number of answers explanations should be the same as the number of answers")
        # 4. None of the hints should be empty
        if any([x["text"]=="" for x in self.hints]):
            self.errors.append("None of the hints should be empty")
        print(self.errors)


class Edit(VueComponent):
    template = "<div>Edit</div>"

class Delete(VueComponent):
    template = "<div>Delete</div>"

class Router(VueRouter):
    routes = [
        VueRoute("/add", Add),
        VueRoute("/edit", Edit),
        VueRoute("/delete", Delete),
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
