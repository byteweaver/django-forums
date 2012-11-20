from django import forms


class TopicCreateForm(forms.Form):
    topic = forms.CharField("Topic", min_length=3, widget=forms.TextInput(attrs={'class': 'input-xxlarge'}))
    message = forms.CharField("Message", min_length=3, widget=forms.Textarea(attrs={'class': 'input-xxlarge'}))

class PostCreateForm(forms.Form):
    message = forms.CharField("Message", min_length=3, widget=forms.Textarea(attrs={'class': 'input-xxlarge'}))
