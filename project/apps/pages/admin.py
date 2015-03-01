from django.contrib import admin
# from django.conf.urls import patterns, url

from django.shortcuts import render

from apps.pages.models import *

def feed_scheduler(request,*args,**kwargs):
    template = "admin/schedules.html"

    merchants = Merchants.objects.all()
    providers = Providers.objects.all()
    feeds = Feeds.objects.all()

    context = {"merchants":merchants,"providers":providers,"feeds":feeds}

    return render(request,template,context)



admin.site.register_view('feed_scheduler', view=feed_scheduler)


# class CustomPeriodicScheduleAdmin(admin.ModelAdmin):
#     def get_urls(self):
#         urls = super(CustomPeriodicScheduleAdmin, self).get_urls()
#         schedule_urls = patterns('',
#             (r'^schedule_feed/$', self.admin_site.admin_view(self.schedule_feed))
#         )
#         return schedule_urls + urls
#
#     def schedule_feed(self,request):
#         template="admin/schedules.html"
#         return render(request,template)
#
# admin.site.register(Feeds,CustomPeriodicScheduleAdmin)

class ProviderAdmin(admin.ModelAdmin):
    fields = ('name','description','url','logo')

class MerchantAdmin(admin.ModelAdmin):
    fields = ('name', 'url', 'logo')

class FeedAdmin(admin.ModelAdmin):
    fields = ('provider','merchant','url','username','password','periodic_task')

admin.site.register(Providers, ProviderAdmin)
admin.site.register(Merchants, MerchantAdmin)
admin.site.register(Feeds, FeedAdmin)