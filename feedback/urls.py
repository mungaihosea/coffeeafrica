from django.urls import path
from .views import CreateEscalation, CreateRawFeedBack

app_name = "feedback"

urlpatterns = [
    path("", CreateRawFeedBack.as_view(), name="createfeedback"),
    path(
        "<int:order_id>/", CreateEscalation.as_view(), name="createescalation"
    ),
]
