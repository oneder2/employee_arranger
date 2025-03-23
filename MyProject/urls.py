"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_one.views import assets_views, depart_views, employee_views, permission_views

index_urlpatterns = [
    path('', depart_views.index)
]

depart_urlpatterns = [
    path('depart/', depart_views.depart_list),
    path('depart/add/', depart_views.depart_add),
    path('depart/<int:nid>/modify/', depart_views.depart_modify),
    path('depart/<int:nid>/del/', depart_views.depart_del),
]

employee_urlpatterns = [
    path('employee/', employee_views.employee_list),
    path('employee/add/modelform/', employee_views.user_add_modelform),
    path('employee/<int:nid>/modify/', employee_views.user_modify_modelform),
    path('employee/<int:nid>/del/', employee_views.employee_del),
]

assets_urlpatterns = [
    path('assets/', assets_views.assets_list),
    path("assets/<int:nid>/del/", assets_views.assets_del),
    path('assets/add/modelform/', assets_views.assets_add_modelform),
    path('assets/<int:nid>/modify/modelform/', assets_views.assets_modify_modelform),
    # path('assets/create/', assets_views.create_assets),
]

permission_urlpatterns = [
    path('permission/', permission_views.permission_list),
    path("permission/<int:nid>/del/", permission_views.permission_del),
    path('permission/add/', permission_views.permission_add),
    path('permission/<int:nid>/modify/', permission_views.permission_modify),
    path('permission/<int:nid>/reset/', permission_views.permission_reset),
    # path('permission/create/', assets_views.create_assets),
]

urlpatterns =  [
    *index_urlpatterns,
    *depart_urlpatterns,
    *employee_urlpatterns,
    *assets_urlpatterns,
    *permission_urlpatterns,
    ]
