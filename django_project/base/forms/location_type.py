# coding=utf-8

from django import forms
from base.models.location_type import (
    LocationTypeAllowedGeometry,
)


class LocationTypeForm(forms.ModelForm):
    allowed_geometry = forms.ModelMultipleChoiceField(
        queryset=LocationTypeAllowedGeometry.objects,
        widget=forms.CheckboxSelectMultiple(),
        required=True,
    )
