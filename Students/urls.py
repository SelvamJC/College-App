from django.urls import path
from Students import views


urlpatterns = [
    path('depget/', views.DepartmentView.as_view(), name='depget'),
    path('deppost/', views.DepartmentView.as_view(), name='deppost'),
    path('depupdate/<int:id>', views.DepartmentView.as_view(), name='depupdate'),
    path('depdelete/<int:id>', views.DepartmentView.as_view(), name='depdelete'),

    path('stdget/', views.StudentView.as_view(), name='stdget'),
    path('stdpost/', views.StudentView.as_view(), name='stdpost'),
    path('stdupdate/<int:id>', views.StudentView.as_view(), name='stdupdate'),
    path('stddelete/<int:id>', views.StudentView.as_view(), name='stddelete'),
]