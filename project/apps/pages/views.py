from django.shortcuts import render
from django.http import HttpResponse

from vanilla import TemplateView

from apps.pages.forms import *




class HomePageView(TemplateView):
    template_name = "pages/home.jade"

class AboutPageView(TemplateView):
    template_name = "pages/about.jade"

class PrivacyPageView(TemplateView):
    pass

class TermsPageView(TemplateView):
    pass

# def add_provider(request,*args,**kwargs):
#     if request.method=="POST":
#         form = AddProvider(request.POST,request.FILES)
#         if form.is_valid():
#             f = form.save(commit=False)
#             f.logo = request.FILES["logo"]
#             f.save()
#             return HttpResponse("success")
#     else:
#         form = AddProvider()
#     return render(request,"admin/schedules.html",{"form":form})


