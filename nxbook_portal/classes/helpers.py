# MIT license
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
