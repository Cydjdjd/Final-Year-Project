from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from general.decorators import normaluser_required
from contributor.models import Job,Course,Article,JobApplicationDetails,CourseApplicationDetails
from user.forms import jobApplyForm,courseApplyForm,careerCoachingForm,NormalUserProfilePageForm
from general.models import User,NormalUser,Contributor
from django.db import IntegrityError
from user.models import careerCoachingApplicationDetails
from general.models import NormalUser
# Create your views here.
@login_required(login_url="/loginpageUser")
@normaluser_required
def home(request):
    return render(request, "userhomepage.html", {})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url="/loginpageUser")
@normaluser_required
def jobsPage(request):
    jobs=Job.objects.all()
    jobsAppliedDetails=JobApplicationDetails.objects.filter(userApplied_id=NormalUser.objects.filter(user_id=request.user.id)[0].id)
    jobsNotApplied=jobs
    for jobApplied in jobsAppliedDetails:
        jobsNotApplied=jobsNotApplied.exclude(id=jobApplied.jobApplied_id)
    jobsApplied=jobs.exclude(id__in=jobsNotApplied)          
    return render(request, "userJobs.html", {'jobsApplied':jobsApplied,'jobsNotApplied':jobsNotApplied})

@login_required(login_url="/loginpageUser")
@normaluser_required
def coursePage(request):
    courses=Course.objects.all()
    coursesAppliedDetails=CourseApplicationDetails.objects.filter(userApplied_id=NormalUser.objects.filter(user_id=request.user.id)[0].id)
    coursesNotApplied=courses
    for courseApplied in coursesAppliedDetails:
        coursesNotApplied=coursesNotApplied.exclude(id=courseApplied.courseApplied_id)
    coursesApplied=courses.exclude(id__in=coursesNotApplied)
    return render(request, "userCourses.html", {'coursesApplied':coursesApplied,'coursesNotApplied':coursesNotApplied})

@login_required(login_url="/loginpageUser")
@normaluser_required
def articlesPage(request):
    articles=Article.objects.all()
    return render(request, "userArticle.html", {'articles':articles})

@login_required(login_url="/loginpageUser")
@normaluser_required
def jobApplyPage(request,job_id):
    form=jobApplyForm()
    job= Job.objects.filter(id=job_id)[0]
    user =request.user
    form.initial["jobTitle"]=job.jobTitle
    form.initial["companyName"]=job.companyName
    form.initial["userName"]=user.username
    form.initial["age"]=NormalUser.objects.filter(user_id=user.id)[0].age
    return render(request, "jobApplyPage.html",{'form':form,'job_id':job_id})

@login_required(login_url="/loginpageUser")
@normaluser_required
def jobApply(request,job_id):
    if request.method == 'POST':
        job= Job.objects.filter(id=job_id)[0]
        form = jobApplyForm(request.POST,request.FILES)
        try:
            if form.is_valid():
                jobApplication=JobApplicationDetails()
                jobApplication.userApplied=NormalUser.objects.filter(user_id=request.user.id)[0]
                jobApplication.jobApplied=job
                jobApplication.jobTitle=form.cleaned_data['jobTitle']
                jobApplication.companyName=form.cleaned_data['companyName']
                jobApplication.userName=form.cleaned_data['userName']
                jobApplication.realName=form.cleaned_data['realName']
                jobApplication.age=form.cleaned_data['age']
                jobApplication.resume=form.cleaned_data['resume']
                jobApplication.save()
                return redirect("/user/jobs")
        except IntegrityError as e:
            return redirect("/user/jobs")

@login_required(login_url="/loginpageUser")
@normaluser_required
def courseApplyPage(request,course_id):
    form=courseApplyForm()
    course= Course.objects.filter(id=course_id)[0]
    user =request.user
    form.initial["courseTitle"]=course.courseTitle
    form.initial["companyName"]=course.companyName
    form.initial["userName"]=user.username
    form.initial["age"]=NormalUser.objects.filter(user_id=user.id)[0].age
    return render(request, "courseApplyPage.html",{'form':form,'course_id':course_id})

@login_required(login_url="/loginpageUser")
@normaluser_required
def courseApply(request,course_id):
    if request.method == 'POST':
        course= Course.objects.filter(id=course_id)[0]
        form = courseApplyForm(request.POST,request.FILES)
        try:
            if form.is_valid():
                courseApplication=CourseApplicationDetails()
                courseApplication.userApplied=NormalUser.objects.filter(user_id=request.user.id)[0]
                courseApplication.courseApplied=course
                courseApplication.courseTitle=form.cleaned_data['courseTitle']
                courseApplication.companyName=form.cleaned_data['companyName']
                courseApplication.userName=form.cleaned_data['userName']
                courseApplication.realName=form.cleaned_data['realName']
                courseApplication.age=form.cleaned_data['age']
                courseApplication.startDate=form.cleaned_data['startDate']
                courseApplication.save()
                return redirect("/user/courses")
        except IntegrityError as e:
            return redirect("/user/courses")
        
@login_required(login_url="/loginpageUser")
@normaluser_required
def articleReadPage(request,article_id):
    article=Article.objects.filter(id=article_id)[0]
    return render(request, "userArticleReadPage.html", {'article':article})

@login_required(login_url="/loginpageUser")
@normaluser_required
def careerCoachingPage(request):
    form=careerCoachingForm()
    if(careerCoachingApplicationDetails.objects.filter(normalUserApplied_id=NormalUser.objects.filter(user_id=request.user.id)[0].id)):
        applicationDetails=careerCoachingApplicationDetails.objects.filter(normalUserApplied_id=NormalUser.objects.filter(user_id=request.user.id)[0].id)[0]
    else:
        applicationDetails=None
    return render(request, "careerCoachingPage.html", {'form':form,'applicationDetails':applicationDetails})

@login_required(login_url="/loginpageUser")
@normaluser_required
def submitCareerCoaching(request):
    if request.method == 'POST':
        form=careerCoachingForm(request.POST)
        if form.is_valid():
            obj=careerCoachingApplicationDetails()
            obj.realName=form.cleaned_data['realName']
            obj.emailAddress=form.cleaned_data['emailAddress']
            obj.contactNumber=form.cleaned_data['contactNumber']
            obj.normalUserApplied=NormalUser.objects.filter(id=NormalUser.objects.filter(user_id=request.user.id)[0].id)[0]
            obj.save()
            return redirect('/user/careerCoachingPage')

@login_required(login_url="/loginpageUser")
@normaluser_required
def aboutPage(request):
    return render(request, "userAboutPage.html")

@login_required(login_url="/loginpageUser")
@normaluser_required
def normalUserProfilePage(request):
    form = NormalUserProfilePageForm()
    form.initial["username"]=request.user.username
    form.initial["password"]=request.user.password
    form.initial["age"]=NormalUser.objects.get(user_id=request.user.id).age
    form.initial["ic"]=NormalUser.objects.get(user_id=request.user.id).ic
    return render(request,"userProfilePage.html",{'form':form})
@login_required(login_url="/loginpageUser")
@normaluser_required
def updateNormalUserProfilePage(request):
    form = NormalUserProfilePageForm(request.POST, request.FILES,instance=request.user)
    if form.is_valid():
        user = User.objects.get(id=request.user.id)
        user.username=form.cleaned_data["username"]
        user.set_password(form.cleaned_data["password"])  # replace with your real password
        user.save()
        normalUser=NormalUser.objects.get(user_id=request.user.id)
        normalUser.age=form.cleaned_data["age"]
        normalUser.ic=form.cleaned_data["ic"]
        normalUser.save()
        login(request, user)
        return redirect("/user/homepage")