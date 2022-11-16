from django.urls import path

from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('view',views.view,name='view'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),

]