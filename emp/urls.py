from django.urls import path

from .import views

urlpatterns=[
    path('',views.index,name='home'),
    path('edit/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
]