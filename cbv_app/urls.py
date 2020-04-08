from django.contrib import admin
from django.urls import path, include
from cbv_app.views import (SchoolListView, SchoolDetailView,
                            SchoolCreateView)

app_name = 'cbv_app'

urlpatterns = [
    path('', SchoolListView.as_view(), name = 'list'),
    path('<int:pk>/',SchoolDetailView.as_view(), name='detail'),
    path('create/', SchoolCreateView.as_view(), name='create'),
]
