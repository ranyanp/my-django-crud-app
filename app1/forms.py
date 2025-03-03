
from django import forms
from .models import data,Profile_pic

class DataForm(forms.ModelForm):
    class Meta:
        model = data
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','id':'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
    # def __init__(self, *args, **kwargs):
    #     super(DataForm, self).__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         if field=='name':
    #           field.required = False
    def __init__(self, *args, **kwargs):
        super(DataForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False

class Profile_form(forms.ModelForm):
     class Meta:
        model = Profile_pic
        fields = ['profile']

        widgets = {
           
            'profile': forms.FileInput(),
        }

