from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.tarefas.search()

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = app_tables.tarefas.add_row(tarefa=self.tarefas.text,Status=True)
    l = list(self.repeating_panel_1.items)+[result]
    self.repeating_panel_1.items = l
    self.tarefas.text=""

