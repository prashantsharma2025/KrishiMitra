
from django import forms


class CropInputForm(forms.Form):
    N = forms.FloatField(
        label="Nitrogen (N)",
        min_value=0,
        max_value=200,
    )
    P = forms.FloatField(
        label="Phosphorus (P)",
        min_value=0,
        max_value=200,
    )
    K = forms.FloatField(
        label="Potassium (K)",
        min_value=0,
        max_value=250,
    )
    temperature = forms.FloatField(
        label="Temperature (°C)",
        min_value=-10,
        max_value=60,
    )
    humidity = forms.FloatField(
        label="Humidity (%)",
        min_value=0,
        max_value=100,
    )
    ph = forms.FloatField(
        label="Soil pH",
        min_value=0,
        max_value=14,
    )
    rainfall = forms.FloatField(
        label="Rainfall (mm)",
        min_value=0,
        max_value=5000,
    )
