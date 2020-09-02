from django.urls import path, re_path
from . import views

urlpatterns = [
    # VIEWS
    path('view_base', views.view_base),
    path('view_date/<int:year>/<int:month>',
         views.view_date, name='dates'),  # name is not mandatory, is used for to be shorter
    re_path(
        r'^view_date/(?P<year>\d{4})/(?P<month>\d{2})', views.view_date),  # view_list with another method to write url
    path('redirection', views.view_redirect),
    path('view_id/<int:id_list>', views.view_list,
         name="show_id"),  # with id_list in url

    # VIEWS + TEMPLATES
    path('date', views.today_date),
    path('add/<int:n1>/<int:n2>', views.addition),

    # VIEWS + FORMS
    path('contact/', views.contact, name='contact'),
]
