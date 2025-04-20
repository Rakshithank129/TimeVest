from django import forms
from django.contrib.auth.models import User
from userapp.models import user_profile
from django_recaptcha.fields import ReCaptchaField 

class userForm(forms.ModelForm):
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)
    class Meta:
        model = User
        # fields = "__all__"
        fields =['username','email','password']

class userFormProfile(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = ['phone','age','address','user_img']
    captcha = ReCaptchaField()

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email'] 

class InvestmentForm(forms.Form):
    name = forms.CharField(label='Name',max_length=100)
    age = forms.IntegerField(label='Age')
    years_of_investment = forms.IntegerField(label='Years of Investment')
    amount = forms.DecimalField(label='Investment Amount',max_digits=10,decimal_places=2)