from django.urls import path, include

from .views.course import CourseView, CourseInitView
from .views.exam import CreateExamTestView
from .views.government import GovernmentView
from .views.hello import HelloView
from .views.student import add_student, query_student_score_history
from .views.test import TestView, test
from .views.school import add_random_school, SchoolView
from .views.pages import index

urlpatterns = [
    # path("", HelloView.as_view()),
    path('hello/<int:pk>/', HelloView.as_view()),

    path('government/', GovernmentView.as_view()),
    path('test/', TestView.as_view()),
    path('test-func/', test),
    path('add-random-school/', add_random_school),
    path('show-all-school/', SchoolView.as_view()),
    path('add-student/', add_student),
    path('query-student-score-history/', query_student_score_history),

    path('init-course/', CourseInitView.as_view()),
    path('course/', CourseView.as_view()),
    path('new-random-exam/', CreateExamTestView.as_view()),

    # page
    path('index/', index)
]
