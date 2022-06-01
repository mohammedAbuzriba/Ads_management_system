from .views import profile

from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('changePassword/',auth_views.PasswordChangeView.as_view(template_name='changePassword.html'),name='changePassword'),
    path('change_password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='changePasswordDone.html'),name='password_change_done'),
    path('account/',views.UserUpdateview.as_view(),name='myAccount'),
    path('accounts/', include('allauth.urls')),
    path('profile/', profile, name='users-profile'),

    # path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="reset_password"),
    # path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),name="password_reset_done"),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),name="password_reset_confirm"),
    # path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_complete"),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]
