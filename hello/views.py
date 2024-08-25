from django.shortcuts import render,redirect
from .forms import LoginModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def home_view(request):
    form = LoginModelForm()  # Replace with your form logic
    if request.method == 'POST':
        form = LoginModelForm(request.POST)
        if form.is_valid():
            # Process the form
            pass
    
    return render(request, 'home.html', {'form': form})

def myView(request):
    if request.method == 'POST':
        form = LoginModelForm(request.POST)
        if form.is_valid():
            cust = form.save()
            return render(request,'form-data.html',{
                'message': 'Data saved to db',
                'customer': cust
            })
    else:
        form = LoginModelForm()
    return render(request,'index.html',{'form':form})

def aboutUs(request):
    return render(request,'aboutus.html')
def pages(request, title):
    return render(request,'pages.html',{'title':title})
def count(request, num):
    return render(request,'count.html',{'num':num})

def pagevisit(request):
    # Get the current count from the session, or set it to 0 if it doesn't exist
    count = request.session.get('page_count', 0)
    # Increment the count
    count += 1
    # Store the updated count in the session
    request.session['page_count'] = count
    # Render the template with the count variable
    return render(request,'page_view.html', {'count': count})

def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            # Redirect to login page after successful signup
            return redirect('createproduct')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            # Redirect to home page after successful login
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)


@login_required(login_url='/login/')
def aboutUs(request):
    return render(request,'about-us.html')

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def  user_check(user):
    return user.username.endswith('@gmail.com')

@login_required(login_url='/login/')
@user_passes_test(user_check,login_url='/login/')
def aboutUs(request):
    return render(request,'about-us.html')