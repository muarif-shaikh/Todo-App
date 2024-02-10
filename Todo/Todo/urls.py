from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("", todoapp, name="todoapp"),
    path("delete-todo/<id>/", delete_todo, name="delete_todo"),
    path("update-todo/<id>/", update_todo, name="update_todo"),
    path("about/", about_page, name="about_page")

    # path('admin/', admin.site.urls),
]
