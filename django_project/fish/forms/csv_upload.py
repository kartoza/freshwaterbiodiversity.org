# coding=utf-8
"""Forms to upload csv.
"""

from django import forms
from fish.models.csv_document import CsvDocument


class CsvUploadForm(forms.ModelForm):
    """Csv upload form"""
    class Meta:
        model = CsvDocument
        fields = '__all__'
