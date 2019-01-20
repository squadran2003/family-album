from django.utils import timezone
from PIL import Image as img
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='pictures')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at',)

    def save(self):
        # Opening the uploaded image
        im = img.open(self.image)
        output = BytesIO()
        # Resize/modify the image
        im = im.resize((400, 300))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(
            output, 'ImageField',
            "%s.jpeg" % self.image.name.split('.')[0],
            'jpeg', sys.getsizeof(output), None
        )
        super(Image, self).save()

    def __str__(self):
        return self.description
