from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'indexPage'),
    url('^homepost',views.homepost,name = 'homepost'),
    url('^homebusiness',views.homebusiness,name = 'homebusiness'),
    url('^homeneighborhood',views.homeneighborhood,name = 'homeneighborhood'),
    url('^homehealth',views.homehealth,name = 'homehealth'),
    url(r'^homepolice', views.homepolice, name='homepolice'),
    url(r'^post/(\d+)',views.post,name ='post'),
    url(r'^neighborhood/(\d+)',views.neighborhood,name ='neighborhood'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^new/health$', views.new_health, name='new-health'),
    url(r'^new/business$', views.new_business, name='new-business'),
    url(r'^search/', views.search, name='search'),
    url(r'^search-details/(\d+)',views.search_details,name = 'search-details'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
