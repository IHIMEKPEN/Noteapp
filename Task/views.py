from django.shortcuts import render,redirect
from .models import Notes,Users

# Create your views here.


def addnotepage(request):
    name='john'
    context={
        'name':name,
    }
    return render(request,'task/addnotes.html',context)

def login(request):
    name='john'
    context={
        'name':name,
    }
    return render(request,'task/login.html',context)

def signup(request):
    if request.method =="POST":        
        username=request.POST['username']   
        email=request.POST['email']   
        password1=request.POST['password1']   
        password2=request.POST['password2']   
        user=Users(username=username,email=email,password1=password1)     
        user.save()
        return redirect('viewnote')
    
    return render(request,'task/signup.html')

def logout(request):
    name='john'
    context={
        'name':name,
    }
    return redirect('login')

def viewnote(request):    
    notes=Notes.objects.all()      
    context={
        "notes":notes,        

    }
    return render(request,'task/viewnotes.html',context)

#handle functionaly of adding note
def addnote(request):
    if request.method =="POST":        
        msg=request.POST['message']   
        title=request.POST['title']   
        notes=Notes(note=msg,title=title)     
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

