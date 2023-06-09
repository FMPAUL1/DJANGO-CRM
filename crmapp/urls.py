from django.urls import path

from .views import Home ,logout_user,reg_user,customer_record,delete_record, add_record, update_record
urlpatterns = [
    path("", Home, name="home"),
    path("logout",logout_user, name='logout' ),
    path("register",reg_user, name='register' ),

    path("record/<int:pk>", customer_record, name='record' ),
    
    path("delete/<int:pk>", delete_record, name='delete' ),
    path("addrecord/", add_record, name='create' ),
    path("updateerecord/<int:pk>", update_record, name='update' ),
    
]

