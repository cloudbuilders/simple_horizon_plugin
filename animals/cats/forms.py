from django import forms
from django.contrib.formtools.wizard import FormWizard


class ContactWizard(FormWizard):
#    def get_form(self, step):
#        form = super(ContactWizard, self).get_form(step)
#        form.initial = {'subject': 'hola', 'choices': ['a', 'b']}
#        return form

    def get_template(self, step):
        # use "step" if you want to use specific templates for certain steps
        return 'animals/cats/wizard.html'

    def done(self, request, form_list):
        # form list is a list of form objects.
        return HttpResponseRedirect('/cats')


class ContactForm1(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ContactForm1, self).__init__(*args, **kwargs)
        choices = [('1', '1'), ('2', '2')]
        self.fields['items'].choices = choices
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
    items = forms.MultipleChoiceField()


class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
