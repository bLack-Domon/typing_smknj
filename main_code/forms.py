from django import forms
from .models import TypingResult

class TypingResultForm(forms.ModelForm):
    class Meta:
        model = TypingResult
        fields = ['nama', 'jenis_kelamin', 'asal_sekolah', 'skor', 'screenshot']

        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'jenis_kelamin': forms.Select(attrs={'class': 'form-select'}),
            'asal_sekolah': forms.TextInput(attrs={'class': 'form-control'}),
            'skor': forms.NumberInput(attrs={'class': 'form-control'}),
            'screenshot': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
