from vue import VueComponent
from top_menu import TopMenu




class App(VueComponent):
    template = "<top-menu></top-menu>"

TopMenu.register("top-menu")

App("#app")
