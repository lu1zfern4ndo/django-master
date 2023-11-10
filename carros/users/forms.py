from django import forms
from . models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(
                'As senhas não são iguais. Tente novamente.')
        return cleaned_data

    def save(self, commit=True):
        password = self.cleaned_data.get('password')
        confirm_passeord = self.cleaned_data.get('confirm_password')

        if password and confirm_passeord and password != confirm_passeord:
            raise forms.ValidationError(
                'As senhas não são iguais. Tente novamente.')

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
