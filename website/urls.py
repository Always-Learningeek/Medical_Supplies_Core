from django.urls import path
from website.views import contact_view, newsletter_view, index_view, about_view, coming_soon_view
from blog.views import blog_view, blog_single


app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('contact/', contact_view, name='contact'),
    path('newsletter/', newsletter_view, name='newsletter'),
    path('about/', about_view, name='about'),
    path('<int:pid>', blog_single, name='blog-single'),
    path('category/<str:cat_name>', blog_view, name='website-category'),
    path('coming-soon/', coming_soon_view, name='coming-soon'),

]
