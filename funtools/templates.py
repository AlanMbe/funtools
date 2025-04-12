from funtools import smart_window

def print_data(data):
    print("name:", data.get("username"))
    print("age:", data.get("age"))

# made a window
smart_window(
    title="window",
    controls=[
        {"type": "entry", "name": "username", "placeholder": "Alan"},
        {"type": "entry", "name": "age", "placeholder": "11"},
        {"type": "button", "text": "print_data", "on_click": print_data}
    ]
)

from funtools import smart_window

def display_selected_tab(data):
    print("NoteBook:", data.get("selected_tab"))
    print("Combo:", data.get("dropdown"))

# mede a window
smart_window(
    title="window",
    controls=[
        {"type": "combobox", "name": "dropdown", "values": ["Option 1", "Option 2", "Option 3"]},
        {"type": "notebook", "tabs": [
            {"name": "Tab 1", "controls": [
                {"type": "entry", "name": "tab1_input", "placeholder": "Tab 1"}
            ]},
            {"name": "Tab 2", "controls": [
                {"type": "entry", "name": "tab2_input", "placeholder": "Tab 2"}
            ]}
        ]},
        {"type": "button", "text": "send", "on_click": display_selected_tab}
    ]
)
from funtools import StatsTool


data = [12, 15, 7, 10, 6, 14, 20, 18, 22]

stats = StatsTool(data)
stats.plot_line()
stats.plot_bar(labels=["A", "B", "C", "D", "E", "F", "G", "H", "I"])
stats.plot_pie()
stats.show_histogram()


from funtools import Captcha


captcha = Captcha(n=6, width=300, height=100)
captcha.generate()
captcha.show()
captcha.save("captcha.png")


from funtools import *

r = Role('photo.png')# made a role
while True:
    update()
    r.forward(10)# right and forward
    r.right(20)