from django.contrib import admin
from django.urls import path
from events import views as event_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', event_views.landing_page, name='landing_page'),
    path('register/', event_views.register, name='register'),
    path('login/', event_views.user_login, name='login'),
    path('logout/', event_views.user_logout, name='logout'),
    path('events/', event_views.event_list, name='event_list'),
    path('events/<int:event_id>/', event_views.event_detail, name='event_detail'),
    path('events/<int:event_id>/register/', event_views.event_register, name='event_register'),
    path('my_registrations/', event_views.my_registrations, name='my_registrations'),
    path('events/unregister/<int:registration_id>/', event_views.event_unregister, name='event_unregister'),
]
