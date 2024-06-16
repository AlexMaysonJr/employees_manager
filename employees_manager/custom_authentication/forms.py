from django_registration.forms import RegistrationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import CustomUser


class CustomRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser

    def __init__(self, *args, **kwargs):
        super(CustomRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Register'))