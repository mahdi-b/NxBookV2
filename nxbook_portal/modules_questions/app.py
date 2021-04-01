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
    selected_q = []
    questions = []
    nx_firebase = None


    @computed
    def questions_display(self):
        if self.questions:
            print(self.questions[0])
        return [{"value": q[0], "text": q[2][:60]+"..."}
                    for q in self.questions]
        # return [{"value": "A", "text": "B"}]

    def created(self):
        # self.nx_firebase = NxFirebaseBackEnd.NxFirebaseBackEnd()
        print("getting list of modules")
        asyncio.run(self.get_module_names())
        #print(self.modules)


    def mod_clicked(self, event):
        print(f"Module {self.selected_m} selected, getting its questions...")
        asyncio.run(self.get_questions())

    def ques_clicked(self, event):
        print(f"Question {self.selected_q} was clicked")

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
        print(f"now getting questions for module id {self.selected_m}")
        self.questions = [[1, None, 'Loading...', None]]
        req = await aio.ajax("POST", f"http://127.0.0.1:5001/questions/{self.selected_m}")
        print(f"just got the questions and they are: --{req.data}-- and type is {type(eval(req.data))}")
        self.questions = eval(req.data)



# used with firebase.
#     async def get_module_names(self):
#         self.modules = await self.nx_firebase.get_modules()
#
#     async def get_questions(self):
#         self.questions = await self.nx_firebase.get_questions(self.selected_m)


App("#app")
