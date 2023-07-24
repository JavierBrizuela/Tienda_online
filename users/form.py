from django import forms
from users.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=128, required=True, widget= forms.TextInput(attrs={
        'class':"form-control",
        'placeholder':'Nombre de usuario',
        'id':'username',
    }))
    firstmame = forms.CharField(label='Nombre', widget= forms.TextInput(attrs={
        'class':"form-control",
        'placeholder':'Nombre',
        'id':'firstname',
    }))
    email = forms.EmailField(label='Correo', required=True, widget= forms.EmailInput(attrs={
        'class':"form-control",
        'placeholder':'Correo electronico',
        'id':'email',
    }))
    password = forms.CharField(label='Contraseña', required=True, widget= forms.PasswordInput(attrs={
        'class':"form-control",
        'id':'password',

    }))
    password2 = forms.CharField(label='Confirmar contraseña', required=True, widget= forms.PasswordInput(attrs={
        'class':"form-control",
        'id':'password2',

    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario ya esta en uso')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya existe')
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('password2'):
            self.add_error('password2', 'Las contraseñas deben ser iguales')
     
    def save(self):
        
        return User.objects.create_user(
                                self.cleaned_data.get('username'),
                                self.cleaned_data.get('email'),
                                self.cleaned_data.get('password')
        )