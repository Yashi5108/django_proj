from django import forms
from .models import Index

class IndexCSVUploadForm(forms.ModelForm):
    class Meta:
        model = Index
        fields = ['csv_file']
