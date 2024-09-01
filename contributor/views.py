from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from general.decorators import contributor_required
from general.models import User,Contributor,NormalUser
from contributor.forms import jobsCreate,courseCreate,articleCreate,ContributorProfilePageForm
from contributor.models import Job,Course,Article,JobApplicationDetails,CourseApplicationDetails
from django.contrib.auth import login,authenticate
# Create your views here.
@login_required(login_url="/loginpageContributor")
@contributor_required
def home(request):
    return render(request, "contributorhomepage.html", {})

@login_required(login_url="/loginpageContributor")
@contributor_required
def createhistorypage(request):
    print(Contributor.objects.filter(user_id=request.user.id))
    jobs=Job.objects.filter(contributor_id=Contributor.objects.filter(user_id=request.user.id)[0].id)
    return render(request, "contributorcreatehistory.html", {"jobs":jobs})

@login_required(login_url="/loginpageContributor")
@contributor_required
def createhistorypage2(request):
    courses=Course.objects.filter(contributor_id=Contributor.objects.filter(user_id=request.user.id)[0].id)
    return render(request, "contributorcreatehistory2.html", {"courses":courses})

@login_required(login_url="/loginpageContributor")
@contributor_required
def createhistorypage3(request):
    articles=Article.objects.filter(contributor_id=Contributor.objects.filter(user_id=request.user.id)[0].id)
    return render(request, "contributorcreatehistory3.html", {"articles":articles})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url="/loginpageContributor")
@contributor_required
def createpage1(request):
    form=jobsCreate()
    return render(request, "contributorcreatepage1.html", {'form':form})

@login_required(login_url="/loginpageContributor")
@contributor_required
def createpage2(request):
    form=courseCreate()
    return render(request, "contributorcreatepage2.html", {'form':form})

@login_required(login_url="/loginpageContributor")
@contributor_required
def createpage3(request):
    form=articleCreate()
    return render(request, "contributorcreatepage3.html", {'form':form})
@login_required(login_url="/loginpageContributor")
@contributor_required
def create1(request):
    if request.method == 'POST':
        form = jobsCreate(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            # process form data
            obj = Job() #gets new object
            obj.companyPicture = form.cleaned_data['companyPicture']
            obj.jobTitle = form.cleaned_data['jobTitle']
            obj.companyName = form.cleaned_data['companyName']
            obj.jobSalary=form.cleaned_data['jobSalary']
            obj.jobDescription = form.cleaned_data['jobDescription']
            obj.contributor=Contributor.objects.get(user_id=request.user.id)
            #finally save the object in db
            obj.save()
            return redirect("../contributor/createPage1")
        else:
            print(form.errors.as_data())
@login_required(login_url="/loginpageContributor")
@contributor_required
def create2(request):
    if request.method == 'POST':
        form = courseCreate(request.POST)
        if form.is_valid():
            # process form data
            obj = Course() #gets new object
            obj.courseTitle = form.cleaned_data['courseTitle']
            obj.companyName = form.cleaned_data['companyName']
            obj.courseDescription = form.cleaned_data['courseDescription']
            obj.contributor=Contributor.objects.get(user_id=request.user.id)
            #finally save the object in db
            obj.save()
            return redirect("../contributor/createPage2")
        else:
            print(form.errors.as_data())
@login_required(login_url="/loginpageContributor")
@contributor_required        
def create3(request):
    if request.method == 'POST':
        form = articleCreate(request.POST)
        if form.is_valid():
            # process form data
            obj = Article() #gets new object
            obj.articleTitle = form.cleaned_data['articleTitle']
            obj.articleDescription = form.cleaned_data['articleDescription']
            obj.contributor=Contributor.objects.get(user_id=request.user.id)
            #finally save the object in db
            obj.save()
            return redirect("/contributor/createPage3")
        
@login_required(login_url="/loginpageContributor")
@contributor_required
def editpage1(request,job_id):
    form=jobsCreate()
    job=Job.objects.filter(id=job_id)[0]
    form.initial["companyPicture"]=job.companyPicture
    form.initial["jobTitle"]=job.jobTitle
    form.initial["companyName"]=job.companyName
    form.initial["jobSalary"]=job.jobSalary
    form.initial["jobDescription"]=job.jobDescription
    
    return render(request, "contributoreditpage1.html", {'form':form,'job':job,'job_id':job_id})

@login_required(login_url="/loginpageContributor")
@contributor_required
def editpage2(request,course_id):
    form=courseCreate()
    course=Course.objects.filter(id=course_id)[0]
    form.initial["courseTitle"]=course.courseTitle
    form.initial["companyName"]=course.companyName
    form.initial["courseDescription"]=course.courseDescription
    
    return render(request, "contributoreditpage2.html", {'form':form,'course':course,'course_id':course_id})

@login_required(login_url="/loginpageContributor")
@contributor_required
def editpage3(request,article_id):
    form=articleCreate()
    article=Article.objects.filter(id=article_id)[0]
    form.initial["articleTitle"]=article.articleTitle
    form.initial["articleDescription"]=article.articleDescription   
    return render(request, "contributoreditpage3.html", {'form':form,'article':article,'article_id':article_id})
@login_required(login_url="/loginpageContributor")
@contributor_required
def edit1(request,job_id):
    if request.method == 'POST':
        form = jobsCreate(request.POST,request.FILES)
        if form.is_valid():
            obj=Job.objects.get(id=job_id)
            obj.companyPicture = form.cleaned_data['companyPicture']
            obj.jobTitle = form.cleaned_data['jobTitle']
            obj.companyName = form.cleaned_data['companyName']
            obj.jobSalary=form.cleaned_data['jobSalary']
            obj.jobDescription = form.cleaned_data['jobDescription']
            obj.contributor=Contributor.objects.get(user_id=request.user.id)
            obj.save()
            return redirect("../../contributor/createhistorypage")
        else:
            print(form.errors.as_data())

@login_required(login_url="/loginpageContributor")
@contributor_required
def edit2(request,course_id):
    if request.method == 'POST':
        form = courseCreate(request.POST)
        if form.is_valid():
            obj=Course.objects.get(id=course_id)
            obj.courseTitle = form.cleaned_data['courseTitle']
            obj.companyName = form.cleaned_data['companyName']
            obj.courseDescription = form.cleaned_data['courseDescription']
            obj.contributor=Contributor.objects.get(user_id=request.user.id)
            obj.save()
            return redirect("../../contributor/createhistorypage2")
        else:
            print(form.errors.as_data())

@login_required(login_url="/loginpageContributor")
@contributor_required
def edit3(request,article_id):
    if request.method == 'POST':
        form = articleCreate(request.POST)
        if form.is_valid():
            obj=Article.objects.get(id=article_id)
            obj.articleTitle=form.cleaned_data['articleTitle']
            obj.articleDescription = form.cleaned_data['articleDescription']
            obj.contributor=Contributor.objects.get(user_id=request.user.id)
            obj.save()
            return redirect("../../contributor/createhistorypage3")
        else:
            print(form.errors.as_data())

@login_required(login_url="/loginpageContributor")
@contributor_required
def jobApplicationDetail(request,job_id):
    jobApplicationDetails=JobApplicationDetails.objects.filter(jobApplied_id=job_id)
    job=Job.objects.filter(id=job_id)[0]
    return render(request,"jobApplicationDetails.html",{'jobApplicationDetails':jobApplicationDetails,'job':job})
    
@login_required(login_url="/loginpageContributor")
@contributor_required
def courseApplicationDetail(request,course_id):
    courseApplicationDetails=CourseApplicationDetails.objects.filter(courseApplied_id=course_id)
    course=Course.objects.filter(id=course_id)[0]
    return render(request,"courseApplicationDetails.html",{'courseApplicationDetails':courseApplicationDetails,'course':course})

@login_required(login_url="/loginpageContributor")
@contributor_required
def contributorProfilePage(request):
    form = ContributorProfilePageForm()
    form.initial["username"]=request.user.username
    form.initial["password"]=request.user.password
    return render(request,"contributorProfilePage.html",{'form':form})

@login_required(login_url="/loginpageContributor")
@contributor_required
def updateContributorProfilePage(request):
    form = ContributorProfilePageForm(request.POST, instance=request.user)
    if form.is_valid():
        user = User.objects.get(id=request.user.id)
        user.username=form.cleaned_data["username"]
        user.set_password(form.cleaned_data["password"])  # replace with your real password
        user.save()
        login(request, user)
        return redirect("/contributor/homepage")
        
    
