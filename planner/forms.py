from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class StudentSignUpForm(UserCreationForm):
    # Fields necessary (first name, last name, enrollment year, major)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    enrollment_year = forms.IntegerField(required=True)
    major = forms.CharField(max_length=30, required=True)
    school_path = forms.ChoiceField(choices=Student.SCHOOL_PATHS)

    # meta class for the fields necessary, using built-in User model
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'school_path', 'enrollment_year', 'major']

    # saves data
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            # Create the related Student profile
            Student.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                school_path=self.cleaned_data['school_path'],
                enrollment_year=self.cleaned_data['enrollment_year'],
                major=self.cleaned_data['major']
            )
        return user