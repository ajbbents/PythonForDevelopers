from django import forms

CHART__CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

# define class-based Form imported from django forms


class SalesSearchForm(forms.Form):
    book_title = forms.CharField(max_length=120)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)
