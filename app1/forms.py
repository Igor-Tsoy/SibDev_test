from django import forms
from .validators import validate_csv


class UploadFileForm(forms.Form):
    file = forms.FileField(validators=[validate_csv])