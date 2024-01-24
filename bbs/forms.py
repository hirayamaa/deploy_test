from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class': 'for-control me-2',
    'placeholder': 'キーワードを入力', 'aria-label': 'Search'}))