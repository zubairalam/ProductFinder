from django.forms import ModelForm
from apps.pages.models import *

class AddProvider(ModelForm):
    class Meta:
        model = Providers
        fields = ["name","description","url",'logo']

