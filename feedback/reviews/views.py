from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView

# Class based view
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/index.html", {
            "form": form
        })
    
    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "reviews/thank_you.html")
        
        # render the form with the error messages if the form is not valid
        return render(request, "reviews/index.html", {
            "form": form
        })

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    # add or manipulate data sent to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context
    
class ReviewsListView(TemplateView):
    model = Review
    template_name = "reviews/reviews_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context

# Function based views
# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             # print(form.cleaned_data)
#             # review = Review(
#             #     user_name = form.cleaned_data['user_name'],
#             #     review_text = form.cleaned_data['review_text'],
#             #     rating = form.cleaned_data['rating']
#             # )
#             form.save()
#             return render(request, "reviews/thank_you.html")
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/index.html", {
#         "form": form
#     })

# def thank_you(request):
    # return render(request, "reviews/thank_you.html")
