from django import forms

from prison.models import Warden

GENDER_CHOICES = {"Male": "Male", "Female": "Female"}

class WardenForm(forms.ModelForm):
    Gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    class Meta:
        model = Warden
        fields = ['FirstName', 'LastName', 'Email', 'Age', 'Weight','Gender','ServiceNumber']
        widgets = {
            'FirstName': forms.TextInput(attrs={'class': 'form-control'}),
            'LastName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Age': forms.DateInput(attrs={'type':'number',}),
            'Weight': forms.TextInput(attrs={'type':'number','min':'0','max':'100'}),
            'ServiceNumber': forms.TextInput(attrs={ 'type':'number','class':'form-control'}),
            'Gender': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)