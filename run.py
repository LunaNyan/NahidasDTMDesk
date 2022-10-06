VERSION = "1.0.0"

from mods import ui as ui

print("Welcome to Nahida's DTM Desk")
print("Sound Canvas SysEx Generator, Ver " + VERSION)
print("\nUse Number keys to select menu\nJust press Enter to go back home\nCtrl+C to exit\n")

while True:
    ui.ui_main()
