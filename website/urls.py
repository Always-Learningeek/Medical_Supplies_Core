from django.urls import path
from website.views import contact_view, newsletter_view


app_name = 'website'

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('newsletter/', newsletter_view, name='newsletter'),
]
