from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def encrypt_image(input_image_path, output_image_path, key):
    try:
        image = Image.open(input_image_path)
        pixels = image.load()

        width, height = image.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                new_r = (g + key) % 256
                new_g = (r + key) % 256
                new_b = (b + key) % 256

                pixels[x, y] = (new_r, new_g, new_b)

        image.save(output_image_path)
        messagebox.showinfo("Success", f"Image encrypted and saved as {output_image_path}")

    except FileNotFoundError:
        messagebox.showerror("Error", f"The file {input_image_path} was not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def decrypt_image(input_image_path, output_image_path, key):
    try:
        image = Image.open(input_image_path)
        pixels = image.load()

        width, height = image.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                original_r = (g - key) % 256
                original_g = (r - key) % 256
                original_b = (b - key) % 256

                pixels[x, y] = (original_r, original_g, original_b)

        image.save(output_image_path)
        messagebox.showinfo("Success", f"Image decrypted and saved as {output_image_path}")

    except FileNotFoundError:
        messagebox.showerror("Error", f"The file {input_image_path} was not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def choose_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", ".png;.jpg;.jpeg"), ("All Files", ".*")]
    )
    return file_path

def handle_encrypt():
    input_image = choose_image()
    if input_image:
        output_image = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("PNG files", ".png"), ("All Files", ".*")]
        )
        key = int(entry_key.get())
        encrypt_image(input_image, output_image, key)

def handle_decrypt():
    input_image = choose_image()
    if input_image:
        output_image = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("PNG files", ".png"), ("All Files", ".*")]
        )
        key = int(entry_key.get())
        decrypt_image(input_image, output_image, key)

window = tk.Tk()
window.title("Image Encryption Tool")

label_key = tk.Label(window, text="Enter Encryption Key:")
label_key.pack(pady=5)

entry_key = tk.Entry(window)
entry_key.pack(pady=5)

button_encrypt = tk.Button(window, text="Encrypt Image", command=handle_encrypt)
button_encrypt.pack(pady=10)

button_decrypt = tk.Button(window, text="Decrypt Image", command=handle_decrypt)
button_decrypt.pack(pady=10)

window.mainloop()
