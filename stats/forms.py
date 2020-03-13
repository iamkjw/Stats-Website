from django import forms
from .models import Game

class GameRegisterForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'image', 'company']

    def __init__(self, *args, **kwargs):
        super(GameRegisterForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

