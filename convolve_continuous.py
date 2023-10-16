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

class convolve_continuous(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)
        self.initialize_styles()
        self.create_empty_frame()
        self.create_title()
        self.create_labeled_frame()
        self.create_menu_buttons()
        self.create_image_labels()
        self.update_image1()
        self.update_image2()
        self.create_convolve_button()
        self.create_back_button()

    def show_convolution(self):
        signal1 = self.selected_option1.get()
        signal2 = self.selected_option2.get()
        signal1 = signal1[-1].lower()
        signal2 = signal2[-1].lower()
        subprocess.run(["python", PATH/"../show_conv_continuous.py", signal1, signal2])

    def initialize_styles(self):
        self.master.style.configure("ConvolveTitle.TLabel", font=("Courier New", 24, "bold"), foreground="#40a231")
        self.master.style.configure("Subtitle.TLabel", font=("Courier New", 10))

    def create_empty_frame(self):
        frame = ttk.Frame(self, padding=10, style=DARK)
        frame.pack(fill=BOTH, expand=YES)
        self.title_frame = frame
        self.create_separator()
        frame = ttk.Frame(self, padding=10, style=DARK)
        frame.pack(fill=BOTH, expand=YES)
        self.convolve_frame = frame

    def create_title(self):
        title_label = ttk.Label(master=self.title_frame, text="Convolución continua", style="ConvolveTitle.TLabel")
        self.title_label = title_label
        self.pumpkin = ttk.PhotoImage(file = PATH / '64/Buy.png')
        pumpkin_label = ttk.Label(image=self.pumpkin, master=self.title_frame)
        self.pumpkin_label = pumpkin_label
        pumpkin_label.pack(side=LEFT, fill=X, expand=NO, pady=5, padx=20)
        title_label.pack(side=LEFT, fill=X, expand=NO, pady=5, padx=5)
        
    def create_separator(self):
        separator = ttk.Separator(self, orient=HORIZONTAL, style=SUCCESS)
        separator.pack(fill=X, pady=5, padx=10)
        self.separator = separator

    def create_labeled_frame(self):
        """Create a labeled frame"""
        labeled_frame = ttk.Labelframe(self.convolve_frame, text="Señal fija", style=INFO)  # Create a labeled frame
        labeled_frame.pack(side=LEFT, fill=BOTH, expand=YES, padx=5, pady=20)  # Pack the labeled frame
        self.labeled_frame_1 = labeled_frame
        labeled_frame = ttk.Labelframe(self.convolve_frame, text="Señal en movimiento", style=PRIMARY)  # Create a labeled frame
        labeled_frame.pack(side=LEFT, fill=BOTH, expand=YES, padx=5, pady=20)  # Pack the labeled frame
        self.labeled_frame_2 = labeled_frame

    def create_menu_buttons(self):
        menu_label1 = ttk.Label(self.labeled_frame_1, text="Seleccione una señal:")
        menu_label1.pack(pady=10, padx=20)

        options = ["Señal A", "Señal B", "Señal C", "Señal D", "Señal E", "Señal F"]
        self.selected_option1 = ttk.StringVar()

        menu_button1 = ttk.Combobox(self.labeled_frame_1, values=options, textvariable=self.selected_option1, bootstyle="INFO")
        menu_button1.bind("<<ComboboxSelected>>", self.update_image1)  # Bind the event handler to update image for x_t
        menu_button1.pack(pady=10, padx=20)

        menu_label2 = ttk.Label(self.labeled_frame_2, text="Seleccione una señal:")
        menu_label2.pack(pady=10, padx=20)

        self.selected_option2 = ttk.StringVar()

        menu_button2 = ttk.Combobox(self.labeled_frame_2, values=options, textvariable=self.selected_option2, bootstyle="PRIMARY")
        menu_button2.bind("<<ComboboxSelected>>", self.update_image2)  # Bind the event handler to update image for h_t
        menu_button2.pack(pady=10, padx=20)

    def create_image_labels(self):
        # Define dictionaries to map options to image paths for each combo box
        self.image_paths_x_t = {
            "Señal A": PATH/"x_t/a.png",
            "Señal B": PATH/"x_t/b.png",
            "Señal C": PATH/"x_t/c.png",
            "Señal D": PATH/"x_t/d.png",
            "Señal E": PATH/"x_t/e.png",
            "Señal F": PATH/"x_t/f.png",
        }

        self.image_paths_h_t = {
            "Señal A": PATH/"h_t/a.png",
            "Señal B": PATH/"h_t/b.png",
            "Señal C": PATH/"h_t/c.png",
            "Señal D": PATH/"h_t/d.png",
            "Señal E": PATH/"h_t/e.png",
            "Señal F": PATH/"h_t/f.png",
        }

        # Create labels with default images for both Comboboxes
        self.image_label_x_t = ttk.Label(self.labeled_frame_1)
        self.image_label_x_t.pack(pady=10)
        self.image_label_h_t = ttk.Label(self.labeled_frame_2)
        self.image_label_h_t.pack(pady=10)

    def update_image1(self, event=None):
        # Get the selected option for x_t
        selected_option_x_t = self.selected_option1.get()
        image_path_x_t = self.image_paths_x_t.get(selected_option_x_t, PATH / "others/Ghost.png")
        self.update_image_label(self.image_label_x_t, image_path_x_t)

    def update_image2(self, event=None):
        # Get the selected option for h_t
        selected_option_h_t = self.selected_option2.get()
        image_path_h_t = self.image_paths_h_t.get(selected_option_h_t, PATH /"others/Ghost.png")
        self.update_image_label(self.image_label_h_t, image_path_h_t)

    def update_image_label(self, label, image_path):
        image = ttk.PhotoImage(file=image_path)
        label.config(image=image)
        label.image = image  # Keep a reference to the image

    def create_convolve_button(self):
        container = ttk.Frame(self)
        container.pack(fill=X)
        convolve_button = ttk.Button(container, text="Convolucionar", width=30, style="SUCCESS-OUTLINE", command=self.show_convolution)
        convolve_button.pack(side=BOTTOM, fill=X, expand=YES, pady=10, padx=30)
        self.convolve_button = convolve_button

    def create_back_button(self):
        container = ttk.Frame(self)
        container.pack(fill=X)
        back_button = ttk.Button(container, text="Volver", width=10, style="PRIMARY-OUTLINE", command=back_to_main)
        back_button.pack(side=LEFT, expand=NO, pady=10, padx=30)
        self.back_button = back_button  



if __name__ == '__main__':
    app = ttk.Window("Laboratorio Señales y Sisemas", "halloween")
    app.iconbitmap(PATH / "others/logo.ico")
    convolve_continuous(app)
    app.mainloop()