from vue import VueComponent

from custom_list import CustomList

CustomList.register("custom-list")

class App(VueComponent):
    template = "<custom-list></custom-list>"




App("#app")

