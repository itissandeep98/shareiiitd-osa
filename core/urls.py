from django.urls import path

from .views import (ChangePasswordView, EditProfileView, ResetPasswordView,
                    UserList, current_user)

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('reset_password/', ResetPasswordView),
    path('change_password/', ChangePasswordView),
    path('edit_profile/', EditProfileView),
]
