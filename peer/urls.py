from django.urls import path
from . import views

urlpatterns=[
    path("", views.homepage, name='index'),
    path("register/", views.register, name='register'),
    path("login/", views.login, name='login'),
    path("welcome-user/", views.welcome_user, name='welcome-user'),
    path("man_stud/", views.man_stud, name='man_stud'),
    path("fill/", views.fill, name='fill'),
    path("learn_more/", views.learn_more, name='learn_more'),
    path("contact_us", views.contact_us, name='contact_us'),
    path("admin_page/", views.admin_page, name='admin_page'),
    path("list/", views.list, name='list'),
    path("add/", views.add, name='add'),
    path("man_stud/delete_student/<int:student_id>/", views.delete_student, name="delete_student"),
] 