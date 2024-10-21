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
    path("stud_profile/", views.stud_profile, name='stud_profile'),
    path("stud_admin/", views.stud_admin, name="stud_admin"),
    path("event/", views.event, name="event"),
    path("add/delete_event/<str:event_id>/", views.delete_event, name="delete_event"),
    path("add/update_event/<str:event_id>/", views.update_event, name='update_event'),
    path("add/update_event/save_update_event/<str:event_id>", views.save_update_event, name='save_update_event'),
    path("list/delete_list/<int:student_id>", views.delete_list, name='delete_list'),
    path("add/search_event/<str:event_name>/", views.add, name='add'),
    path("edit_profile_s", views.edit_profile_s, name="edit_profile_s"),
    path("stud_profile/edit_profile_s/save_update_profile/<int:student_id>/", views.save_update_profile, name="save_update_profile"),
] 