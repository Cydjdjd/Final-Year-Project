from django.urls import path
from contributor import views
from django.conf import settings

urlpatterns=[
    path("homepage", views.home, name='home'),
    path("logout",views.logout_view,name="logout"),
    path("createhistorypage", views.createhistorypage, name='createhistorypage'),
    path("createhistorypage2", views.createhistorypage2, name='createhistorypage2'),
    path("createhistorypage3", views.createhistorypage3, name='createhistorypage3'),
    path("createPage1",views.createpage1,name="createpage1"),
    path("createPage2",views.createpage2,name="createpage2"),
    path("createPage3",views.createpage3,name="createpage3"),
    path("create1",views.create1,name="create1"),
    path("create2",views.create2,name="create2"),
    path("create3",views.create3,name="create3"),
    path("editPage1/<int:job_id>",views.editpage1,name="editpage1"),
    path("edit1/<int:job_id>",views.edit1,name="edit1"),
    path("editPage2/<int:course_id>",views.editpage2,name="editpage2"),
    path("edit2/<int:course_id>",views.edit2,name="edit2"),
    path("editPage3/<int:article_id>",views.editpage3,name="editpage3"),
    path("edit3/<int:article_id>",views.edit3,name="edit3"),
    path("jobApplicationDetail/<int:job_id>",views.jobApplicationDetail,name="jobApplicationDetail"),
    path("courseApplicationDetail/<int:course_id>",views.courseApplicationDetail,name="courseApplicationDetail"),
    path("contributorProfilePage",views.contributorProfilePage,name="contributorProfilePage"),
    path("updateContributorProfilePage",views.updateContributorProfilePage,name="updateContributorProfilePage"),
]