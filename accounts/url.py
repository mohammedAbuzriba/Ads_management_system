from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('changePassword/',auth_views.PasswordChangeView.as_view(template_name='changePassword.html'),name='changePassword'),
    path('change_password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='changePasswordDone.html'),name='password_change_done'),
    path('account/',views.UserUpdateview.as_view(),name='myAccount')

]
