import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pathlib import Path
import subprocess
import sys

PATH = Path(__file__).parent / 'icons'

def back_to_main():
    app.destroy()
    subprocess.run(["python", PATH/"../main.py"])
    sys.exit()


class convolve_discrete(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)
        self.initialize_styles()
        self.create_empty_frame()
        self.create_title()
        self.create_radio_buttons()
        self.create_separator()
        self.create_label()
        self.create_labeled_frames()
        self.create_image_display()
        self.preload_images()
        self.create_convolve_button()
        self.create_back_button()
          
    def show_convolution(self):
        convolution = self.radio_var.get()
        moving_signal = self.combo_var.get()
        if convolution == "Convolución 1":
            if moving_signal == "Señal x[n]":
                signal1 = "b"
                signal2 = "a"
            else:
                signal1 = "a"
                signal2 = "b"
        else:
            if moving_signal == "Señal x[n]":
                signal1 = "d"
                signal2 = "c"
            else:
                signal1 = "c"
                signal2 = "d"
        subprocess.run(["python", PATH/"../show_conv_discrete.py", signal1, signal2])

    def initialize_styles(self):
        self.master.style.configure("ConvolveTitle.TLabel", font=("Courier New", 24, "bold"), foreground="#fa7602")
        self.master.style.configure("Subtitle.TLabel", font=("Courier New", 10))

    def create_empty_frame(self):
        frame = ttk.Frame(self, padding=10, style=DARK)
        frame.pack(fill=BOTH, expand=YES)
        self.title_frame = frame
        self.create_separator()
        frame = ttk.Frame(self, padding=10, style=DARK)
        frame.pack(fill=BOTH, expand=YES)
        self.buttons_frame = frame
        frame = ttk.Frame(self, padding=10, style=DARK)
        frame.pack(fill=BOTH, expand=YES)
        self.text_frame = frame

    def create_title(self):
        title_label = ttk.Label(master=self.title_frame, text="Convolución discreta", style="ConvolveTitle.TLabel")
        self.title_label = title_label
        self.pumpkin = ttk.PhotoImage(file = PATH / '64/Pumpkin1.png')
        pumpkin_label = ttk.Label(image=self.pumpkin, master=self.title_frame)
        self.pumpkin_label = pumpkin_label
        pumpkin_label.pack(side=LEFT, fill=X, expand=NO, pady=5, padx=20)
        title_label.pack(side=LEFT, fill=X, expand=NO, pady=5, padx=5)

    def create_separator(self):
        separator = ttk.Separator(self, orient=HORIZONTAL, style=SECONDARY)
        separator.pack(fill=X, pady=5, padx=10)
        self.separator = separator

    def create_radio_buttons(self):
        self.radio_var = ttk.StringVar()  # Variable to store the selected option

        def update_images(event=None):
            self.combo_var.set("")  # Clear the combo box choice
            self.update_image_display()

        # Create radio buttons with different options
        radio_button1 = ttk.Radiobutton(
            self.buttons_frame, 
            text="Convolución 1", 
            variable=self.radio_var, 
            value="Convolución 1", 
            style=SECONDARY,
        )
        radio_button1.bind("<Button-1>", update_images)
        radio_button1.pack(side=LEFT, fill=BOTH, expand=YES, padx=80)

        radio_button2 = ttk.Radiobutton(
            self.buttons_frame, 
            text="Convolución 2", 
            variable=self.radio_var, 
            value="Convolución 2", 
            style=SECONDARY,
        )
        radio_button2.bind("<Button-1>", update_images)
        radio_button2.pack(side=LEFT, fill=BOTH, expand=YES, padx=80)

        # You can set a default option using the variable
        self.radio_var.set("Convolución 1")

    def create_label(self):
        container = ttk.Frame(self)
        container.pack(fill=X)
        menu_label1 = ttk.Label(container, text="Seleccione una señal en movimiento:")
        menu_label1.pack(side=LEFT, fill=BOTH, expand=YES, pady=10, padx=20)

        def update_images(event=None):
            self.update_image_display()

        options = ["Señal x[n]", "Señal h[n]"]
        self.combo_var = ttk.StringVar()

        menu_button1 = ttk.Combobox(container, values=options, textvariable=self.combo_var, bootstyle="SECONDARY")
        menu_button1.bind("<<ComboboxSelected>>", update_images)  # Bind the event handler to update image for x_n
        menu_button1.pack(side=LEFT, fill=BOTH, expand=YES, pady=10, padx=20)
        self.combo_var.set("")

    def create_labeled_frames(self):
        """Create a labeled frame"""
        container = ttk.Frame(self)
        container.pack(fill=X)
        labeled_frame = ttk.Labelframe(container, text="Señal fija", style=WARNING)  # Create a labeled frame
        labeled_frame.pack(side=LEFT, fill=BOTH, expand=YES, padx=5, pady=20)  # Pack the labeled frame
        self.labeled_frame_1 = labeled_frame
        labeled_frame = ttk.Labelframe(container, text="Señal en movimiento", style=DANGER)  # Create a labeled frame
        labeled_frame.pack(side=LEFT, fill=BOTH, expand=YES, padx=5, pady=20)  # Pack the labeled frame
        self.labeled_frame_2 = labeled_frame

    def create_image_display(self):
        self.image_frame1 = ttk.Frame(self.labeled_frame_1)
        self.image_frame1.pack(fill=BOTH, expand=YES)
        self.image_frame2 = ttk.Frame(self.labeled_frame_2)
        self.image_frame2.pack(fill=BOTH, expand=YES)

        # Define dictionaries to map options to sets of images
        self.image_sets = {
            ("Convolución 1", "Señal x[n]"): [PATH/"x_n/b.png", PATH/"h_n/a.png"],
            ("Convolución 1", "Señal h[n]"): [PATH/"x_n/a.png", PATH/"h_n/b.png"],
            ("Convolución 2", "Señal x[n]"): [PATH/"x_n/d.png", PATH/"h_n/c.png"],
            ("Convolución 2", "Señal h[n]"): [PATH/"x_n/c.png", PATH/"h_n/d.png"],
        }

        # Create labels for displaying images
        self.image_labels = []

        label1 = ttk.Label(self.image_frame1)
        label1.pack(side=LEFT, fill=X, expand=YES)
        self.image_labels.append(label1)
        label2 = ttk.Label(self.image_frame2)
        label2.pack(side=LEFT, fill=X, expand=YES)
        self.image_labels.append(label2)

        # Initialize image display
        self.update_image_display()

    def preload_images(self):
        for image_paths in self.image_sets.values():
            for image_path in image_paths:
                ttk.PhotoImage(file=image_path)

    def update_image_display(self):
        selected_radio = self.radio_var.get()
        selected_combo = self.combo_var.get()
        selected_images = self.image_sets.get((selected_radio, selected_combo), [PATH/"others/Cat.png", PATH/"others/Cat.png"])

        for i, image_path in enumerate(selected_images):
            image = ttk.PhotoImage(file=image_path)
            self.image_labels[i].config(image=image)
            self.image_labels[i].image = image

    def create_convolve_button(self):
        container = ttk.Frame(self)
        container.pack(fill=X)
        convolve_button = ttk.Button(container, text="Convolucionar", width=30, style="SECONDARY-OUTLINE", command=self.show_convolution)
        convolve_button.pack(side=BOTTOM, fill=X, expand=YES, pady=10, padx=30)
        self.convolve_button = convolve_button
    
    def create_back_button(self):
        container = ttk.Frame(self)
        container.pack(fill=X)
        back_button = ttk.Button(container, text="Volver", width=10, style="PRIMARY-OUTLINE", command=back_to_main)
        back_button.pack(side=LEFT, expand=NO, pady=10, padx=30)
        self.back_button = back_button

if __name__ == '__main__':
    app = ttk.Window("Laboratorio Señales y Sistemas", "halloween")
    app.iconbitmap(PATH / "others/logo.ico")
    convolve_discrete_window = convolve_discrete(app)  # Keep a reference to the convolve_discrete window
    app.mainloop()