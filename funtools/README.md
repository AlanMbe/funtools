# funtools

🧸 **funtools** is a beginner-friendly Python toolkit for creating GUIs, games, captchas, charts, and more — built by an 11-year-old coder!

## ✨ Features

- ✅ Easy GUI creation with `guitools`
- 🔢 Captcha generation with `captchatools`
- 📊 Data visualization with `charttools` (based on `matplotlib`)
- 📦 One-click executable packaging with `packtools` (using PyInstaller)
- 🎮 Game utilities with `gametools` *(coming soon — needs the `imp` module)*
- 🖼 Image editor with `imagetools`
## 📦 Included Modules

- `pygame`
- `pymunk`
- `matplotlib`
- `tkinter`
- `os`
- `imp` *(for compatibility support in some tools)*
- `pillow`

## Developer

**Alan Mbe**, a **Hmong** boy from Guizhou, China.
At just **11 years old**, I'm already creating Python libraries! 🧠🔥

## Usage
###game
```python

from funtools.gametools import *
setup(800,600)
r = Role(image)

while True:
  update()
  ......
```

###GUI
```python
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
```

## 📅 Update History

- **v0.1 – Apr 12, 2025**  
  Initial version with support for:
  - Basic GUI creation  
  - Captcha image generation  
  - Data chart plotting
- **v0.2 - Apr 13, 2025**
  - New tool: Imagetools! 🔥
