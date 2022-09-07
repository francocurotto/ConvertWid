from urwid import *

quantity = Text("Voltage")
unit = Text("V")
columns = Columns([quantity, unit])
value = Edit(edit_text="10")
pile = Pile([columns, value])
linebox = LineBox(pile, "Voltage, Current, Resistance")
filler = Filler(linebox)
loop = MainLoop(filler)
loop.run()
