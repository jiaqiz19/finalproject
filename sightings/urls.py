from django.urls import path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='squirrel_all'),

    path('stats/', views.stats),

    path('add/', views.add, name='squirrel_add'),
    # url(r'^add$', views.add),
    # url(r'^<str:uid>$', views.uid),

    path('<str:squirrel_id>/', views.edit, name='squirrel_edit'),

    path('<str:squirrel_id>/delete/', views.delete, name='squirrel_delete')
 ]
