from django.shortcuts import render
from django.http  import HttpResponse,Http404

# Create your views here.

# @login_required(login_url='/accounts/login/')
def index(request):
    business = Business.get_all()
    neighborhood = Neighborhood.get_all()
    post = Post.get_all()
    return render(request,'index.html',{'business':business,'neighborhood':neighborhood, 'post':post})
    
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