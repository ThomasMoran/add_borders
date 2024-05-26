#!/usr/bin/env python3

import os
import sys  
from PIL import Image

def add_border(image_path, output_folder, border_size):
    """
    Add a white border to an image without resizing it.

    Args:
    image_path (str): Path to the input image file.
    output_folder (str): Path to the folder to save the output image file.
    border_size (int): Size of the border to add around the image.
    """
    with Image.open(image_path) as img:
        # Create a new image with increased dimensions
        new_size = (img.width + 2 * border_size, img.height + 2 * border_size)
        new_img = Image.new("RGB", new_size, "white")

        # Paste the original image onto the new image with a border
        new_img.paste(img, (border_size, border_size))

        # Save the new image
        filename = os.path.basename(image_path)
        output_path = os.path.join(output_folder, filename)
        new_img.save(output_path)

def process_images(input_folder, output_folder, border_size):
    """
    Process all images in the input folder, adding a white border to each image.

    Args:
    input_folder (str): Path to the folder containing input images.
    output_folder (str): Path to the folder to save the output images.
    border_size (int): Size of the border to add around the images.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):
            input_path = os.path.join(input_folder, filename)
            add_border(input_path, output_folder, border_size)

def main():
    input_folder = os.getcwd()  # Current directory
    output_folder = os.path.join(input_folder, "with_borders")

    # Set border size
    border_size = 50
    if len(sys.argv) > 1:
        try:
            border_size = int(sys.argv[1])
        except ValueError:
            print("Error: Border size must be an integer. Using default size.")

    # Process images
    process_images(input_folder, output_folder, border_size)

if __name__ == "__main__":
    main()
