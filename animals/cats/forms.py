from django import forms
from django.contrib.formtools.wizard import FormWizard


class ContactWizard(FormWizard):
#    def get_form(self, step, *args):
#        form = super(ContactWizard, self).get_form(step)
#        try:
#            form.narrow_scope(self.previous_fields)
#        except AttributeError:
#            pass
#        return form

    def get_template(self, step):
        # use "step" if you want to use specific templates for certain steps
        return 'animals/cats/wizard.html'

    def done(self, request, form_list):
        # form list is a list of form objects.
        return HttpResponseRedirect('/cats')


class DependentForm(forms.Form):
    def narrow_scope(self, previous_fields):
        pass

class ContactForm1(DependentForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm1, self).__init__(*args, **kwargs)
        choices = [('1', '1'), ('2', '2')]
        self.fields['items'].choices = choices
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
    items = forms.MultipleChoiceField()


class ContactForm2(DependentForm):
    message = forms.CharField(widget=forms.Textarea)
    other_items = forms.MultipleChoiceField()

    def narrow_scope(self, previous_fields):
        choices = [('3', '3'), ('4', '4')]
        self.fields['other_items'].choices = choices
