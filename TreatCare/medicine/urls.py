from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.MedicineListView.as_view()),
]
