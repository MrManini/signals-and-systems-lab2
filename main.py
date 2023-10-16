import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pathlib import Path
import subprocess
import sys

PATH = Path(__file__).parent / 'icons'

def open_convolve_discrete():
    app.destroy()
    subprocess.run(["python", PATH/"../convolve_discrete.py"])
    sys.exit()

def open_convolve_continuous():
    app.destroy()
    subprocess.run(["python", PATH/"../convolve_continuous.py"])
    sys.exit()


class main(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)
        self.initialize_styles()
        self.create_title()
        self.create_separator()
        self.create_labeled_frame("Integrantes", "PRIMARY")
        self.create_subtitle()
        self.create_separator()
        self.create_labeled_frame("Opciones de convolución", "WARNING")
        self.create_buttons()
        self.place_images()

    def initialize_styles(self):
        self.master.style.configure("MainTitle.TLabel", font=("Courier New", 24, "bold"), foreground="#a42cd6")
        self.master.style.configure("Subtitle.TLabel", font=("Courier New", 10))

    def create_title(self):
        """Create a title label with a larger font size"""
        title_label = ttk.Label(self, text="¡Feliz 2do Laboratorio de Señales!", style="MainTitle.TLabel")
        title_label.pack(pady=10)
        self.title_label = title_label

    def create_separator(self):
        separator = ttk.Separator(self, orient=HORIZONTAL)
        separator.pack(fill=X, pady=5, padx=10)
        self.separator = separator

    def create_subtitle(self):
        container = ttk.Frame(self.labeled_frame, padding=5)
        container.pack(fill=X)
        #people_label = ttk.Label(text="Integrantes:", style="Subtitle.TLabel", master=container)
        #people_label.pack(pady=5, padx=3, anchor="w")
        self.people = ["Belissa Briceño", "Isabella Orozco", "Kevin Torregrosa"]
        self.icons = [
            ttk.PhotoImage(
                file=PATH / '32/Net.png'),
            ttk.PhotoImage(
                file=PATH / '32/Sickle.png'),
            ttk.PhotoImage(
                file=PATH / '32/Skeleton.png'),
        ]
        for i in range(3):
            person_label = ttk.Label(text=self.people[i], style="Subtitle.TLabel", master=container)
            image_label = ttk.Label(image=self.icons[i], master=container)
            image_label.pack(side=LEFT, fill=X, expand=NO, pady=5, padx=1)
            person_label.pack(side=LEFT, fill=X, expand=YES, pady=5, padx=3)

    def create_labeled_frame(self, text, style):
        """Create a labeled frame"""
        labeled_frame = ttk.Labelframe(self, text=text, style=style)  # Create a labeled frame
        labeled_frame.pack(fill=BOTH, expand=YES, padx=10, pady=20)  # Pack the labeled frame
        self.labeled_frame = labeled_frame

    def create_buttons(self):
        """Create the control frame with buttons"""
        container = ttk.Frame(self.labeled_frame, padding=10)
        container.pack(fill=X)
        self.buttons = []
        self.buttons.append(
            ttk.Button(
                master=container,
                text="Convolución Discreta",
                width=30,
                bootstyle="SECONDARY-OUTLINE",
                command=open_convolve_discrete
            )
        )
        self.buttons.append(
            ttk.Button(
                master=container,
                text="Convolución Continua",
                width=30,
                bootstyle="SUCCESS-OUTLINE",
                command=open_convolve_continuous
            )
        )
        for button in self.buttons:
            button.pack(side=LEFT, fill=X, expand=YES, pady=10, padx=30)

    def place_images(self):
        container = ttk.Frame(self.labeled_frame, padding=5)
        container.pack(fill=X)
        self.images = [
            ttk.PhotoImage(
                name='pumpkin',
                file=PATH / '128/Pumpkin.png'),
            ttk.PhotoImage(
                name='zombie',
                file=PATH / '128/Buy.png'),
        ]
        for image in self.images:
            image_label = ttk.Label(image=image, master=container)
            image_label.image = image  # Keep a reference to the image
            image_label.pack(side=LEFT, fill=X, expand=YES, pady=5, padx=128)


if __name__ == '__main__':
    app = ttk.Window("Segundo Laboratorio Señales y Sistemas", "halsloween")
    app.iconbitmap(PATH / "others/logo.ico")
    main_window = main(app)  # Keep a reference to the main window
    app.mainloop()