from components.image_reading import image_reading
from components.image_taking import image_taking
from PIL import ImageTk, Image as PILImage
from tkinter import *
import customtkinter
from servo_control import ServoControl

class main_menu(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Braille Translation Device")
        self.geometry("500x800")
        self._create_function_screen()

    def _create_function_screen(self):

        customtkinter.CTkLabel(self, text="Braille Translation Device").place(relx=0.5, rely=0.2, anchor=CENTER)

        customtkinter.CTkButton(self, text="Take Image", command=self._take_image).place(relx=0.5, rely=0.4, anchor=CENTER)

        customtkinter.CTkButton(self, text="Read Image", command=self._read_image).place(relx=0.5, rely=0.6, anchor=CENTER)

    def _take_image(self):
        image_taking()
        customtkinter.CTkLabel(self, text = " ", image=self._load_image('./UI/images/temp.png')).place(relx=0.5, rely=0.8, anchor=CENTER)
    
    def _read_image(self):
        results = image_reading('./UI/images/temp.png')
        customtkinter.CTkLabel(self, text=results).place(relx=0.5, rely=0.95, anchor=CENTER)
        servo_control = ServoControl()
        servo_control.control_servos(results)
        servo_control.close_connection()

    def _load_image(self, image_path):
        img = PILImage.open(image_path)
        img = img.resize((300, 200), PILImage.NEAREST)
        return ImageTk.PhotoImage(img)        

# Create an instance of the main_menu class
if __name__ == "__main__":
    app = main_menu()
    app.mainloop()
