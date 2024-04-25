#     #for 12000x4000px

from PIL import Image
import os

# # Open the image
# image = Image.open("E:\Instagram\ZenIt\Final\Zenit OG.jpg")

# # Get the dimensions of the image
# width, height = image.size

# # Calculate the dimensions of each cropped image
# crop_width = width // 3
# crop_height = height

# # Construct the output file paths
# input_dir, input_filename = os.path.split(image.filename)
# output_dir = input_dir

# # Crop the image and save the cropped images
# for i in range(3):
#     left = i * crop_width
#     right = left + crop_width
#     top = 0
#     bottom = crop_height
#     cropped_image = image.crop((left, top, right, bottom))
#     output_filename = os.path.join(output_dir, f'cropped_image_{i+1}.jpg')
#     cropped_image.save(output_filename)





# for 6000x6000px
# 3 x 3



# def crop_image(input_path):
#     # Load the input image
#     img = Image.open(input_path)
    
#     # Ensure the image is 6000 x 6000
#     if img.size != (6000, 6000):
#         raise ValueError("Input image must be 6000 x 6000 pixels")

#     # Define the size of each cropped image
#     crop_width = 2000
#     crop_height = 2000

#     # Initialize a counter for naming cropped images
#     image_count = 9

#     # Extract the directory from the input path
#     output_folder = os.path.dirname(input_path)

#     # Iterate through a 3x3 grid to crop the image
#     for i in range(3):
#         for j in range(3):
#             # Calculate the left, upper, right, and lower boundaries for the crop
#             left = j * crop_width
#             upper = i * crop_height
#             right = left + crop_width
#             lower = upper + crop_height

#             # Crop the image
#             cropped_img = img.crop((left, upper, right, lower))

            
#             # Create a filename for the cropped image
#             filename = os.path.join(output_folder, f"image{image_count}.png")

#             # Save the cropped image in the same folder as the input image
#             cropped_img.save(filename)

#             print(f"Cropped image saved as: {filename}")

#             # Increment the image count
#             image_count -= 1

#     print(f"Cropped images saved in: {output_folder}")

# # Example usage
# input_path = "E:\Instagram\ZenIt\Final\Zenit OG.jpg" # Specify the path to your 6000x6000px image

# # Call the function to crop the image
# crop_image(input_path)

# 4 x 3


def crop_image(input_path):

    img = Image.open(input_path)

    crop_width = 2000
    crop_height = 2000

    image_count = 12 

    output_folder = os.path.dirname(input_path)

    for i in range(4):
        for j in range(3):
            left = j * crop_width
            top = i * crop_height
            right = left + crop_width
            bottom = top + crop_height

            cropped_img = img.crop((left, top, right, bottom))

            filename = os.path.join(output_folder, f"image{image_count}.png")
            print(f"Saved as: {filename}")

            cropped_img.save(filename)

            image_count -= 1

    print(f"Saved in: {output_folder}")


input_path = "E:\Instagram\Porsche 911 GT3\Final\GT3.jpg"

crop_image(input_path)