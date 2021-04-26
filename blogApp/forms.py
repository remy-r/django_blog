import datetime

from django import forms
from .models import Post
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ()
    #ields = ('name', 'email', 'body')

