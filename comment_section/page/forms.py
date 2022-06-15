from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=1028, required=True, label=False,
                              widget=forms.Textarea(attrs={'placeholder': 'Napisz komentarz...'}))


class PodcastForm(forms.Form):
    name = forms.CharField(max_length=128, required=True, label=False,
                           widget=forms.Textarea(attrs={'placeholder': 'Podaj nazwę podcastu...'}))
    author = forms.CharField(max_length=64, required=True, label=False,
                             widget=forms.Textarea(attrs={'placeholder': 'Podaj nazwę autora...'}))
    description = forms.CharField(max_length=1028, required=True, label=False,
                                  widget=forms.Textarea(attrs={'placeholder': 'Dodaj opis..'}))
