from django.core.exceptions import ValidationError
from django.forms import HiddenInput
from django.forms.models import ModelForm


class BaseApplicationForm(ModelForm):
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        required_fields = self.instance.required_fields
        hidden_fields = self.instance.hidden_fields
        for field in self.fields:
            if field in required_fields:
                self.fields.get(field).required = True
            if field in hidden_fields:
                self.fields.get(field).widget = HiddenInput()

#    def clean_first_name(self):
#        age = self.cleaned_data.get("age", "")
#       if "e" in age:
#            raise ValidationError("People with 'e' in their first name need not apply.")
#        # else
#       return age

#    class Media:
#        css = {
#            "all": ("recommender/css/job_application.css",)
#        }
