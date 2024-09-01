from django.urls import path
from user import views
from django.conf import settings

urlpatterns=[
    path("homepage", views.home, name='normalhome'),
    path("jobs",views.jobsPage,name="jobPage"),
    path("courses",views.coursePage,name="coursePage"),
    path("articles",views.articlesPage,name="articlesPage"),
    path("articleReadPage/<int:article_id>",views.articleReadPage,name="articleReadPage"),
    path("jobApplyPage/<int:job_id>",views.jobApplyPage,name="jobApplyPage"),
    path("jobApply/<int:job_id>",views.jobApply,name="jobApply"),
    path("courseApplyPage/<int:course_id>",views.courseApplyPage,name="courseApplyPage"),
    path("courseApply/<int:course_id>",views.courseApply,name="courseApply"),
    path("careerCoachingPage",views.careerCoachingPage,name="careerCoachingPage"),
    path("submitCareerCoaching",views.submitCareerCoaching,name="submitCareerCoaching"),
    path("aboutPage",views.aboutPage,name="aboutPage"),
    path("logout",views.logout_view,name="logout"),
    path("normalUserProfilePage",views.normalUserProfilePage,name="normalUserProfilePage"),
    path("updateNormalUserProfilePage",views.updateNormalUserProfilePage,name="updateNormalUserProfilePage"),
]