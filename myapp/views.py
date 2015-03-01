#coding=utf-8
from django.shortcuts import render
from myapp.models import User
from django.template.loader import get_template
from django.template.context import Context
from django.http.response import HttpResponse,HttpResponseRedirect
from myapp.form import UserregistForm,UserloginForm
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
#def regist(request):
    #if request.method=='GET':
      #  uf=UserregistForm(request.GET)
      #  if uf.is_valid():
       #     username=uf.cleaned_data['username']
       #     password=uf.cleaned_data['password']
        #    User.objects.create(username=username,password=password)
            #return HttpResponseRedirect('/login/')
         #   return HttpResponse('成功注册')
    #else:

       # t=get_template('./regist.html')
        #c=Context()
       # html=t.render(c)
        #return HttpResponse(html)

def regist(request):
    if request.method=='POST':
        uf=UserregistForm(request.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            user=User.objects.create(username=username,password=password)

            #t=get_template('./login.html')
            #c=Context()
            #html=t.render(c)
            #return HttpResponse(html)
            return HttpResponseRedirect('/login/')
    else:
        uf=UserregistForm()
        return render_to_response('regist.html',context_instance=RequestContext(request))

        #return render_to_response('regist.html',{'uf':uf},content_instance=RequestContext(request))
        #return render_to_response('regist.html',content_instance=RequestContext(request))
def login(request):
    if request.method=='POST':
        uf=UserloginForm(request.POST)
        if uf.is_valid():
            cd=uf.cleaned_data
            username=cd['username']
            password=cd['password']
            user=User.objects.filter(username=username,password=password)
            if user:
                response=HttpResponseRedirect('/index/')
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf=UserloginForm()
        return render_to_response('login.html',context_instance=RequestContext(request))

def index(request):

   username=request.COOKIES.get('username','')
   t=get_template('./index.html')
   c=Context({'username':username})
   html=t._render(c)
   return HttpResponse(html)
def logout(request):
    t=get_template('./logout.html')
    c=Context()
    html=t.render(c)
    response=HttpResponse(html)
    response.delete_cookie('username')
    return response



