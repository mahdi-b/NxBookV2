from vue import VueComponent

class CustomList(VueComponent):
    template = "#customlist"
    items = [{"id": "1", "text": "Some_text"}, {"id": "2", "text": "Other text"}]
    item_id = "Parent"

    def add_new_item(self, event):
        print("Adding new item")


    def clear_items(self, event):
        self.items = []
        print("clearing item")

    def remove_item(self, item_id):
        print(f"removing item {item_id} from the list")
