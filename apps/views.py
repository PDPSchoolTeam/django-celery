import logging
from apps.forms import FeedbackForm
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.tasks import send_feedback_email_task

logger = logging.getLogger(__name__)


def feedback_form_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")
            print(email)
            print(message)
            send_feedback_email_task.delay(email, message)

            messages.success(request, "Fikr-mulohazangiz yuborildi, rahmat!")  # noqa
            return redirect("success")
            # except Exception as e:
            #     logger.error(f"Feedback email yuborishda xatolik: {e}")  # noqa
            #     messages.error(request, "Xatolik yuz berdi. Iltimos, keyinroq urinib ko‘ring.")  # noqa
    else:
        form = FeedbackForm()

    return render(request, "feedback.html", {"form": form})


def success_view(request):
    return render(request, "success.html")
