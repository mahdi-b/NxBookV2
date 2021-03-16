from vue import VueComponent

class ListItem(VueComponent):
    template = "#listitem"
    # message = "TEST"
    # element_id: str = "element_1"
    placeholder_list : str = "please enter your question here"

    def remove_list_element(self, event):
        print(f"removing {event.target.parent.id} from the list")


