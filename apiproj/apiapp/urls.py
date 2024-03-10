from django.urls import path
from apiapp import views
urlpatterns = [
    path('clients', views.client),
    path('projects', views.project),
    path('users', views.usersinfo),
    path('users/<uid>', views.userAct),
    path('clients/<clientid>', views.clientAct),
    path('projects/<pid>', views.projectAct)
    
    # path('emp/<empid>', views.clientAct)
]