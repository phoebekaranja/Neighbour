from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 500)
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.name


    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    def update_neighborhood(self,location):
        self.location = location
        self.save()

    def update_neighborhood(self,count):
        self.count = count
        self.save()

    @classmethod
    def get_all(cls):
        neighborhood = cls.objects.all()
        return neighborhood

    @classmethod
    def get_neighborhood(cls, neighborhood_id):
        neighborhood = cls.objects.get(id=neighborhood_id)
        return neighborhood
class Profile(models.Model):
    user=models.ForeignKey(User,null=True)
    photo = models.ImageField(upload_to = 'profile/')
    bio = models.TextField(max_length = 100)
    contact = models.IntegerField(null=True)



    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Business(models.Model):
    business_image = models.ImageField(upload_to = 'business/', null=True)
    business_name = models.CharField(max_length = 50)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE, null=True)
    business_email = models.EmailField()


    def __str__(self):
        return self.business_name

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self,business_name):
        self.business_name = business_name
        self.save()

    @classmethod
    def get_all(cls):
        business = cls.objects.all()
        return business

    @classmethod
    def get_business(cls, business_id):
        business = cls.objects.get(id=business_id)
        return business

    @classmethod
    def search_by_title(cls,search_term):
        business = cls.objects.filter(business_name__icontains=search_term)
        return business

class Post(models.Model):
    post_image = models.ImageField(upload_to = 'post/', null=True)
    title = models.CharField(max_length = 50, null = True)
    description = models.TextField(max_length = 500,null=True)
    writer= models.ForeignKey(User,on_delete=models.CASCADE,null = True)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_all(cls):
        post = cls.objects.all()
        return post

    @classmethod
    def get_post(cls, post_id):
        post = cls.objects.get(id=post_id)
        return post

class Health(models.Model):
    contact_name = models.CharField(max_length=30)
    contacts = models.PositiveIntegerField()
    hospital = models.CharField(max_length = 50)
    neighborhood_contact = models.ForeignKey(Neighborhood, null= True,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.contact_name}'

    def save_health(self):
        self.save()

    def delete_health(self):
        self.delete()

    @classmethod
    def get_all(cls):
        health = cls.objects.all()
        return health

class Police(models.Model):
    Station = models.CharField(max_length=30)
    contacts = models.PositiveIntegerField()
    neighborhood_contact = models.ForeignKey(Neighborhood, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Station}'

    def save_police(self):
        self.save()

    def delete_police(self):
        self.delete()

    @classmethod
    def get_all(cls):
        police = cls.objects.all()
        return police