from django.urls import path
from . import views

urlpatterns = [
    path('',  views.home,name='home'),#page
    path('addnote', views.addnote,name='addnote'),#action
    path('viewnote', views.viewnote,name='viewnote'),#page
    path('updatenote/<int:notes_id>', views.updatenote,name='updatenote'),#page
    path('deletenote/<int:notes_id>', views.deletenote,name='deletenote'),#action
    
    
]