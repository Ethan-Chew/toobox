### ⓖ ⒢ ℊ Granwyn's Part ℊ ⒢ ⓖ ###
# and Ethan's Part :D #
import tkinter as tk
from tkinter import Canvas, PhotoImage, ttk
import os
import time

import config
from PIL import ImageTk, Image

# Important UI Details
## 1. Default Font Size is *20*

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.setup_widgets()
        # Variable to track if fullscreen
        self.fullScreen = False
        # Set fullscreen
        self.fullScreenBindings()
        self.notify("Toobox", "Testing Notification", "Boop")

    # Full Screen Toggles
    def fullScreenBindings(self):
        root.attributes("-fullscreen", self.fullScreen)
        root.bind("f", self.toggleFullScreen)
        root.bind("<F11>", self.toggleFullScreen)
        root.bind("<Escape>", self.quitFullScreen)
    def toggleFullScreen(self, event):
        self.fullScreen = not self.fullScreen
        root.attributes("-fullscreen", self.fullScreen)

    def quitFullScreen(self, event):
        self.fullScreen = False
        root.attributes("-fullscreen", self.fullScreen)

    # Setup Widgets
    def setup_widgets(self):
        # Panedwindow
        self.paned = ttk.PanedWindow(self, orient="horizontal")
        self.paned.pack(fill="both", expand=True, anchor="center")

        # Selection Pane
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=1)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.pane_1)
        self.scrollbar.pack(side="right", fill="y")

        # Treeview
        self.treeview = ttk.Treeview(
            self.pane_1,
            selectmode="browse",
            yscrollcommand=self.scrollbar.set
        )


        ## Treeview Label
        self.treeViewTopLab = ttk.Label(self.pane_1, text="Tools:", font=("", 20, 'bold'))
        self.treeViewTopLab.pack(side="top", pady=20, anchor="w", fill="x")

        self.treeview.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)

        ## Treeview columns
        self.treeview.column("#0", anchor="w", width=80)
        ## Define treeview data
        treeview_data = [
            ("", 1, "Chemistry"),
            (1, 2, "Periodic Table"),
            (1, 3, "Salt Solubilities"),
            (1, 4, "Chemical Equation"),
            (1, 5, "Ionic Equation"),
            ("", 6, "Mathematics"),
            (6, 7, "Calculator"),
            (6, 8, "Equations"),
            (8, 9, "Simultaneous"),
            (8, 10, "Quadratic"),
            (8, 11, "Cubic"),
            (8, 12, "Quartic"),
            (6, 13, "Matrices"),
            (6, 14, "Inequalities"),
            (6, 15, "Mensuration"),
            (15, 16, "Area"),
            (16, 17, "Rectangle/Square"),
            (16, 18, "Triangle"),
            (16, 19, "Parallelogram"),
            (16, 20, "Rhombus"),
            (16, 21, "Trapezium"),
            (16, 22, "Circle/Semicircle"),
            (15, 23, "Volume"),
            (23, 24, "Pyramid"),
            (24, 25, "Triangle-Based"),
            (24, 26, "Square-Based"),
            (24, 27, "Cone"),
            (23, 28, "Sphere/Hemisphere"),
            (23, 29, "Prism"),
            (29, 30, "Triangular Prism"),
            (29, 31, "Cylinder"),
            (29, 32, "Cuboid/Cube"),
            (6, 33, "Percentage"),
            (6, 34, "Coordinate Geometry"),
            (34, 35, "Gradient"),
            (34, 36, "Distance/Length"),
            (34, 37, "Perpendicular Lines"),
            (6, 38, "Circles"),
            (38, 39, "Circle Properties"),
            (38, 40, "Equation of Circle"),
            ("", 41, "Revision"),
            (41, 42, "Grade Planner"),
            (41, 43, "Grade Calculator"),
        ]

        # Insert treeview data
        for item in treeview_data:
            self.treeview.insert(
                parent=item[0], index="end", iid=item[1], text=item[2]
            )
            if item[0] == "" or item[1] in {8, 15, 16, 23, 24, 29, 34, 38, 41}:
                self.treeview.item(item[1], open=False)  # Open parents

        self.treeview.see(21)

        # Home Screen UI
        ## Main Home Screen Frame
        self.homeScreen = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.homeScreen, weight=10)
        self.notebook = ttk.Notebook(self.homeScreen, padding=3)
        self.notebook.pack(fill="both", expand=True)

        ## Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.pack(side="right")

        ## Top Labels
        self.welcomeFrame = ttk.Frame(self.notebook)
        self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
        self.helloUserLab = ttk.Label(self.welcomeFrame ,text="Hello, {}".format(config.username), font=("",50, 'bold'))
        self.helloUserLab.pack(pady=2)
        self.welcomeLab = ttk.Label(self.welcomeFrame, text="Welcome to Toobox!",font=("", 15))
        self.welcomeLab.pack(side="left")

        ## Toobox Information
        self.tooboxInfoFrame = ttk.Frame(self.notebook)
        self.tooboxInfoFrame.pack(side="bottom", padx=25, pady=18, anchor="w")
        self.imgCanvas = Canvas(self.tooboxInfoFrame, width = 300, height = 300)
        self.imgCanvas.pack()
        img = ImageTk.PhotoImage(Image.open("./src/images/AppIcon.png"))
        self.imgCanvas.create_image(20, 20, anchor="w", image=img)
        self.appDescText = ttk.Label(text="Test")

    def on_tree_select(self, event):
##        currentlySelected = self.treeview.item(self.treeview.focus())['text']
##        config.currentlySelected = currentlySelected
        for item in self.treeview.selection():
            print(str("Selected Item: "+self.treeview.item(item, "text")))

    def _quit(self):
        root.quit()
        root.destroy()

    def notify(self, title, text, sound):
        os.system("""
                  osascript -e 'display notification "{}" with title "{}" sound name "{}"'
                  """.format(text, title, sound))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Toobox")

    # Simply set the theme
    root.tk.call("source", "sun-valley.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = root.winfo_screenwidth()
    # int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = root.winfo_screenheight()
    # int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

    root.state('zoomed')

    root.mainloop()
### ⓖ ⒢ ℊ Granwyn's Part ℊ ⒢ ⓖ ###
