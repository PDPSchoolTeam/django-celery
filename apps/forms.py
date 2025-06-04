from django import forms


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Sizning email", required=True)  # noqa
    message = forms.CharField(label="Xabar", widget=forms.Textarea, required=True)  # noqa
