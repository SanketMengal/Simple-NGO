from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
def index(request):
    data=slider.objects.all().order_by('-id')[0:2]
    bdata=myblog.objects.all().order_by('-id')[0:3]
    # d=myblog.objects.all().order_by('-id')[0:3]
    im = igallery.objects.all().order_by('-id')[0:4]
    mydict={"res":data,"data":bdata,"img":im}
    return render(request,'user/index.html',mydict)
#################################################################
def about(request):
    return render(request,'user/about.html')
#################################################################
def contact(request):
    status=False
    if request.method=="POST":
        x=request.POST.get('name')
        y=request.POST.get('email')
        z=request.POST.get('mob')
        a=request.POST.get('msg')
        contactus(Name=x,Email=y,Mobile=z,Message=a).save()
        status=True
        #mydict={"Name":x,"Email":y,"Mobile":z,"Message":a}

    msg={"m":status}
    return render(request,'user/contact.html',context=msg)
#################################################################
def video(request):
    data=vgallery.objects.all().order_by('-id')
    myd={"vdata":data}
    return render(request,'user/video.html',myd)
#################################################################
def gallery(request):
    d=igallery.objects.all().order_by('-id')[0:3]
    mydict={"data":d}
    return render(request,'user/gallery.html',context=mydict)
##################################################################
def blog(request):
    bdata=myblog.objects.all().order_by('-id')[0:3]
    if request.method=="POST":
        s=request.POST.get('search')
        if s is not "":
            bdata=myblog.objects.all().filter(Q(bname__icontains=s) | Q(bdes__icontains=s))
        else:
            return HttpResponse("<script>alert('Please Enter Data for search');location.href='/user/blog/'</script>")



    mydict={"bdata":bdata}
    return render(request,'user/blog.html',mydict)
##################################################################
def login(request):
    return render(request,'user/login.html')
##################################################################
def membership(request):
    cities=city.objects.all().order_by('-id')
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('pincode')
        d=request.POST.get('acc')
        e=request.POST.get('caddress')
        f=request.POST.get('paddress')
        g=request.POST.get('city')
        h=request.FILES.get('ppic')
        members(name=a,email=b,cacc=d,paddress=f,caddress=e,pcode=c,city=g,ppic=h).save()
    mydict={"ct":cities}
    return render(request,'user/membership.html',mydict)
#################################################################
def donate(request):
    ddata=donateus.objects.all().order_by('-id')
    # status=False
    if request.method=="POST":
        l=request.POST.get('avalue')
        b=request.POST.get('fname')
        c=request.POST.get('lname')
        d=request.POST.get('email')
        e=request.POST.get('mob')
        f=request.POST.get('cont')
        g=request.POST.get('add')
        h=request.POST.get('sta')
        i=request.POST.get('pin')
        j=request.POST.get('occ')
        k=request.FILES.get('ppic')
        donateus(avalue=l,fname=b,lname=c,email=d,mob=e,cont=f,add=g,sta=h,pin=i,occ=j,ppic=k).save()
        # status=True
    dict={"dn":ddata}
    # msg={"m":status}
    return render(request,'user/donate.html', dict)
##############################################################
def causes(request):
    return render(request,'user/causes.html')
#######################################################
def vdodetails(request):
    y=request.GET.get('msg')
    x=vgallery.objects.all().filter(id=y)
    myd={"vdata":x}
    return render(request,'user/details.html',myd)
#####################################################
def blogdetails(request):

    y=request.GET.get('msg')

    a=request.GET.get('msg')
    data=myblog.objects.all().filter(id=y)
    md={"data":data}
    return render(request,'user/bdetails.html',md)
###########################################################
def my(request):
    return render(request,'user/my.html')