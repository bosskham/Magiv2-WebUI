from PIL import Image
import numpy as np

# Function to read images
def read_image(path_to_image):
    image = Image.open(path_to_image).convert("L").convert("RGB")
    return np.array(image)
