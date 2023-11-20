from django.urls import path, include

from .views.course import init_course, CourseView
from .views.exam import create_and_test
from .views.government import GovernmentView
from .views.hello import HelloView
from .views.student import add_student, query_student_score_history
from .views.test import TestView, test
from .views.school import add_random_school, show_all_school
from .views.pages import index

urlpatterns = [
    path("", HelloView.as_view()),
    path('hello/', HelloView.as_view()),
    path('government/', GovernmentView.as_view()),
    path('test/', TestView.as_view()),
    path('test-func/', test),
    path('add-random-school/', add_random_school),
    path('show-all-school/', show_all_school),
    path('add-student/', add_student),
    path('query-student-score-history/', query_student_score_history),

    path('init-course/', init_course),
    path('course/', CourseView.as_view()),
    path('new-random-exam/', create_and_test),
    # page
    path('index/', index)
]
