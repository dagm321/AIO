from django.urls import path
from django.conf import Settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('first/', views.first, name='first'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name='sell'),
    path('profile/', views.profile, name='profile'),
    path('viewprofile/', views.viewprofile, name='viewprofile'),
    path('viewbuy/', views.viewbuy, name='viewbuy'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('message/', views.message, name='message'),
    path('popups/', views.popups, name='popups'),
]

# if Settings.DEBUG:
#     urlpatterns += static(Settings.MEDIA_URL,document_root=Settings.MEDIA_ROOT)