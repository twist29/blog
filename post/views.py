
from django.shortcuts import render, HttpResponse,get_object_or_404, HttpResponseRedirect,redirect,Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def post_index(request):
    post_list = Post.objects.all()

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query)| 
            Q(content__icontains=query) 
            #Q(user__first_name__icontains=query) |
           # Q(user__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(post_list, 3)  # Show 3 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, "post/index.html", {'posts': posts})

def post_detail(request,id):
    post= get_object_or_404(Post,id=id)
    context={
        'post': post,
        }
    return render(request,'post/detail.html',context)


def post_create(request):
    
    #1.YOL
    #if request.method== "POST":
     #   print(request.POST)#GELEN POST ÝSTEGÝNÝ YAZDIR
     
   # title= request.POST.get('title')
    #content= request.POST.get('content') 
    #Post.objects.create(title=title, content=content)
    
    #2.YOL:
   # if request.method== "POST":
        #FORMDAN GELEN BILGILERI KAYDET
      #  form= PostForm(request.POST)
    #else:
        #FORMU KULLANICIYA GOSTER
       # form= PostForm()
      #  if form.is_valid():
           # form.save()#DATABASE'E KAYDETTIK 
    #context={'form': form,
      #  }        
    
    
    #3.YOL
    if not request.user.is_authenticated:
        return Http404()
    
    form= PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post= form.save()
        messages.success(request,'Operation Successfully Completed')
        return HttpResponseRedirect(post.get_absolute_url())
            
    context= {
        'form': form,
    }
    
    return render(request, 'post/form.html', context)


def post_update(request,id):
    
    if not request.user.is_authenticated:
        return Http404()
    
    post= get_object_or_404(Post,id=id)#get post
    form= PostForm(request.POST or None, request.FILES or None, instance=post)#get form info
    if form.is_valid():#save user action
        form.save()
        messages.success(request,'Operation Successfully Completed', extra_tags= 'Message-Successful')
        return HttpResponseRedirect(post.get_absolute_url())
             
    context= {
        'form': form,
    }#send form object as content(içerik olarak gönder)
    return render(request, 'post/form.html', context)


def post_delete(request,id):
    
    if not request.user.is_authenticated:
        return Http404()
    
    post= get_object_or_404(Post,id=id)
    post.delete()#buraya kadar postu sildik. Postun içeriðini de silmemiz lazým.
    return redirect('post:index')#redirect ile delete desired post and its content i.e. by writing its name