import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from tkinter import ttk  # Import ttk widgets
from PIL import Image, ImageTk  # Pillow library for image handling; install with pip install pillow
import ctypes

# Global data storage
data = {}

# Get the value of a widget
def get(name):
    var = data.get(name)
    return var.get() if var else None

# Show information message box
def show_info(title="Information", message="This is a prompt"):
    messagebox.showinfo(title, message)

# Show warning message box
def show_warning(title="Warning", message="Be careful!"):
    messagebox.showwarning(title, message)

# Show error message box
def show_error(title="Error", message="An error occurred!"):
    messagebox.showerror(title, message)

# Ask for text input
def ask_text(title="Please Enter", prompt="Please input something:"):
    return simpledialog.askstring(title, prompt)

# Select a file
def choose_file(title="Select a file"):
    return filedialog.askopenfilename(title=title)

# Select a folder
def choose_folder(title="Select a folder"):
    return filedialog.askdirectory(title=title)

# Create a custom window
def simple_window(title="Custom Window", buttons={"OK": lambda: print("You clicked OK")}):
    win = tk.Tk()
    # Set DPI awareness for the application
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

    # Get the screen's scale factor
    ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)

    # Adjust the scaling of the application
    win.tk.call('tk', 'scaling', ScaleFactor/75)

    win.title(title)
    for text, command in buttons.items():
        btn = tk.Button(win, text=text, command=lambda cmd=command, w=win: (cmd(), w.destroy()))
        btn.pack(padx=10, pady=5)
    win.mainloop()

# Create a smart window with flexible controls
def smart_window(title="Window", size=(400, 300), bg_color="#ffffff", bg_image=None, styletm=None, controls=[]):
    win = tk.Tk()
    win.title(title)
    win.geometry(f"{size[0]}x{size[1]}")
    win.configure(bg=bg_color)
    style = ttk.Style(win)
    try:
        style.theme_use(styletm)
    except:
        print('This style is unavailable')
    
    # Optional background image setup
    if bg_image:
        try:
            img = Image.open(bg_image)
            img = img.resize(size)
            bg = ImageTk.PhotoImage(img)
            bg_label = tk.Label(win, image=bg)
            bg_label.image = bg  # Prevent garbage collection
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print("Failed to load background image:", e)

    def get_widget(control):
        type_ = control.get("type", "label")
        if type_ == "label":
            return tk.Label(win, text=control.get("text", ""), bg=bg_color)
        elif type_ == "entry":
            var = tk.StringVar()
            name = control.get("name", f"entry{len(data)}")
            entry = tk.Entry(win, textvariable=var)
            var.set(control.get("placeholder", ""))
            data[name] = var
            return entry
        elif type_ == "button":
            cmd = control.get("command")  # User-defined function
            if callable(cmd):
                return tk.Button(win, text=control.get("text", "Button"), command=cmd)
            else:
                def default_action():
                    result = {key: var.get() for key, var in data.items()}
                    if callable(control.get("on_click")):
                        control["on_click"](result)
                return tk.Button(win, text=control.get("text", "Button"), command=default_action)

        elif type_ == "combobox":  # Drop-down list
            var = tk.StringVar()
            combobox = ttk.Combobox(win, textvariable=var, values=control.get("values", []))
            var.set(control.get("default", ""))
            data[control.get("name", f"combobox{len(data)}")] = var
            return combobox
        elif type_ == "notebook":  # Notebook tabs
            notebook = ttk.Notebook(win)
            for tab in control.get("tabs", []):
                tab_frame = tk.Frame(notebook)
                for ctrl in tab.get("controls", []):
                    widget = get_widget(ctrl)
                    widget.pack(pady=5)
                notebook.add(tab_frame, text=tab.get("name", "Tab"))
            return notebook
        else:
            return tk.Label(win, text=f"[Unknown widget: {type_}]", bg=bg_color)

    # Widget arrangement
    for ctrl in controls:
        widget = get_widget(ctrl)
        widget.pack(pady=5)

    win.mainloop()

    # Return data dictionary
    return data
