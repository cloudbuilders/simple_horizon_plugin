from django import forms
from django.contrib.formtools.wizard import FormWizard


class ContactWizard(FormWizard):
    def __init__(self, *args, **kwargs):
        super(ContactWizard, self).__init__(*args, **kwargs)
        self.previous_data = {}

    def process_step(self, request, form, step):
        super(ContactWizard, self).process_step(request, form, step)
        self.previous_data.update(form.clean())

    def get_template(self, step):
        # use "step" if you want to use specific templates for certain steps
        return 'animals/cats/wizard.html'

    def render_template(self, request, form, previous_fields, step, context=None):
        if self.previous_data:
            form.set_previous_data(self.previous_data)
        return super(ContactWizard, self).render_template(request, form,
                                                   previous_fields, step,
                                                   context)

    def done(self, request, form_list):
        # form list is a list of form objects.
        return HttpResponseRedirect('/cats')


class DependentForm(forms.Form):
    def set_previous_data(self, previous_fields):
        pass


class ContactForm1(DependentForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm1, self).__init__(*args, **kwargs)
        choices = [('1', '1'), ('2', '2')]
        self.fields['items'].choices = choices
    subject = forms.CharField(max_length=100)
    #sender = forms.EmailField()
    items = forms.MultipleChoiceField()


class ContactForm2(DependentForm):
    message = forms.CharField(widget=forms.Textarea)
    other_items = forms.MultipleChoiceField()

    def __init__(self, *args, **kwargs):
        super(ContactForm2, self).__init__(*args, **kwargs)

    def set_previous_data(self, previous_fields):
        items = previous_fields['items'] 
        choices = []
        for i in xrange(0, len(items)):
            choices += [(items[i], items[i])]
        self.fields['other_items'].choices = choices
