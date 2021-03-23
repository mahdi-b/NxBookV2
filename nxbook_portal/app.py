from vue import VueComponent, VueStore, mutation, computed
# from components.top_menu.top_menu import TopMenu
from components.list_item.list_item import TextListItem
from components.custom_list.custom_list import CustomList

# TopMenu.register("top-menu")
TextListItem.register("list-item")
CustomList.register("custom-list")

class Store(VueStore):
    answers = {}
    hints = {}

    @mutation
    def update_param(self, param_name, new_value, name=None):
        print(f"I am updating the {param_name}")
        setattr(self, param_name, new_value)

    # @mutation
    # def update_answers(self, new_answers, name=None):
    #     print("I am updating the answers")
    #     self.answers = new_answers




class App(VueComponent):
    template = "#index"
    q_name = ""
    q_text = ""
    q_details = ""
    q_instructions = ""
    q_type = "multiple"

    @computed
    def answers(self):
        return self.store.answers

    @computed
    def hints(self):
        return self.store.hints

    @computed
    def json_representation(self):
        return {"name": self.q_name,
                "text": self.q_text,
                "details": self.q_details,
                "instructions": self.q_instructions,
                "type":self.q_type,
                "answers": self.answers,
                "hints": self.hints}


    def submit(self):
        print("In main: I am submitted because I button was pressed")

App("#app", store=Store())
