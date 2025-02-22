from django import forms
from website.models import Contact, Newsletter
from captcha.fields import CaptchaField
from phonenumber_field.formfields import PhoneNumberField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    phone_number = PhoneNumberField(region="IR")
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'subject', 'message']
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].required = False

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ['email']