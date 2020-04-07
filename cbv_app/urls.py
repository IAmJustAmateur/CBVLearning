from django.contrib import admin
from django.urls import path, include
from cbv_app.views import SchoolListView

app_name = 'cbv_app'

urlpatterns = [
    path('', SchoolListView.as_view(), name = 'list'),
]
