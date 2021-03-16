from vue import VueComponent
from components.top_menu.top_menu import TopMenu
from components.list_item.list_item import ListItem

class App(VueComponent):
    template = "#index"

TopMenu.register("top-menu")
ListItem.register("list-item")


App("#app")
