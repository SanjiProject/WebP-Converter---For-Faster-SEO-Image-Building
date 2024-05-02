from PIL import Image
import os

def convert_to_webp(input_path, output_path):
    try:
        img = Image.open(input_path)
        output_folder = os.path.dirname(output_path)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        output_path_with_extension = os.path.splitext(output_path)[0] + ".webp"
        img.save(output_path_with_extension, 'WEBP')
        print(f"Converted {input_path} to {output_path_with_extension}")
    except Exception as e:
        print(f"Error converting {input_path}:", e)

def batch_convert_to_webp(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    supported_formats = ['.png', '.jpg', '.jpeg', '.gif']

    print("Converting images to WEBP...")
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        if os.path.isfile(input_path) and any(filename.lower().endswith(ext) for ext in supported_formats):
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0])
            convert_to_webp(input_path, output_path)

# Input and output folders
input_folder = "1. Put Your Images Here"
output_folder_webp = "2. Images Export"

# Convert images to WebP
batch_convert_to_webp(input_folder, output_folder_webp)
