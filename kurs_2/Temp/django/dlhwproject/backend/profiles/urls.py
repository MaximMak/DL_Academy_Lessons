from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.ProfileDetail.as_view(), name="profiles_detail"),
    path("update/<int:pk>/", views.ProfileUpdate.as_view(), name="profiles_update"),
    path("avatar/update/<int:pk>", views.UpdateProfileAvatar.as_view(), name="avatar_update"),

]