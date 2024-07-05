import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageResizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        self.image_path = None
        self.image = None
        self.tk_image = None

        self.canvas = tk.Canvas(root, bg="#ffffff", bd=2, relief="groove")
        self.canvas.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        self.controls_frame = tk.Frame(root, bg="#f0f0f0")
        self.controls_frame.pack(pady=10)

        self.upload_button = tk.Button(self.controls_frame, text="Upload Image", command=self.upload_image)
        self.upload_button.grid(row=0, column=0, padx=5)

        self.width_label = tk.Label(self.controls_frame, text="Width:")
        self.width_label.grid(row=0, column=1, padx=5)

        self.width_entry = tk.Entry(self.controls_frame, width=5)
        self.width_entry.grid(row=0, column=2, padx=5)

        self.height_label = tk.Label(self.controls_frame, text="Height:")
        self.height_label.grid(row=0, column=3, padx=5)

        self.height_entry = tk.Entry(self.controls_frame, width=5)
        self.height_entry.grid(row=0, column=4, padx=5)

        self.resize_button = tk.Button(self.controls_frame, text="Resize", command=self.resize_image)
        self.resize_button.grid(row=0, column=5, padx=5)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if self.image_path:
            self.image = Image.open(self.image_path)
            self.display_image(self.image)

    def display_image(self, image):
        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

    def resize_image(self):
        if self.image:
            try:
                width = int(self.width_entry.get())
                height = int(self.height_entry.get())
                resized_image = self.image.resize((width, height), Image.Resampling.LANCZOS)
                self.display_image(resized_image)
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter valid width and height values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageResizer(root)
    root.mainloop()
