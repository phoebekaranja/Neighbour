from django.shortcuts import render
from django.http  import HttpResponse,Http404

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    business = Business.get_all()
    neighborhood = Neighborhood.get_all()
    post = Post.get_all()
    return render(request,'index.html',{'business':business,'neighborhood':neighborhood, 'post':post})