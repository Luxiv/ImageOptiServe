import os
from PIL import Image


def optimize_image(file_path):
    """
    Optimize the image by reducing its quality to 75%, 50%, and 25%.

    :param file_path: The path of the image file.
    :return: None
    """
    print("[X] image from queue.")
    destination_dir = "X:/ImageOptiServe/static/images/"
    image_name = str(file_path).split("/")[-1]
    image_id = image_name.split(".")[0]

    with Image.open(file_path) as image:
        for q in [75, 50, 25]:
            destination_path = f"{destination_dir}{q}percent/{image_id}.jpeg"
            image.save(destination_path, quality=q)


def unique_id_gen(path):
    """
    Generate a unique ID for the uploaded image based on the images present in the original directory.

    :param path: The path of the directory containing the original images.
    :return: An integer representing the unique ID.
    """
    sorted_image_list = sorted([int(file[:-5]) for file in os.listdir(path) if str(file).endswith(".jpeg")])
    check_list = [el for el in range(1, len(sorted_image_list) + 2)]
    return int([file_id for file_id in check_list if file_id not in sorted_image_list][0])
