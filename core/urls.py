from django.urls import path

from .views import (ChangePasswordView, EditProfileView, ResendEmailView,
                    ResetPasswordView, UserList, VerifyEmailView, current_user)

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('reset_password/', ResetPasswordView),
    path('verify_email/', VerifyEmailView),
    path('resend_email/', ResendEmailView),
    path('change_password/', ChangePasswordView),
    path('edit_profile/', EditProfileView),
]
