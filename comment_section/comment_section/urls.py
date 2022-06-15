"""comment_section URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from page.views import homepage, login_request, logout_request, register_request, PodcastList, PodcastComments, Account, AddPodcast, delete_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('podcasty/', PodcastList.as_view(), name='podcasty'),
    path('podcasty/<int:podcast_id>', PodcastComments.as_view(), name='komentarze'),
    path('dodaj_podcast/',  AddPodcast.as_view(), name='dodaj podcast'),
    path('account', Account.as_view(), name='konto'),
    path('delete/<int:comment_id>', delete_comment, name='usuń komentarz'),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),
]
