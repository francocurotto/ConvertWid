from urwid import *

class UnitEditor(BoxAdapter):
    def __init__(self, quantity):
        self.quantity = quantity
