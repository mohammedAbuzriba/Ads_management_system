from pyexpat.errors import messages

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy

from AdsBoard.models import Profile
from .forms import SignUpForm, UserUpdateForm, UpdateUserForm, UpdateProfileForm
from django.views.generic import UpdateView, FormView
from django.contrib.auth.models import User

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.




@login_required
def profile(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            # messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'ProfileUpdate.html', {'form': form, 'profile_form': profile_form})

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            profile = Profile.objects.create(
                user = user,
                bio = 'defult'
            )

            return redirect('home')
    return render(request,'signup.html',{'form':form})


class UserUpdateview(UpdateView):
    template_name = 'myAccount.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('myAccount')

    def get_object(self):
        return self.request.user


