from django.urls import path
from . import views

urlpatterns = [
    path('addnotepage', views.addnotepage,name='addnotepage'),#page
    path('addnote', views.addnote,name='addnote'),#action
    path('logout', views.logout,name='logout'),#action
    path('', views.viewnote,name='viewnote'),#page
    path('login', views.login,name='login'),#page
    path('updatenote/<int:notes_id>', views.updatenote,name='updatenote'),#page
    path('deletenote/<int:notes_id>', views.deletenote,name='deletenote'),#action
    
    
]