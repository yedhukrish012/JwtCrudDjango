from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView )
from users.views import RegisterUser, RetrieveUserView, StudentCreateAPIView, StudentDeleteAPIView, StudentListAPIView, StudentUpdateAPIView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('list/user/',RetrieveUserView.as_view() ,name='getRoutes'),
    path('register/',RegisterUser.as_view(),name='register'),

    path('students/',  StudentListAPIView.as_view(), name='student-list'),
    path('students/create/', StudentCreateAPIView.as_view(), name='student-create'),
    path('students/<int:pk>/update/', StudentUpdateAPIView.as_view(), name='student-update'),
    path('students/delete/<int:pk>/', StudentDeleteAPIView.as_view(), name='delete_student'),
]