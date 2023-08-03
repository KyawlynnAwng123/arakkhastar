from email.policy import default
from django.contrib.auth.models import User
import uuid
from django.db import models
from django.utils.text import slugify
import string
from django.utils.crypto import get_random_string
# Category Model

def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + get_random_string(length=4)
    return unique_slug
    
# start category model
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
            default='',
            editable=False,
            unique=True,blank=True,null=True
        )
    order = models.IntegerField(blank=True,null=True)    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.name))
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = ("categories")
        verbose_name_plural = ("categories")

    class Meta:
        ordering=['-order']

    def __str__(self):
        return self.name
# end category model


# start  Tag Model
class Tag(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(blank=True,null=True)    

    class Meta:
        verbose_name = ("tags")
        verbose_name_plural = ("tags")

    def __str__(self):
        return self.name
# end  Tag Model


# start About Model
class About(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to = 'static/%Y/%m/%d/about', blank= True,null=True,default='static/assets/img/hero-bg.jpg')

    class Meta:
        verbose_name = ("About")
        verbose_name_plural = ("Abouts")

    def __str__(self):
        return self.title
# end About Model


# start Contact Model
class Contact(models.Model):
    name=models.CharField(max_length=255,null=True)
    email=models.EmailField(null=True)
    phone = models.IntegerField()
    subject= models.CharField(max_length=255,null=True)
    Message= models.TextField(max_length=255,null=True)
    

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.name
# end Contact Model




# start Social Model 
class Social(models.Model):
    name = models.CharField(max_length=255)
    # icon = models.ImageField()
    link = models.CharField(max_length=255)
    

    class Meta:
        verbose_name = ("Social")
        verbose_name_plural = ("Socials")

    def __str__(self):
        return self.name
# end Social Model 


# start Message Model
class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    

    class Meta:
        verbose_name = ("Message")
        verbose_name_plural = ("Messages")

    def __str__(self):
        return self.name
# end Message Model



# start Post Model
class Post(models.Model):
    title = models.CharField(max_length= 255)
    slug = models.SlugField(
            default='',
            editable=False,
            unique=True,blank=True,null=True
        )
    short_content = models.TextField()
    long_content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='Arakkhastar')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='Admin')
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to = 'static/%Y/%m/%d/post-images', blank= True,null=True,default='static/assets/img/hero-bg.jpg')
    show_image = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated = models.DateTimeField(auto_now=True,blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.title))
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
        
    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.title
   

    # def get_absolute_url(self):
    #     return reverse("Post_detail", kwargs={"pk": self.pk})

# end Post Model

