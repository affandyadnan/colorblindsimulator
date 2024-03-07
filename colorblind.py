import requests
from PIL import Image
from io import BytesIO
import numpy as np

def fetch_random_image():
    # Fetch a random image from Lorem Picsum
    response = requests.get("https://picsum.photos/800/600")
    image = Image.open(BytesIO(response.content))
    return image

def simulate_color_blindness(image, blindness_type='trinatopia'):
    # Convert the image to numpy array
    img_array = np.array(image)

    # Define matrices for different types of color blindness
    if blindness_type == 'protanopia':
        # Protanopia (red-blind)
        transform_matrix = np.array([[0.567, 0.433, 0],
                                      [0.558, 0.442, 0],
                                      [0,     0.242, 0.758]])
    elif blindness_type == 'deuteranopia':
        # Deuteranopia (green-blind)
        transform_matrix = np.array([[0.625, 0.375, 0],
                                      [0.7,   0.3,   0],
                                      [0,     0.3,   0.7]])
    elif blindness_type == 'tritanopia':
        # Tritanopia (blue-blind)
        transform_matrix = np.array([[0.95,  0.05,  0],
                                      [0,     0.433, 0.567],
                                      [0,     0.475, 0.525]])
    else:
        raise ValueError("Invalid color blindness type")

    # Apply transformation
    sim_img_array = np.dot(img_array[..., :3], transform_matrix.T)
    sim_img_array = np.clip(sim_img_array, 0, 255).astype(np.uint8)

    # Create simulated image
    sim_img = Image.fromarray(sim_img_array)

    return sim_img

if __name__ == "__main__":
    original_image = fetch_random_image()
    original_image.show()
    simulated_image = simulate_color_blindness(original_image, blindness_type='protanopia')
    simulated_image.show()
