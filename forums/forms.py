from django import forms


class TopicCreateForm(forms.Form):
    topic = forms.CharField("Topic", min_length=3)
    message = forms.CharField("Message", min_length=3, widget=forms.Textarea())


class PostCreateForm(forms.Form):
    message = forms.CharField("Message", min_length=3, widget=forms.Textarea())
