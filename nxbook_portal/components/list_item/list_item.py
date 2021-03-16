from vue import VueComponent

class ListItem(VueComponent):
    template = "#listitem"
    myItem: dict = None
    message="abc"
    def remove(self, event):
        if event.target.id:
            print("**** removing: " + event.target.id+"---")
        else:
            print("**** removing: " + event.target.parentNode.id+"---")


