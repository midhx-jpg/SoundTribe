from Frontend import views
from django.urls import path

urlpatterns=[
    path('',views.home,name="home"),
    path('album/<alphabet>',views.albums,name="album"),
    path('event/',views.events,name="event"),
    path('contact/',views.contact,name="contact"),
    path('news/',views.news,name="news"),
    # path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.log_out_view,name="logout"),
    # path('save_register/',views.save_register,name="save_register"),
    # path('loginbycheck/',views.loginbycheck,name="loginbycheck"),
    # path('user_logout/',views.user_logout,name="user_logout"),
    path('save_message/',views.save_message,name="save_message"),
    path('payment/',views.payment,name="payment"),
    path('save_check/',views.save_check,name="save_check"),
    path('history/',views.bookhistory,name="history"),
    path('eventdetails/<int:eid>',views.eventdetails,name="eventdetails"),
    path('music_player/<int:mid>/',views.music_player,name="music_player"),
    path('bookpdf/<int:booking_id>/',views.booking_pdf,name="bookpdf"),
    path('delete_history/<int:hid>/',views.delete_history,name="delete_history"),
    path('singlegenre/<genrename>/',views.singlegenre,name="singlegenre"),
    # path('chat/',views.chat,name="chat"),

    

]
