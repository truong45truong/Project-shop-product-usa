from django.urls import path,include 
from .views import NewViewSet

new = NewViewSet.as_view({
    'get' : 'get_new'
})

urlpatterns = [
    path('new/',new , name ="get_new")
]

