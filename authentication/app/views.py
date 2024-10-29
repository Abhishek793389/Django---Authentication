from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from . forms import userform, profileform, blogform, edituser
from . models import Profile,Blog, User
from django.contrib.auth import authenticate,login,logout as user_logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# signup data
def showform(request):
        if request.method == 'POST':
            form = userform(request.POST)
            form1 = profileform(request.POST, request.FILES) 

            if form.is_valid() and form1.is_valid():
                user = form.save() 
                profile = form1.save(commit=False) 
                profile.user = user 
                profile.save()  
                messages.success(request, "Account Register Successfully")
                return redirect('login')

        else:
            form = userform()
            form1 = profileform()

        context = {
            "form": form,
            "form1": form1,
        }
        return render(request, 'app/signup.html', context)


# login user
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            
            if form.is_valid() :
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password) 
                if user is not None:
                    login(request, user)
                    request.session['username'] = username
                    request.session['user_session_id'] = request.session.session_key
                    messages.success(request, f"Welcome {user.first_name} here your profile!")
                    return redirect('userprofile')  
                
                    
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            form = AuthenticationForm()
            
        return render(request, 'app/login.html',{'form':form})
    else:
        return redirect('userprofile')



# Display base temp data
def base(request):
    return render(request, 'app/base.html')

# user profile data

def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        blog_data = Blog.objects.filter(user=user)
        session_id = request.session.get('user_session_id', None)
        
        context = {
            'user': user,
            'profile': profile,
            'data': blog_data, 
            'session_id':session_id 
        }
        return render(request, 'app/datadisplay.html', context)
    else:
        messages.error(request, "Login  required  to  access  Dashboard")
    return redirect('login')

# home
def home(request):
    return render(request, 'app/home.html')


#logout
@login_required
def logout(request):
    user_logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('login')


# blog
@login_required
def blog(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = blogform(request.POST)  
            if form.is_valid():
                blog = form.save(commit=False)  
                blog.user = request.user  
                blog.save()  
                messages.success(request, "Blog added successfully")
                return redirect('userprofile')  
        else:
            form = blogform() 
        return render(request, 'app/blog.html', {'form': form})
    else:
        messages.error(request, "Login  required  to  access  Dashboard")
    return redirect('login')
    
# blog data

def all_blog(request):
    if request.user.is_authenticated:
        current_user = request.user
        blog_data = Blog.objects.filter(user = current_user)
        return render(request, 'app/viewblog.html', {'data':blog_data})
    else:
            messages.error(request, "Login  required  to  access  Dashboard")
    return redirect('login')


# change password

def changepassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully')
                return redirect('login')
                
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'app/changepass.html', {'form': form})

    else:
        return redirect('login')
    
    
# update user

def update_user(request, id):
    update = User.objects.get(pk=id)
    additional_data = update.profile
    if request.method == "POST":
        form = edituser(request.POST, instance=update)
        form1 = profileform(request.POST, request.FILES, instance=additional_data)
        if form.is_valid() and form1.is_valid():
            user = form.save() 
            profile = form1.save(commit=False) 
            profile.user = user  
            profile.save()  
            messages.success(request, 'Account updated successfully.')
            return redirect('userprofile') 
    else:
        form = edituser(instance=update)
        form1 = profileform(instance=additional_data)
    return render(request, 'app/signup.html', {'form': form, 'form1': form1})


# delete user
def delete_user(request):
    return render(request, 'app/delete.html')



# # delete blog
# def delete_blog(request, id):
#     if request.method =='POST':
#         form = Blog.objects.get(pk=id, user = request.user)
#         form.delete()
#         messages.success(request, 'Blog deleted Successfully')
#         return redirect('viewblog')
#     else:
#         return render(request,'app/datadisplay.html')

@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    if blog.user == request.user:
        blog.delete()
        messages.success(request, 'Blog deleted Successfully')
        return redirect('viewblog')
    
        
# delete user

@login_required
def delete_login_user(request,id):
    if request.user.is_authenticated:
        delete = User.objects.get(pk = id)

        if request.method =='POST':
            delete_choice = request.POST.get('delete_choice')
            

            if delete_choice == 'delete_session':
                request.session.flush()
                messages.success(request,'Sessions deleted but User remains')
                return redirect('login')
            
            elif delete_choice == 'delete_user':
                delete.delete()
                messages.success(request,'User deleted but sessions remains')
                return redirect('login')
            
            elif delete_choice =='delete_all':
                request.session.flush()
                delete.delete()
                messages.success(request, 'All data deleted')
                return redirect('login')

        return render(request, 'app/delete.html',{'user':delete})
    else:
      return redirect('login')

# About

def about_section(request):
    return render(request, 'app/about.html')

# update blog
def update_blog(request, id):
    if request.method == 'POST':
        update = Blog.objects.get(pk = id)
        form = blogform(request.POST, instance=update)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated')
            return redirect('viewblog')
    else:
        update = Blog.objects.get(pk=id)
        form = blogform(instance=update)
    return render(request, 'app/blog.html', {'form':form})
