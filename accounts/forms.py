from django import forms

from django.contrib.auth import get_user_model
User = get_user_model() 

class AccountSignupForm(forms.ModelForm):

    password = forms.CharField(label="Senha", max_length=50, widget=forms.widgets.PasswordInput())


    class Meta:

        model = User # conecta o form com o model padrão de usuário
        fields = ('username', 'email', 'password', )