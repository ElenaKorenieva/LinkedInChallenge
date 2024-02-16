from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserInfo


def validate_no_numbers(value):
    if any(char.isdigit() for char in value):
        raise forms.ValidationError(
            'Name and job title should not contain numbers.')
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['job_title']

    job_title = forms.CharField(
        max_length=255,
        validators=[validate_no_numbers],
        widget=forms.TextInput(attrs={'placeholder': 'Your job title'}),
        error_messages={
            'min_length': 'Job title should be at least 14 characters long.'}
    )

class SignupForm(UserCreationForm):
    jobtitle = forms.CharField(max_length=255, required=True,
                                help_text='Required. Should be at least 14 characters long.',
                                validators=[validate_no_numbers],
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Your job title'}),
                                error_messages={
                                    'min_length': 'Job title should be at least 14 characters long.'
                                })

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', 'jobtitle')

        # username = forms.CharField(widget=forms.TextInput(attrs={
        #     'placeholder': 'Your username',
        #     'class': 'w-full py-4 px-6 rounded-xl h-2'
        # }))
        # email = forms.CharField(widget=forms.EmailInput(attrs={
        #     'placeholder': 'Your email address',
        #     'class': 'w-full py-4 px-6 rounded-xl'
        # }))
        # password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        #     'placeholder': 'Your password',
        #     'class': 'block w-full py-4 px-6 rounded-xl h-4'
        # }))
        # password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        #     'placeholder': 'Repeat your password',
        #     'class': 'w-full py-4 px-6 rounded-xl'
        # }))
        # jobtitle = forms.CharField(widget=forms.TextInput(attrs={
        #     'placeholder': 'Enter your job title',
        #     'class': 'w-full py-4 px-6 rounded-xl'
        # }))

        INPUT_CLASSES = 'h-8 w-full py-4 px-6 rounded-xl border'

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Your username',
                'class': INPUT_CLASSES
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your email address',
                'class': INPUT_CLASSES
                }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Enter your password',
                'class': INPUT_CLASSES
                }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Repeat your password',
                'class': INPUT_CLASSES
                }),
            'jobtitle': forms.TextInput(attrs={
                'placeholder': 'Enter your job title',
                'class': INPUT_CLASSES
            }),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
