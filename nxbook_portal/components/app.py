from vue import VueComponent

from custom_list.custom_list import CustomList
from list_item.list_item import TextListItem

CustomList.register("custom-list")
TextListItem.register("list-item")

class App(VueComponent):
    template = """<custom-list listName="test_list"></custom-list>"""




App("#app")

