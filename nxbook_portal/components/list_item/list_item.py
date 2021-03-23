from vue import VueComponent, computed
from browser import timer

def debounce(func, milliseconds, leading=False):
  """Debounce a function"""
  t = None
  leading = leading

  def wrapper(*args, **kwargs):
    nonlocal t, leading

    def cancel():
      if t:
        timer.clear_timeout(t)

    def run():
      func(*args, **kwargs)
      cancel()

    if leading:
       leading = False
       run()
       return lambda : None, lambda : None   # Calling run or cancel does nothing

    cancel()

    t = timer.set_timeout(run, milliseconds)

    return run, cancel

  return wrapper

class TextListItem(VueComponent):
    template = "#textlistitem"
    myItem: dict = None
    message="abc"

    debounce_item_text = None


    def update_item_text(self, new_value):
        print(f"In debouce: the value is {new_value}")
        self.myItem.text = new_value
        self.emit("updated-item")

    def created(self):
        self.debounce_item_text = debounce(self.update_item_text, 1000, leading=False)

    @computed
    def itemText(self):
        return self.myItem.text

    @itemText.setter
    def itemText(self, new_value):
        print(f"editing itemModel, new value is {new_value}")
        print("calling debounce here")
        self.debounce_item_text(new_value)

    def remove(self, event):
        item_id = None
        if event.target.id:
            item_id = event.target.id
        else:
            item_id = event.target.parentNode.id
        print("**** removing: " + item_id)
        self.emit("remove-item", item_id)

