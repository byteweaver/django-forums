from django import forms


class TopicCreateForm(forms.Form):
    topic = forms.CharField(label="Topic", min_length=3)
    message = forms.CharField(label="Message", min_length=3, widget=forms.Textarea())


class PostCreateForm(forms.Form):
    message = forms.CharField(label="Message", min_length=3, widget=forms.Textarea())
