from django.contrib import admin
from .models import *
# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Mobile','Message')

admin.site.register(contactus,contactusAdmin)

class igalleryAdmin(admin.ModelAdmin):
    list_display = ('id','gname','gpic')
admin.site.register(igallery,igalleryAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','shead','ssubject','sdes','spic')
admin.site.register(slider,sliderAdmin)

class myblogAdmin(admin.ModelAdmin):
    list_display = ('bname','bdes','bpic','bdate')
admin.site.register(myblog,myblogAdmin)

class cityAdmin(admin.ModelAdmin):
    list_display = ('id','ncity','cdate')
admin.site.register(city,cityAdmin)

class memberAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','cacc','caddress','paddress','pcode','ppic')
admin.site.register(members,memberAdmin)

class vgalleryAdmin(admin.ModelAdmin):
    list_display = ('id','vlink','vdes','vtitle','vdate')
admin.site.register(vgallery,vgalleryAdmin)

class donateusAdmin(admin.ModelAdmin):
    list_display = ('id','avalue', 'fname','lname', 'email', 'mob','cont','add', 'sta', 'pin','occ','ppic')
admin.site.register(donateus,donateusAdmin)