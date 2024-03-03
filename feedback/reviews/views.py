from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse

# Class based view
# Using CreateVie as oppose to FormView


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/index.html"
    success_url = "/thank-you"

# Using FormView as oppose to View
# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/index.html"
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()

#         return render(request, "reviews/index.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return render(request, "reviews/thank_you.html")

#         # render the form with the error messages if the form is not valid
#         return render(request, "reviews/index.html", {
#             "form": form
#         })

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    # add or manipulate data sent to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context

# Using ListView as oppose to TemplateView


class ReviewsListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review
    context_object_name = "reviews"

    # Narrow down the data exported to the template
    # def get_queryset(self):
    #     base_query =  super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data

# class ReviewsListView(TemplateView):
#     template_name = "reviews/reviews_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

# Using DetailView as oppose to TemplateView


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        favorite_review = self.request.session.get("favorite_review")
        context["is_favorite"] = favorite_review == str(loaded_review.id)
        return context

# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context

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


class AddFavoriteReviewView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        # fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect(reverse("single-review", args=[review_id]))
