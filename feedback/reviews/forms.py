from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(
#         label="Your Name",
#         required=True,
#         max_length=100,
#         error_messages={
#             "required":"Your name must not be empty!",
#             "max_length": "Please enter a shorter name"
#         }
#     )
#     review_text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=100)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__' # or user a list to select the fields ["user_name", "review_text"]
        # exclude = ["some_field"] this excludes one or more fields
        
        # customize the labels
        labels = {
            "user_name":"Your Name",
            "review_text":"Your Feedback",
            "rating":"Your Rating"
        }

        # customize error messages
        error_messages = {
            "user_name": {
                "required":"Your name must not be empty!",
                "max_length": "Please enter a shorter name"
            }
        }
