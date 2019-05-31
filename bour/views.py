from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required(login_url='/accounts/login/')
def index(request):
    business = Business.get_all()
    neighborhood = Neighborhood.get_all()
    post = Post.get_all()
    return render(request,'index.html',{'business':business,'neighborhood':neighborhood, 'post':post})

@login_required(login_url='/accounts/login/')
def homepost(request):
    post = Post.get_all()
    return render(request,'homepost.html',{'post':post})

@login_required(login_url='/accounts/login/')
def homebusiness(request):
    business = Business.get_all()
    return render(request,'homebusiness.html',{'business':business})

@login_required(login_url='/accounts/login/')
def homeneighborhood(request):
    neighborhood = Neighborhood.get_all()
    return render(request,'homeneighborhood.html',{'neighborhood':neighborhood,})

@login_required(login_url='/accounts/login/')
def homehealth(request):
    health = Health.objects.all()
    return render(request,'homehealth.html',{'health':health,})

@login_required(login_url='/accounts/login/')
def homepolice(request):
    police = Police.get_all()
    return render(request,'homepolice.html',{'police':police,})

def post(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"post.html", {"post":post})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = current_user
            post.save()
        return redirect('indexPage')

    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            # business.user = current_user
            business.save()
        return redirect('indexPage')

    else:
        form = BusinessForm()
    return render(request, 'new_business.html', {"form": form})


def neighborhood(request,neighborhood_id):
    try:
        neighborhood = Neighborhood.objects.get(id = neighborhood_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"neighborhood.html", {"neighborhood":neighborhood})

def search(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def search_details(request,business_id):
    try :
        business = Business.objects.get(id = business_id)

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'search_details.html', {'business':business})

@login_required(login_url='/accounts/login/')
def new_health(request):
    current_user = request.user
    if request.method == 'POST':
        form = HealthForm(request.POST, request.FILES)
        if form.is_valid():
            health = form.save(commit=False)
            health.user = current_user
            health.save()
        return redirect('indexPage')

    else:
        form = HealthForm()
    return render(request, 'new_health.html', {"form": form})