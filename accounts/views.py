from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignUpForm,UserForm, ProfileForm
from django.contrib.auth import authenticate,login
from  .models import Profile

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/accounts/profile')

    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html',{'form':form})



def profile(request):
	user = request.user
	profile = Profile.objects.get(user=request.user)

	return render(request,'accounts/profile.html',{'profile':profile})

 
def edit_profile(request, slug):

    profile = get_object_or_404(Profile, slug=slug)
    if request.method == "POST":
        user_form    = UserForm(request.POST, instance=request.user)
        Profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and Profile_form.is_valid():
            user_form.save()
            new_profile = Profile_form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
    else:
        user_form    = UserForm(instance=request.user)
        Profile_form = ProfileForm(instance=profile)
    context = {

        'user_form':user_form,
        'Profile_form':Profile_form
    }
    return render(request, 'accounts/edit_profile.html', context)
