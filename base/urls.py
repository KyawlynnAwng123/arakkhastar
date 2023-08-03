from django.urls import path
from .import views

urlpatterns = [
    path('',views.home_page_views,name="homepage"),
    path('about/',views.about_page_views,name="aboutpage"),
    path('contact/',views.contact_page_views,name="contactpage"),
    path('category/<slug:slug>/',views.each_categories_page_views,name='eachcategories_page'),
    path('category',views.eachcategories,name='eachpage'),

    path('detail/<slug:slug>/',views.post_detail_page_views,name="detail_page"),

    ]
