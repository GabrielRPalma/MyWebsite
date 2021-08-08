from django.urls import path
from. import views

app_name='curriculum'
urlpatterns = [
    path('modules/', views.StandardListView.as_view(), name = 'standard_list'),
    path('tutorial/', views.tutorial, name = 'tutorial'),
    path('<slug:slug>/', views.SubjectListView.as_view(), name = 'subject_list'),
    path('<str:standard>/<slug:slug>/', views.LessonListView.as_view(), name = 'lesson_list')
]