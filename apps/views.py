from django.shortcuts import render, redirect
from apps.forms import FeedbackForm


def feedback_form_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect("/success/")
    else:
        form = FeedbackForm()

    return render(request, "feedback.html", {"form": form})


def success_view(request):
    return render(request, "success.html")
