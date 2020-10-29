from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('showlist', views.show_list),
    path('addshow', views.add_show),
    path('shows/<showId>', views.show_select)
]
