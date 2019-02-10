from django.conf.urls import url,include
from .views import stud

urlpatterns = [

    url(r'^student/',stud),   # function based views

]