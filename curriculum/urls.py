from django.urls import path

from .views import *

app_name = 'curriculum'

urlpatterns = [
	path('', StandardListView.as_view(), name='standard_list'),
	path('<slug:slug>/', SubjectListView.as_view(), name='subject_list'),
	path('<str:standard>/<slug:slug>/', LessonListView.as_view(), name='lesson_list'),

	path('<str:standard>/<slug:slug>/create/', LessonCreateView.as_view(), name='lesson_create'),

	path('<str:standard>/<str:subject>/<slug:slug>/', LessonDetailView.as_view(), name='lesson_detail'),

	path('<str:standard>/<str:subject>/<slug:slug>/update/', LessonUpdateView.as_view(), name='lesson_update'),
	path('<str:standard>/<str:subject>/<slug:slug>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),

]