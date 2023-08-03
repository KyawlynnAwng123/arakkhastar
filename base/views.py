from email import message
from multiprocessing import context
from unicodedata import category
from django.shortcuts import HttpResponse, render,redirect
from .models import *
import datetime
from .forms import ContactForm
from django.db.models import Q
from django.contrib import messages





# start home_page_views
def home_page_views(request):
    new_search=request.GET.get('search') if request.GET.get('search') !=None else ''
    heder_content_post=Post.objects.all()[0:1]
    categories=Category.objects.all()
    one_month_ago=datetime.date.today()-datetime.timedelta(30)
    top_views_post=Post.objects.filter(created__gte=one_month_ago).order_by('-views')[1:6]

    posts=Post.objects.filter(category__name__icontains=new_search)[1:4]
    eachcategories={categories:Post.objects.filter(category=categories)[:3] for categories in Category.objects.filter(name__icontains=new_search)}

    marquee_title = Post.objects.all()
    context={'posts':posts,
            'eachcategories':eachcategories,
            'heder_content_post':heder_content_post,
            'marquee_title': marquee_title,
            'categories':categories,
            'top_views_post':top_views_post
            }
    return render(request,'pages/index.html',context)
# end home_page_views



# start each_post_page_views

def each_categories_page_views(request,slug):
    new_search=request.GET.get('search') if request.GET.get('search') != None else ''
    all_categories=Category.objects.get(slug=slug)
    all_posts=all_categories.post_set.filter(category__name__icontains=new_search)
    categories=Category.objects.all()
    one_month_ago=datetime.date.today()-datetime.timedelta(30)
    top_views_post=Post.objects.filter(created__gte=one_month_ago).order_by('-views')[1:6]
    

    
    marquee_title = Post.objects.all()[0:5]
    context={
        'marquee_title':marquee_title,
        'all_posts':all_posts,
        'all_categories':all_categories,
        'categories':categories,
        'top_views_post':top_views_post
        }
    return render(request,'pages/each_post.html',context)
# end each_post_page_views


# start about_page_views
def about_page_views(request):
    about = About.objects.first()
    categories=Category.objects.all()

    
    context = {'about':about,'categories':categories}
    return render(request,'pages/about.html',context)
# end about_page_views


# start post_detail_page_views
def post_detail_page_views(request,slug):
    posts=Post.objects.get(slug=slug)
    posts.views=posts.views+1
    posts.save()
    category=Category.objects.get(slug=posts.category.slug)
    similar_posts=Post.objects.filter(category=category)
    categories=Category.objects.all()
    marquee_title = Post.objects.all()[0:5]
    context={'posts':posts,'similar_posts':similar_posts,'marquee_title':marquee_title,'categories':categories}
    return render(request,'pages/post_detail.html',context)
# end post_detail_page_views



# start contact_page_views
def contact_page_views(request):
    if request.method == 'POST':
        username=request.POST.get('name')
        useremail=request.POST.get('email')
        userphone=request.POST.get('phone')
        usersubject=request.POST.get('subject')
        usermesage=request.POST.get('userimage')
        user_obj=Contact(name=username,email=useremail,phone=userphone,subject=usersubject,Message=usermesage)
        user_obj.save()
        
        
        return redirect('homepage')
        
    else:
        categories=Category.objects.all()
        context={'categories':categories}
        messages.success(request, "Contact Successfully!")
        return render(request,'pages/contact.html',context)
    # end contact_page_views




# eachcategories_page_views
def eachcategories(request):
    eachcategories={cat:Post.objects.filter(category=cat)for cat in Category.objects.all()}
    categories=Category.objects.all()
   
  
    context={
        'eachcategories':eachcategories,
        'categories':categories,
       
        }
    return render(request,'pages/eachcategory.html',context)
# eachcategories_page_views



