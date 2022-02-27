from django.urls import path
from .views import QueryListingView


app_name = "query"
urlpatterns = [
    path('', QueryListingView.as_view(), name="index")
]
