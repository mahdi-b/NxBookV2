from vue import VueComponent, computed

class CustomList(VueComponent):
    template = "#customlist"
    listName: str

    items = [{"id": "0", "text": "Some_text"}, {"id": "1", "text": "Other text"}]
    item_id = "Parent"
    items_positions = {}
    next_item_id = len(items)

    def add_new_item(self, event):
        print("Adding new item")
        item_id = self.next_item_id
        self.next_item_id += 1

        self.items_positions[item_id] = len(self.items)
        self.items.append({"id": f"{item_id}", "text": "More text"})

    def clear_list(self, event):
        self.items = []
        print("clearing_list")

    def remove_item(self, item_id):
        print(item_id.split("_"))
        item_id = int(item_id.split("_")[1])
        print(f"removing item {item_id} from the list")
        item_position = -1
        for i,item in enumerate(self.items):
            if int(item["id"]) ==  item_id:
                item_position = i

        if item_position == -1:
            print(f"Cannot remove {item_id}: not a valid index in the list")
        else:
            print(f"Item is at position {item_position}")
            self.items.pop(item_position)

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

