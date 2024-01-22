from PIL import Image
import os

def split_image_2x2(input_path, output_path):
    try:
        os.makedirs(output_path, exist_ok=True)
        image_files = [f for f in os.listdir(input_path) if f.lower().endswith('.png')]
        
        for filename in image_files:
            image_path = os.path.join(input_path, filename)
            img = Image.open(image_path)
            
            width, height = img.size
            new_width, new_height = width // 2, height // 2
            
            top_left = img.crop((0, 0, new_width, new_height))
            top_right = img.crop((new_width, 0, width, new_height))
            bottom_left = img.crop((0, new_height, new_width, height))
            bottom_right = img.crop((new_width, new_height, width, height))
            
            new_filenames = [f"{os.path.splitext(filename)[0]}_{suffix}.png" for suffix in ['tl', 'tr', 'bl', 'br']]
            new_paths = [os.path.join(output_path, new_filename) for new_filename in new_filenames]
            
            top_left.save(new_paths[0], "PNG")
            top_right.save(new_paths[1], "PNG")
            bottom_left.save(new_paths[2], "PNG")
            bottom_right.save(new_paths[3], "PNG")
            
            print(f"Split {filename} into 4 images.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "output_images"
    split_image_2x2(input_folder, output_folder)
