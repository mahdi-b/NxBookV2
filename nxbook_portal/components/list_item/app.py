from vue import VueComponent

from list_item import ListItem

ListItem.register("list-item")

class App(VueComponent):
    template = "<list-item></list-item>"




App("#app")

