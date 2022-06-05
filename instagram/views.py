from django.shortcuts import render,redirect,get_object_or_404
from .models import Image,Profile,Comment
from .forms import PostForm, UpdateUserForm, UpdateUserProfileForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()


            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    params = {
        'images': images,
        'form': form,
        'users': users,
    }


    return render(request, 'index.html', params)
   

@login_required(login_url='login')
def profile(request, username):
    #current_user = request.user
   
    #images = Image.objects.all().filter(profile_id=current_user.id)
    images = request.user.posts.all()

  
    if request.method == 'POST':
        #user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        #if user_form.is_valid() and prof_form.is_valid():
            #user_form.save()
        if prof_form.is_valid():    
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        #user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        #'user_form': user_form,
        'form': prof_form,
        'images': images,

    }

    return render (request, 'profile.html', params)
        

@login_required(login_url='/accounts/login/')
def new_status(request, username):
    current_user = request.user
    username = current_user.username
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.user = request.user
            image.save()
        return redirect('homePage')
    else:
        form = PostForm()
    return render(request, 'new_status.html', {"form": form})



@login_required(login_url='login')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.posts.all()



    params = {
        'user_prof': user_prof,
        'user_posts': user_posts,

    }

    return render(request, 'user_profile.html', params)    



    
