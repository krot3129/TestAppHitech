from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.CustomSignupView.as_view(), name='account_signup'),
    path('login/', views.CustomLoginView.as_view(), name='account_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='account_logout'),
    path('confirm-email/<str:key>/', views.CustomConfirmEmailView.as_view(), name='account_confirm_email'),
    path('profile/<uuid:user_id>/', views.ProfileView.as_view(), name='account_profile'),
    path('edit-profile/<uuid:user_id>/', views.EditProfileView.as_view(), name='account_edit_profile'),
    path('change-password/', views.ChangePasswordView.as_view(), name='account_change_password'),
    path('change-email/', views.ChangeEmailView.as_view(), name='account_change_email'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='account_reset_password'),
    path('reset-password/done/', views.ResetPasswordDoneView.as_view(), name='account_reset_password_done'),
    path('reset-password/confirm/<uidb64>/<token>/', views.ResetPasswordConfirmView.as_view(), name='account_reset_password_confirm'),
    path('reset-password/complete/', views.ResetPasswordCompleteView.as_view(), name='account_reset_password_complete'),
    path('user-list/', views.UserListView.as_view(), name='user_list'),
]
