from django.urls import path
from taskmanagement import views

urlpatterns = [
    path('',views.taskmanagement,name='alltasks'),
    path('edit/<int:id>',views.edit_task,name='edit'),
    path('delete/<int:id>',views.delete_task,name='delete')

]