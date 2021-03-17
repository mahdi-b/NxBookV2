from vue import VueComponent, VueStore, mutation, computed
from components.top_menu.top_menu import TopMenu
from components.list_item.list_item import ListItem
from components.custom_list.custom_list import CustomList

TopMenu.register("top-menu")
ListItem.register("list-item")
CustomList.register("custom-list")

class Store(VueStore):
    questions = {}
    hints = "Hints are"


    @mutation
    def update_questions(self, new_questions, name=None):
        print("I am updating the question")
        self.questions = new_questions


class App(VueComponent):
    template = "#index"
    hints = "Some hints go here"

    @computed
    def questions(self):
        return self.store.questions



    def created(self):
        self.questions = self.store.questions

        self.hints = self.store.hints




App("#app", store=Store())
