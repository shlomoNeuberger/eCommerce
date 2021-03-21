
import os
import random
import string
from django.utils.text import slugify


def get_extenstion(filename: str) -> str:
    _, ext = os.path.split(os.path.basename(filename))
    return ext


def upload_image_path(instance, filename):
    ext = get_extenstion(filename)
    new_filename = f"{random.randint(1,216546172576123)}{ext}"
    return f"image/products/{instance}{new_filename}"


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def unique_order_generator(instance, new_order_id=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    oreder_id = f"{random_string_generator(size=4)}-{instance.cart.id}"

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=oreder_id).exists()
    if qs_exists:
        oreder_id = f"{random_string_generator(size=4)}-{oreder_id}"
        return unique_order_generator(instance, oreder_id)
    return oreder_id
