# First install python on your system and Run this below command
# pip install Pillow

from PIL import Image
import os

# Define the directory containing the images
input_dir = "Input_images"

# Define the directory to save the converted images
output_dir = "Output_images"

# Get a list of all files in the input directory
files = os.listdir(input_dir)

# Loop through each file in the input directory
for file_name in files:
    # Open the image file
    image_path = os.path.join(input_dir, file_name)
    with Image.open(image_path) as img:
        # Compress the image and convert it to WebP format
        img.save(os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}.webp"), "WEBP", quality=80)
