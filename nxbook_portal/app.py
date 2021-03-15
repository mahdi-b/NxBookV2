from vue import VueComponent
from components.topmenu import TopMenu

class App(VueComponent):
    template = "#index"
    message = "TEST"

TopMenu.register("top-menu")

App("#app")
