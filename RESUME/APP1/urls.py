from django.urls import path, re_path
from . import views

urlpatterns = [
    path('view_base', views.view_base),
    path('view_list/<int:year>/<int:month>',
         views.view_list),  # See views view_list
    re_path(
        r'^view_list2/(?P<year>\d{4})/(?P<month>\d{2})', views.view_list2),  # view_list2
]
