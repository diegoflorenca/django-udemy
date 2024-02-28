from django import forms


class ProfileForm(forms.Form):
    user_image = forms.FileField()

    labels = {
        "user_image": "Your Image",
    }
