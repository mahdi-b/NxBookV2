from vue import VueComponent, data, computed
from vue.utils import js_lib, js_load
from vue.bridge import Object
from browser import  timer
import NxFirebaseBackEnd
from browser import aio as asyncio
import json

class App(VueComponent):

    template = "#index"
    modules = [{"value": 1, "text": 'Loading...'}]
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
        asyncio.run(self.get_questions())

    def ques_clicked(self, event):
        print(f"Question {self.selected_m} was clicked")


    async def get_module_names(self):
        self.modules = await self.nx_firebase.get_modules()

    async def get_questions(self):
        self.questions = await self.nx_firebase.get_questions(self.selected_m)

    def created(self):
        self.nx_firebase = NxFirebaseBackEnd.NxFirebaseBackEnd()
        print("getting list of modules")
        asyncio.run(self.get_module_names())
        #print(self.modules)

App("#app")
