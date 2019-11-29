from django.urls import path
from author import views
app_name = 'author'

urlpatterns = [
    path('first_name_field-last_name_field', views.author, name='add_author'),
    path('', views.author_details, name='authors'),
    path('<int:id>', views.author_display, name='author_display'),
    path('contact_page', views.contact_page, name='contact_page'),
]