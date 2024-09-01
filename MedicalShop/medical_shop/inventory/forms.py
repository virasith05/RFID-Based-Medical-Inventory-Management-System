from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'rfid_tag', 'location', 'original_quantity', 'quantity']
