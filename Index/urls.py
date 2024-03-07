from django.urls import path,include
from Index import views
app_name="index"
urlpatterns = [
    path('',views.index,name="index"),
]