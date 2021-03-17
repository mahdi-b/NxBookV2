from vue import VueComponent, computed

class CustomList(VueComponent):
    template = "#customlist"
    listName: str

    items = [{"id": "1", "text": "Some_text"}, {"id": "2", "text": "Other text"}]
    item_id = "Parent"


    def add_new_item(self, event):
        print("Adding new item")
        item_id = 1
        if len(self.items):
            item_id = int(self.items[-1]["id"]) + 1
        self.items.append({"id": f"{item_id}", "text": "More text"})

    def clear_list(self, event):
        self.items = []
        print("clearing_list")

    def remove_item(self, item_id):
        print(item_id.split("_"))
        item_id = int(item_id.split("_")[1])
        print(f"removing item {item_id} from the list")
        if 1 <= item_id <= len(self.items):
            self.items.pop(item_id-1)
        else:
            print(f"Cannot remove {item_id}: not a valid index in the list")

    def on_updated_item(self):
        print("I am in th elist component. \nThe list has changed and it's time to push it to the store")
        self.store.commit(f"update_{self.listName}", self.items)

    # @computed
    # def list_items(self):
    #     return self.items
    #
    # @list_items.setter
    # def list_items(self):
    #     print("value of my items i changing....")

