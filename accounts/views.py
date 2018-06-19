from django.shortcuts import render,redirect,reverse
from .forms import LoginForm, RegisterForm, UserProfile
from django.contrib.auth import authenticate, login, logout
#from django.template.context_processors import request
from django.contrib import messages
from django.http.response import HttpResponseRedirect

def login_view(request):
    form= LoginForm(request.POST or None)
    if form.is_valid():
        username= form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        user= authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')#goes home page therefore we need to create url for it
        
    return render(request, 'accounts/form.html', {'form': form, 'title': 'Login'})

def register_view(request):
    form= RegisterForm(request.POST or None)
    if form.is_valid():
        user= form.save(commit=False)
        password= form.cleaned_data.get('password1')
        user.set_password(password)
        user.is_staff=user.is_superuser=True
        user.save()
        new_user= authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('home')
    return render(request, 'accounts/form.html', {'form': form, 'title': 'Register'})

def logout_view(request):
    logout(request)
    return redirect('home')

def user_edit_profile(request):
    data={'sex': request.user.userprofile.sex, 'description': request.user.userprofile.description,'birth': request.user.userprofile.birth, 'phone_number': request.user.userprofile.phone_number}
    
    user_profile_form= UserProfile(request.POST or None, instance=request.user,initial=data)
    
    if request.method== "POST":
        if user_profile_form.is_valid():
            user_profile_form.save(commit=True)
            phone_number=user_profile_form.changed_data['phone_number']
            birth=user_profile_form.changed_data['birth']
            description=user_profile_form.changed_data['description']
            sex=user_profile_form.changed_data['sex']
            
            request.user.userprofile.sex=sex
            request.user.description.description=description
            request.user.userprofile.birth=birth
            request.user.userprofile.phone_number=phone_number
            request.user.userprofile.save()
            
            messages.success(request,"User informations successfully updated!")
            return HttpResponseRedirect(reverse('posts:post_list'))
    
    return render(request,'accounts/form.html',context={'form':user_profile_form})