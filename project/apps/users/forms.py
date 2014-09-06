# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import User


class SignUpForm(forms.ModelForm):

    """
    Require username when a user signs up
    """

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    username = forms.CharField(
        label=_(u"Username"),
        max_length=75,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
    password1 = forms.CharField(
        label=_(u"Password"),
        max_length=128,
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}),
    )
    password2 = forms.CharField(
        label=_(u"Repeat password"),
        max_length=128,
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}),
    )

    def clean_username(self):
        username = self.cleaned_data["username"].strip()
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("The username is already used!")
        except User.DoesNotExist:
            return username

    def clean(self):
        """
        Verifies that the values entered into the password fields match
        """
        super(SignUpForm, self).clean()
        if self.cleaned_data['password1'] and self.cleaned_data['password2']:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(
                    "Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class SignInForm(forms.Form):

    username = forms.CharField(
        label=_(u"Username"),
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
    password = forms.CharField(
        label=_(u"Password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}),
    )

    class Meta:
        fields = ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data.get("username", "")
        username = username.strip()
        return username
