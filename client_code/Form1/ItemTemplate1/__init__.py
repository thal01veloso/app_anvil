from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def apagar_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.item.delete()
    self.remove_from_parent()


  