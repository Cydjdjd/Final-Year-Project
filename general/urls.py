from django.urls import path
from general import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name='originalhome'),
    path("loginpageUser", views.normalLogin, name='loginpageuser'),
    path("loginpageContributor", views.contributorLogin, name='loginpagecontributor'),
    path("signuppageUser", views.NormalSignUpView.as_view(), name='signuppageuser'),
    path("signuppageContributor", views.ContributorSignUpView.as_view(), name='signuppagecontributor'),
    path("aboutPage",views.aboutPage,name="originalaboutPage"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)