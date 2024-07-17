from django.urls import path
from . import views

urlpatterns = [
    path('Machines/',views.MachinesListCreate.as_view(),name="Machines-view-create"),
    path('Machines/<int:id>/',views.MachinesRetrieveUpdateDestroy.as_view(),name="update ")
]