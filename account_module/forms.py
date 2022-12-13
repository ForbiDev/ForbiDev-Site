from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

x = 1
class RegisterForm(forms.Form):
    username = forms.CharField(label='نام کاربری', validators=[
        validators.MaxLengthValidator(100),
        validators.RegexValidator('^[a-zA-Z0-9]*$', message='نام کاربری باید شامل اعداد و حروف باشد'),
    ])
    email = forms.EmailField(label='ایمیل',widget=forms.EmailInput(),validators=[
        validators.EmailValidator(),
        validators.MaxLengthValidator(100),
    ])
    password = forms.CharField(label='کلمه عبور',widget=forms.PasswordInput(),validators=[
        validators.MinLengthValidator(8),
    ])
    confirm_password = forms.CharField(label='کلمه عبور',widget=forms.PasswordInput())
    first_name = forms.CharField(label='نام',validators=[validators.MaxLengthValidator(100),])
    last_name = forms.CharField(label='نام خانوادگی',validators=[validators.MaxLengthValidator(100),])

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        conf = self.cleaned_data.get('confirm_password')
        if conf == password:
            return True
        else:
            raise ValidationError('کلمه عبور با تکرار یکسان نمیباشد')

