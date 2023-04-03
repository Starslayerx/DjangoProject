from django.urls import path
from game.views import index # game/views的函数index

urlpatterns = [
        path("", index, name = "index"),
]
