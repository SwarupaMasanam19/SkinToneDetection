import cv2
import numpy as np
from sklearn.cluster import KMeans
from tkinter import Tk, filedialog, Label, Button
from PIL import Image, ImageTk

# Function to detect skin tone
def detect_skin_tone(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((100, 100))  # Resize for faster processing
    img_array = np.array(image).reshape(-1, 3)

    kmeans = KMeans(n_clusters=1, random_state=0, n_init=10)
    kmeans.fit(img_array)
    dominant_color = kmeans.cluster_centers_[0].astype(int)

    hex_color = "#{:02x}{:02x}{:02x}".format(dominant_color[0], dominant_color[1], dominant_color[2])
    return hex_color, dominant_color

# Function to open file dialog
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        hex_color, rgb_color = detect_skin_tone(file_path)
        result_label.config(text=f"Skin Tone: {hex_color}\nRGB: {rgb_color}")

        img = Image.open(file_path)
        img.thumbnail((250, 250))
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img

# Create Tkinter UI
root = Tk()
root.title("Skin Tone Detector")

Button(root, text="Upload Image", command=upload_image, font=("Arial", 12)).pack(pady=10)
image_label = Label(root)
image_label.pack()
result_label = Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

root.mainloop()
