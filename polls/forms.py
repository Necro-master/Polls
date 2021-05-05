from django import forms

class TextForm(forms.Form):
    ans = forms.CharField(max_length=4096)
    def __init__(self, label, name):
        super().__init__()
        self.fields['ans'].label = label
        self.fields[name] = self.fields.pop('ans')

class MultipleForm(forms.Form):
    ans = forms.MultipleChoiceField(choices=((0, 'YES'), (1, 'NO')), widget=forms.CheckboxSelectMultiple)
    def __init__(self, choices, label, name):
        super().__init__()
        self.fields['ans'].choices = choices
        self.fields['ans'].label = label
        self.fields[name] = self.fields.pop('ans')

class SingleForm(forms.Form):
    ans = forms.ChoiceField(choices=((0, 'YES'), (1, 'NO')), widget=forms.RadioSelect)
    def __init__(self, choices, label, name):
        super().__init__()
        self.fields['ans'].choices = choices
        self.fields['ans'].label = label
        self.fields[name] = self.fields.pop('ans')

