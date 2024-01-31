"""
URL configuration for libraryapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from books import views
from rest_framework.authtoken import views as rviews   #Module aliasing
from rest_framework.routers import DefaultRouter


router=DefaultRouter()  #this router is specially for viewset based views.
router.register('books',views.bookviewset) # when we run server it will show error because our site works withhttps:127.0.0.1.8000/books so that is mentioned here.

#for registration:
#router=DefaultRouter()
router.register('user',views.userviewset)

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('',views.booklist.as_view()),    #commenting paths for other class based views
   # path('book/<int:pk>',views.bookdetail.as_view()),  #commenting paths for other class based views
   # path('',include(router.urls)),   #providing connection to router which is provided for viewset based views
    path('',include(router.urls)), #for providing connection to router for registration based views
    path('api-token-auth/',rviews.obtain_auth_token), #for login(authentication)
]
