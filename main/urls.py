from django.urls import path, include

from .views.asyncTest import AsyncView
from .views.course import CourseView, CourseInitView
from .views.exam import CreateExamTestView
from .views.government import GovernmentView
from .views.hello import HelloView
from .views.student import query_student_score_history, StudentView
from .views.test import TestView, test
from .views.school import SchoolView
from .views.pages import IndexView

urlpatterns = [
    # path("", HelloView.as_view()),
    path('hello/<int:pk>/', HelloView.as_view()),

    path('government/', GovernmentView.as_view()),
    path('test/', TestView.as_view()),
    path('test-func/', test),
    path('school/', SchoolView.as_view()),
    path('student/', StudentView.as_view()),
    path('query-student-score-history/', query_student_score_history),

    path('init-course/', CourseInitView.as_view()),
    path('course/', CourseView.as_view()),
    path('new-random-exam/', CreateExamTestView.as_view()),

    path('async/', AsyncView.as_view()),

    # page
    path('index/', IndexView.as_view())
]
