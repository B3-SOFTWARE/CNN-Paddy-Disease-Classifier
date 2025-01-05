import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Initialize the global variables
selected_image_path = None
preprocessed_image = None
model = None

# Function to select an image
def select_image():
    global selected_image_path
    selected_image_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    if selected_image_path:
        # Display the selected image
        img = Image.open(selected_image_path)
        img.thumbnail((300, 300))  # Resize for display in the GUI
        img = ImageTk.PhotoImage(img)
        selected_image_label.configure(image=img)
        selected_image_label.image = img
        messagebox.showinfo("Image Selected", f"Selected Image: {selected_image_path}")

# Function to preprocess the image
def preprocess_image():
    global preprocessed_image, selected_image_path
    if not selected_image_path:
        messagebox.showerror("Error", "Please select an image first.")
        return
    
    # Preprocess the selected image
    img = image.load_img(selected_image_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0  # Normalize
    preprocessed_image = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Display the preprocessed image
    plt.imshow(img)
    plt.title("Preprocessed Image")
    plt.axis("off")
    plt.show()
    messagebox.showinfo("Preprocessing Complete", "The image has been preprocessed.")

# Function to load the model
def load_model_file():
    global model
    model_path = filedialog.askopenfilename(filetypes=[("H5 Model files", "*.h5")])
    if model_path:
        model = load_model(model_path)
        messagebox.showinfo("Model Loaded", f"Model loaded from: {model_path}")

# Function to predict the class
def predict_class():
    global model, preprocessed_image
    if not model:
        messagebox.showerror("Error", "Please load a model first.")
        return
    if preprocessed_image is None:
        messagebox.showerror("Error", "Please preprocess an image first.")
        return
    
    # Predict the class
    predictions = model.predict(preprocessed_image)
    class_idx = np.argmax(predictions, axis=-1)[0]
    class_labels = [
        'Normal', 'Disease 1', 'Disease 2', 'Disease 3', 
        'Disease 4', 'Disease 5', 'Disease 6', 'Disease 7', 
        'Disease 8', 'Disease 9'
    ]
    predicted_class = class_labels[class_idx]
    messagebox.showinfo("Prediction", f"Predicted Class: {predicted_class}")

# Build the Tkinter GUI
root = tk.Tk()
root.title("Disease Classifier")
root.geometry("600x600")

# Create buttons and labels
select_image_button = tk.Button(root, text="Select Image", command=select_image)
select_image_button.pack(pady=10)

selected_image_label = tk.Label(root, text="Selected Image Will Appear Here")
selected_image_label.pack(pady=10)

preprocess_button = tk.Button(root, text="Preprocess Image", command=preprocess_image)
preprocess_button.pack(pady=10)

load_model_button = tk.Button(root, text="Load Model", command=load_model_file)
load_model_button.pack(pady=10)

predict_button = tk.Button(root, text="Predict Class", command=predict_class)
predict_button.pack(pady=10)

# Run the application
root.mainloop()
