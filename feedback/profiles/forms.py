from django import forms


class ProfileForm(forms.Form):
    # This form has not been used because we are extending CreateView on the CreateProfileView
    user_image = forms.FileField()

    labels = {
        "user_image": "Your Image",
    }
