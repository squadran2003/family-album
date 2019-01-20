from django.forms import ModelForm
from .models import Image


class UploadForm(ModelForm):
    class Meta:
        model = Image
        fields = ['description', 'image']
