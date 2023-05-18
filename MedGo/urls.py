from django.urls import path

from .import views 

urlpatterns = [

    path('',views.index,name="index"),

    path('register/',views.register,name="register"),

    path('login/',views.log,name="login"),

    path('dashboard/',views.dashboard,name="dashboard"),

    path('addpost/',views.addpost,name="addpost"),

    path('listall/',views.viewall,name="viewall"),

    path('viewone/',views.viewone,name="viewone"),

    path('deleteone/',views.deleteone,name="deleteone"),

    path('about/',views.about,name="about"),

    path('buy/',views.buy,name="buy"),

    path('contact/',views.contact,name="contact"),

    path('index/',views.index,name="index"),

    path('medicine/',views.medicine,name="medicine"),

   

]