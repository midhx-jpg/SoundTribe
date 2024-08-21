from django.shortcuts import render,redirect
from Backend.models import songdb,Eventdb,Genredb
from Frontend.models import contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def sound_index(req):
    return render(req,"index.html")

def add_music(req):
    data=Genredb.objects.all()
    return render(req,"Add_Music.html",{'data':data})

def view_music(req):
    data=songdb.objects.all()
    return render(req,"View_Music.html",{'data':data})

def add_genre(req):
    return render(req,"Add_Genre.html")

def view_genre(req):
    data=Genredb.objects.all()
    return render(req,"View_Genre.html",{'data':data})

def save_genre(req):
    if req.method=="POST":
        gna=req.POST.get("gname")

        des=req.POST.get("desc")

        ob=Genredb(Genre_name=gna,Description=des)
        ob.save()
        return redirect(add_genre)

def delete_genre(req,gid):
    data=Genredb.objects.filter(id=gid)
    data.delete()
    return redirect(view_genre)

def save_music(req):
    if req.method=="POST":
        sna=req.POST.get("sname")
        ana=req.POST.get("aname")
        gen=req.POST.get("genre")
        des=req.POST.get("desc")
        img=req.FILES["image"]
        song=req.FILES["song"]
        ob=songdb(Song_name=sna,Artist_name=ana,Genre=gen,Description=des,Song_Image=img,Song=song)
        ob.save()
        return redirect(add_music)

def edit_song(req,sid):
    data=songdb.objects.get(id=sid)
    genre=Genredb.objects.all()
    return render(req,"Edit_Music.html",{'data':data,'genre':genre})

def update_song(req,sid):
    if req.method=="POST":
        sna = req.POST.get("sname")
        ana = req.POST.get("aname")
        gen = req.POST.get("genre")
        des = req.POST.get("desc")
        try:
            img = req.FILES["image"]
            fs=FileSystemStorage()
            ifile=fs.save(img.name,img)
        except:
            ifile=songdb.objects.get(id=sid).Song_Image

        try:
            song = req.FILES["song"]
            fs=FileSystemStorage()
            sfile=fs.save(song.name,song)
        except:
            sfile=songdb.objects.get(id=sid).Song

    songdb.objects.filter(id=sid).update(Song_name=sna,Artist_name=ana,Genre=gen,Description=des,Song_Image=ifile,Song=sfile)
    return redirect(view_music)
def delete_song(req,sid):
    data=songdb.objects.filter(id=sid)
    data.delete()
    return redirect(view_music)

def add_event(req):
    return render(req,"Add_Events.html")

def save_event(req):
    if req.method=="POST":
        ena=req.POST.get("ename")
        p1na=req.POST.get("p1name")
        p2na=req.POST.get("p2name")
        p3na=req.POST.get("p3name")
        p4na=req.POST.get("p4name")
        p1rl=req.POST.get("p1role")
        p2rl=req.POST.get("p2role")
        p3rl=req.POST.get("p3role")
        p4rl=req.POST.get("p4role")
        ven=req.POST.get("venue")
        pri=req.POST.get("price")
        date=req.POST.get("date")
        time=req.POST.get("time")
        des=req.POST.get("desc")
        add=req.POST.get("address")
        img=req.FILES["image"]
        p1img=req.FILES["p1image"]
        p2img=req.FILES["p2image"]
        p3img=req.FILES["p3image"]
        p4img=req.FILES["p4image"]
        ob=Eventdb(Event_name=ena,Venue_hall=ven,Price=pri,Date=date,Time=time,Description=des,Venue_address=add,Event_Image=img,Performer1=p1na,Performer2=p2na,Performer3=p3na,Performer4=p4na,Performer1role=p1rl,Performer2role=p2rl,Performer3role=p3rl,Performer4role=p4rl,Performer1Image=p1img,Performer2Image=p2img,Performer3Image=p3img,Performer4Image=p4img)
        ob.save()
        return redirect(add_event)

def view_event(req):
    data=Eventdb.objects.all()
    return render(req,"View_Events.html",{'data':data})

def edit_event(req,eid):
    data=Eventdb.objects.get(id=eid)
    return render(req,"Edit_Events.html",{'data':data})

def update_event(req,eid):
    if req.method=="POST":
        ena = req.POST.get("ename")
        ven = req.POST.get("venue")
        pri = req.POST.get("price")
        date = req.POST.get("date")
        time = req.POST.get("time")
        des = req.POST.get("desc")
        add = req.POST.get("address")
        p1na=req.POST.get("p1name")
        p2na=req.POST.get("p2name")
        p3na=req.POST.get("p3name")
        p4na=req.POST.get("p4name")
        p1rl=req.POST.get("p1role")
        p2rl=req.POST.get("p2role")
        p3rl=req.POST.get("p3role")
        p4rl=req.POST.get("p4role")
        try:
            img = req.FILES["image"]
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except:
            file = Eventdb.objects.get(id=eid).Event_Image
        
        try:
            p1 = req.FILES["p1image"]
            fs = FileSystemStorage()
            p1img = fs.save(p1.name, p1)
        except:
            p1img = Eventdb.objects.get(id=eid).Performer1Image

        try:
            p2 = req.FILES["p2image"]
            fs = FileSystemStorage()
            p2img = fs.save(p2.name, p2)
        except:
            p2img = Eventdb.objects.get(id=eid).Performer2Image

        try:
            p3 = req.FILES["p3image"]
            fs = FileSystemStorage()
            p3img = fs.save(p3.name, p3)
        except:
            p3img = Eventdb.objects.get(id=eid).Performer3Image

        try:
            p4 = req.FILES["p4image"]
            fs = FileSystemStorage()
            p4img = fs.save(p4.name, p4)
        except:
            p4img = Eventdb.objects.get(id=eid).Performer4Image
    Eventdb.objects.filter(id=eid).update(Event_name=ena,Venue_hall=ven,Price=pri,Date=date,Time=time,Description=des,Venue_address=add,Event_Image=file,Performer1=p1na,Performer2=p2na,Performer3=p3na,Performer4=p4na,Performer1role=p1rl,Performer2role=p2rl,Performer3role=p3rl,Performer4role=p4rl,Performer1Image=p1img,Performer2Image=p2img,Performer3Image=p3img,Performer4Image=p4img)
    return redirect(view_event)

def delete_event(req,eid):
    data=Eventdb.objects.filter(id=eid)
    data.delete()
    return redirect(view_event)

def admin(req):
    return render(req,"Admin_login.html")

def admin_login(req):
    if req.method=="POST":
        un=req.POST.get("username")
        pas=req.POST.get("pass")
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pas)
            if x is not None:
                login(req,x)
                req.session['username']=un
                req.session['password']=pas
                messages.success(req, "Welcome,Homie $")
                return redirect(sound_index)
            else:
                messages.warning(req, "Incorrect password!!")
                return redirect(admin)
        else:
            messages.error(req,"User not found")
            return redirect(admin)

def admin_logout(req):
    del req.session['username']
    del req.session['password']
    messages.success(req, "Successfully Logout")

    return redirect(admin)

def view_message(req):
    data=contactdb.objects.all()
    return render(req,"View_message.html",{"data":data})

def delete_message(req,mid):
    data=contactdb.objects.filter(id=mid)
    data.delete()
    return redirect(view_message)
