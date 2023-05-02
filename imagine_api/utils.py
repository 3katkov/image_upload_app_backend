from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def process_image(image_instance, plan):
    image = Image.open(image_instance.image.path) 
    urls = []

    for size in plan.thumbnail_sizes:
        thumbnail = image.copy()
        thumbnail.thumbnail((size, size), Image.ANTIALIAS)
        temp_file = BytesIO()
        thumbnail.save(temp_file, format='JPEG')
        temp_file.seek(0)

        file_name = f'{image_instance.pk}_{size}.jpg'
        image_instance.image.storage.save(f'thumbnails/{file_name}', ContentFile(temp_file.read()))

    image_instance.save()

# explicitly setting image upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

## upload to function
def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])
