from django.urls import path

from urls.views import IndexView, RedirectView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<id>/", RedirectView.as_view(), name="url_by_id")
]