from django.db import models

# Create your models here.
class contactus(models.Model):
    Name=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Message=models.TextField()
    def __str__(self):
        return self.Name
#############################################
class slider(models.Model):
    shead=models.CharField(max_length=300)
    ssubject=models.CharField(max_length=500)
    sdes=models.TextField()
    spic=models.ImageField(upload_to='static/slider/',default="")
    def __str__(self):
        return self.shead
    ######################################
class igallery(models.Model):
    gname=models.CharField(max_length=400)
    gpic=models.ImageField(upload_to='static/gallery/',default="")
    def __str__(self):
        return self.gname
########################################################################

class myblog(models.Model):
    bname=models.CharField(max_length=40)
    bdes=models.TextField()
    bpic=models.ImageField(upload_to='static/blogs',null=True)
    bdate=models.DateField()
    def __str__(self):
        return self.bname
############################################################
class city(models.Model):
    ncity=models.CharField(max_length=30)
    cdate=models.DateField()
#######################################################
class members(models.Model):
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=90)
    cacc=models.CharField(max_length=26)
    caddress=models.TextField()
    paddress=models.TextField()
    pcode=models.IntegerField()
    city=models.CharField(max_length=50)
    ppic=models.ImageField(upload_to='static/profile/',null=True)

####################################################################
class vgallery(models.Model):
    vlink=models.TextField()
    vdes=models.TextField()
    vtitle=models.CharField(max_length=200)
    vdate=models.DateField()

#################################################
class donateus(models.Model):
    avalue=models.IntegerField()
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    mob=models.CharField(max_length=50)
    cont=models.CharField(max_length=40)
    add=models.CharField(max_length=100)
    sta=models.CharField(max_length=40)
    pin=models.IntegerField()
    occ=models.CharField(max_length=20)
    ppic=models.ImageField(upload_to='static/screenshot/')
    # def __str__(self):
    #     return self.fname
