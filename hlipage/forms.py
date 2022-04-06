from django import forms
from .models import Input
from django.contrib import messages
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineCheckboxes
#from django_crispy.bootstrap import InlineCheckboxes

from datetime import date
from django.utils import timezone
from .scripts import investigators

choicelist = investigators.all_PIs_listofstr
clist = list(zip(choicelist,choicelist))

class InputQuery(forms.Form):
    #select_all_authors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[("1", "yes"),("2", "no")], required=False)

    or_choose_which_author = forms.MultipleChoiceField(label= "", widget=forms.CheckboxSelectMultiple, choices=clist)
    min_date = forms.DateField(label= 'Min date in format DD/MM/YYYY: ')
    max_date = forms.DateField(label= 'Max date in format DD/MM/YYYY: ')

#    def __init__(self, *args, **kwargs):
#        super(InputQuery, self).__init__(*args, **kwargs)
        #Change date field's widget here
#        self.fields['or_choose_which_author'].widget = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=clist)
#        self.fields['min_date'].widget = forms.extras.widgets.SelectDateWidget()
#        self.fields['max_date'].widget = forms.extras.widgets.SelectDateWidget()


#    def clean(self):
#        cleaned_data = super().clean()
#        or_choose_which_author = cleaned_data.get("or_choose_which_author")

#        min_date = cleaned_data['min_date']
#        max_date = cleaned_data['max_date']

#        if min_date > max_date:
#            msg = "Min date is greater than max date"
#            #raise ValidationError("You have forgotten about Fred!")
#            self.add_error('min_date', msg)
        
#        if min_date > date.today():
#            msg = "Min date is in the future"
#            self.add_error('min_date', msg)

    def clean_min_date(self):
        data = self.cleaned_data['min_date']
        if data > timezone.now().date():
            raise forms.ValidationError(" Min date cannot be a future date.") 
        return data
    
    def clean(self):
        cleaned_data = super().clean()
        min_date = cleaned_data.get("min_date")
        max_date = cleaned_data.get("max_date")

        if min_date and max_date:
            if max_date < min_date:
                self.add_error('max_date', " Max date cannot be less than min date.")
                #raise forms.ValidationError(" Max date cannot be less than min date.") 

    helper = FormHelper()
    helper.layout = Layout(InlineCheckboxes('or_choose_which_author'))
    #helper.layout = Layout(Field('text_input', css_class='form-control-lg'))
        
    
    #def validate(self, value):
    #    """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
    #    super().validate(value)
    #    for email in value:
    #        validate_email(email)

class ExampleForm(forms.Form):
    
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            Fieldset(
                'first arg is the legend of the fieldset',
                'like_website',
                'favorite_number',
                'favorite_color',
                'favorite_food',
                'notes'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )       

class InputForm(forms.ModelForm):

    class Meta:
        model = Input
        fields = ('min_date', 'max_date',)