from django.forms import Form, CharField, EmailField, Textarea


class ContactForm(Form):
    name = CharField(max_length=255)
    email = EmailField()
    content = CharField(widget=Textarea)