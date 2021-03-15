from vue import VueComponent

class App(VueComponent):
    template = "#index"
    message = "TEST"


App("#app")
