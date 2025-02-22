from django.urls import path
from website.views import contact_view, newsletter_view, index_view


app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('contact/', contact_view, name='contact'),
    path('newsletter/', newsletter_view, name='newsletter'),
]
