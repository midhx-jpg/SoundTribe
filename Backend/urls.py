from django.urls import path
from Backend import views

urlpatterns=[
    path('sound_index/',views.sound_index,name="sound_index"),
    path('add_music/',views.add_music,name="add_music"),
    path('add_genre/',views.add_genre,name="add_genre"),
    path('view_music/',views.view_music,name="view_music"),
    path('view_genre/',views.view_genre,name="view_genre"),
    path('save_music/',views.save_music,name="save_music"),
    path('save_genre/',views.save_genre,name="save_genre"),
    path('edit_song/<int:sid>/',views.edit_song,name="edit_song"),
    path('update_song/<int:sid>/',views.update_song,name="update_song"),
    path('delete_song/<int:sid>/',views.delete_song,name="delete_song"),
    path('delete_genre/<int:gid>/',views.delete_genre,name="delete_genre"),
    path('add_event/',views.add_event,name="add_event"),
    path('save_event/',views.save_event,name="save_event"),
    path('view_event/',views.view_event,name="view_event"),
    path('admin/',views.admin,name="admin"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('view_message/',views.view_message,name="view_message"),
    path('edit_event/<int:eid>/',views.edit_event,name="edit_event"),
    path('update_event/<int:eid>/',views.update_event,name="update_event"),
    path('delete_event/<int:eid>/',views.delete_event,name="delete_event"),
    path('delete_message/<int:mid>/',views.delete_message,name="delete_message"),
]
