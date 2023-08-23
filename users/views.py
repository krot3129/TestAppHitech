from allauth.account.views import SignupView, LoginView, ConfirmEmailView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, FormView

from users.forms import UserProfileForm
from users.models import CustomUser


class CustomSignupView(SignupView):
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account_login')

class CustomLoginView(LoginView):
    template_name = 'account/login.html'

class CustomConfirmEmailView(ConfirmEmailView):
    template_name = 'account/confirm_email.html'
    success_url = reverse_lazy('account_login')

class ChangePasswordView(TemplateView):
    template_name = 'account/change_password.html'

class ChangeEmailView(TemplateView):
    template_name = 'account/change_email.html'

class ResetPasswordView(FormView):
    template_name = 'account/reset_password.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('account_reset_password_done')

class ResetPasswordDoneView(TemplateView):
    template_name = 'account/reset_password_done.html'

class ResetPasswordConfirmView(FormView):
    template_name = 'account/reset_password_confirm.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('account_reset_password_complete')

class ResetPasswordCompleteView(TemplateView):
    template_name = 'account/reset_password_complete.html'



class UserListView(ListView):
    model = get_user_model()
    template_name = 'account/user_list.html'
    context_object_name = 'users'

class ProfileView(View):
    template_name = 'account/profile.html'

    def get(self, request, user_id):
        user = CustomUser.objects.get(id=user_id)
        context = {
            'user': user,
        }
        return render(request, self.template_name, context)


class EditProfileView(LoginRequiredMixin, View):
    template_name = 'account/edit_profile.html'

    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        form = UserProfileForm(instance=user)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('account_profile', user_id)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')