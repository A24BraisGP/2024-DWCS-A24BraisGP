"""
URL configuration for feedback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # path('',views.ReviewView.as_view()),
    # path('thank_you',views.ThankYouView.as_view()),
    # path('review_list',views.ReviewListView.as_view()),
    # path('single_review/<int:pk>',views.SingleReviewView.as_view(), name="single_review"),
    path('',views.StudentView.as_view()),
    path('student_list',views.StudentList.as_view(), name="student-list"),
    path('single_student/<int:pk>',views.SingleStudentView.as_view(), name="single_student"),
    path('student/<int:pk>/update/',views.StudentUpdateView.as_view(), 
    name='update'),
    path('student/<int:pk>/delete',views.StudentDeleteView.as_view(), name='delete'),
    
]
