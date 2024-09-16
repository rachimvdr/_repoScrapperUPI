import os
import requests
import re

# Define the base URL pattern with placeholders
base_url_template = "http://reader-repository.upi.edu/index.php/display/img/{}/{:03d}/{}"

# Define the ranges for the placeholders
range_1 = range(1, 8)
range_2 = range(0, 201)

# Function to extract the ID (number) from the user input URL
def extract_id_from_url(url):
    # Use regex to find the number in the URL
    match = re.search(r'/(\d+)', url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid URL format. No ID found.")

# Ask the user for the URL
user_url = input("link repo upi yang ingin kamu download, misal by @rachimvdr : https://repository.upi.edu/112863/ , masukkan :")

# Extract the ID from the user-provided URL
image_id = extract_id_from_url(user_url)

# Specify the directory where you want to save the downloaded images
output_directory = f"downloaded_images_{image_id}"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate through the placeholders and download images
for value_1 in range_1:
    for value_2 in range_2:
        # Construct the URL with the current values and extracted image ID
        url = base_url_template.format(image_id, value_2, value_1)

        # Get the image data
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200: #@rachimvdr
            # Generate a filename based on the placeholders
            filename = f"image_{image_id}_{value_1}_{value_2:03d}.png"

            # Define the full path to save the image
            save_path = os.path.join(output_directory, filename)

            # Save the image to the specified directory
            with open(save_path, "wb") as file:
                file.write(response.content)
                print(f"Downloaded: {save_path}")
        else:
            print(f"Failed to download: {url}")

print("Download completed.")
