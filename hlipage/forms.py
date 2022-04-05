from django import forms
from .models import Input

from .scripts import investigators

choicelist = investigators.all_PIs_listofstr
clist = list(zip(choicelist,choicelist))

class InputQuery(forms.Form):
    #select_all_authors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[("1", "yes"),("2", "no")], required=False)
    or_choose_which_author = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=clist)
    min_date = forms.DateField()
    max_date = forms.DateField()

class InputForm(forms.ModelForm):

    class Meta:
        model = Input
        fields = ('min_date', 'max_date',)