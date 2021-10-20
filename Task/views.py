from django.shortcuts import render,redirect
from .models import Notes,User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
# Create your views here.


def addnotepage(request):
    if request.user.is_authenticated :

        name=request.user.username
        context={
            'name':name,
        }
        return render(request,'task/addnotes.html',context)
    else:
        return redirect('login')

def loginview(request):
    if request.method =="POST":        
        username=request.POST['username']          
        password=request.POST['password']           
        user = authenticate(request, username=username, password=password)
        
         # Check if authentication successful
        if user is not None:
            login(request,user)
            return redirect('viewnote')
        else:
             return render(request,'task/login.html', {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "task/login.html")
    
   
    

def signup(request):
    if request.method =="POST":        
        username=request.POST['username']   
        email=request.POST['email']   
        password=request.POST['password1']   
        confirmation=request.POST['password2']   

        if password != confirmation:
            return render(request, "task/signup.html", {
                "message": "Passwords must match."
            })

         # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "task/signup.html", {
                "message": "Username already taken."
            })
        login(request,user)
        return redirect('viewnote')
    else:
        return render(request, "task/signup.html")
        
    
  

def logoutview(request):
    logout(request)
    return redirect('login')


def viewnote(request):  
    name=request.user.username
   
    if request.user.is_authenticated :

        notes=request.user.noelated.all()      
        context={
            "notes":notes,        
            'name':name,
        }
        return render(request,'task/viewnotes.html',context)
    else:
        return redirect('login')

#handle functionaly of adding note
def addnote(request):
    if request.method =="POST":        
        msg=request.POST['message']   
        title=request.POST['title']   
        notes=Notes(note=msg,title=title,user=request.user) 
            
        notes.save()

    return redirect('viewnote')

#handle functionaly of adding note
def updatenote(request,notes_id):
    note=Notes.objects.get(id=notes_id)
    
    
    if request.method =="POST":     
        note=Notes.objects.get(id=notes_id)   
        msg=request.POST['message']   
        title=request.POST['title']  
        # print(note.note)
        note.title =title
        note.note =msg
            
        note.save()
        return redirect('viewnote')
    else :
        context={
            "note":note,     

        }
        
        
    return render(request,'task/editnotes.html',context)

#handle functionaly of deleting note
def deletenote(request,notes_id):
    Notes.objects.filter(id=notes_id).delete()    
    
    return redirect('viewnote')

# #handle functionaly of deleting note
# def editnote(request):
#     Notes.objects.filter(id=notes_id).delete()    
    
#     return redirect('viewnote')

