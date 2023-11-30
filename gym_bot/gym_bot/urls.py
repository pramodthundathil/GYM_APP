
from django.contrib import admin
from django.urls import path,include
from Index import urls
import Index
import Members
from Members import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("Index.urls")),
    path("members/",include(Members.urls))
]
