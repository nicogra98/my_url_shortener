from django import forms
from urls.models import UrlModel

class URLForm(forms.Form):
    url = forms.URLField(label='URL')