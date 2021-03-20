import os
import random


def get_extenstion(filename: str) -> str:
    _, ext = os.path.split(os.path.basename(filename))
    return ext


def upload_image_path(instance, filename):
    ext = get_extenstion(filename)
    new_filename = f"{random.randint(1,216546172576123)}{ext}"
    return f"image/products/{instance}{new_filename}"
