from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, HiddenInput, DateInput
from django import forms

from app.models.personel_details import Personal_Data




class PersonalForm(ModelForm):

    class Meta:
        model = Personal_Data

        fields = fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
