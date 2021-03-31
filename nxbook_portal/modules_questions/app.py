from vue import VueComponent, data, computed
from vue.utils import js_lib, js_load
from browser import  timer, aio
import NxFirebaseBackEnd
from browser import aio as asyncio
import json
import urllib.request
import urllib.request


class App(VueComponent):

    template = "#index"
    modules = []
    modules_repr = [{"value": 1, "text": 'Loading...'}]
    selected_m = ""
    selected_ques = [{"value": 1, "text": 'A'}, {"value": 2, "text": 'B'}]
    questions = []
    nx_firebase = None



    @computed
    def questions_display(self):
        if self.questions:
            print(self.questions[0])
        return [{"value": q.value, "text": q.data["question"]}
                    for q in self.questions]
        # return [{"value": "A", "text": "B"}]


    def mod_clicked(self, event):
        print(f"Module {self.selected_m} selected, getting it questions...")
        # asyncio.run(self.get_questions())

    def ques_clicked(self, event):
        print(f"Question {self.selected_m} was clicked")

    # used with sqlite.
    async def get_module_names(self):
        print("now getting modules")
        req = await aio.ajax("POST", 'http://127.0.0.1:5001/modules')
        # self.modules_repr = [{"value": x[1], "text": x[1]} for x in self.modules]
        print(f"just got the modules and they are: --{req.data}-- and type is {type(eval(req.data))}")
        self.modules = eval(req.data)
        self.modules_repr = [ {"value": x[0], "text": x[1]} for x in self.modules]
        print(f"modules_repr is: {self.modules_repr}")

    async def get_questions(self):
        print("now getting questions")
        #self.questions = await self.nx_firebase.get_questions(self.selected_m)


# used with firebase.
#     async def get_module_names(self):
#         self.modules = await self.nx_firebase.get_modules()
#
#     async def get_questions(self):
#         self.questions = await self.nx_firebase.get_questions(self.selected_m)

    def created(self):
        self.nx_firebase = NxFirebaseBackEnd.NxFirebaseBackEnd()
        print("getting list of modules")
        asyncio.run(self.get_module_names())
        #print(self.modules)

App("#app")
