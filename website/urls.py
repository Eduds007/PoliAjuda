from django.urls import path
from .views import  main, upload, login, logout_page, materia_page


urlpatterns = [
    path('', main, name='menu'),
    path('upload/', upload, name='upload'),
    path('login/', login, name='login'),
    path('logout/', logout_page, name="logout"),
    path('<str:id>', materia_page, name='materia')
]
