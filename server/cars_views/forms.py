from django import forms
from .models import Car  # Import the Car model from your models.py

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'price', 'description', 'image_url']

        # You can customize the widgets for specific fields if needed, for example:
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
