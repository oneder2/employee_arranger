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
from app_one.views import assets_views, depart_views, employee_views, permission_views, login_views

index_urlpatterns = [
    path('', depart_views.index, name="index"),
]

depart_urlpatterns = [
    path('depart/', depart_views.depart_list, name="depart_list"),
    path('depart/add/', depart_views.depart_add, name="depart_add"),
    path('depart/<int:nid>/modify/', depart_views.depart_modify, name="depart_modify"),
    path('depart/<int:nid>/del/', depart_views.depart_del, name="depart_del"),
]

employee_urlpatterns = [
    path('employee/', employee_views.employee_list, name="employee_list"),
    path('employee/add/modelform/', employee_views.user_add_modelform, name="user_add_modelform"),
    path('employee/<int:nid>/modify/', employee_views.user_modify_modelform, name="user_modify_modelform"),
    path('employee/<int:nid>/del/', employee_views.employee_del, name="employee_del"),
]

assets_urlpatterns = [
    path('assets/', assets_views.assets_list, name="assets_list"),
    path("assets/<int:nid>/del/", assets_views.assets_del, name="assets_del"),
    path('assets/add/modelform/', assets_views.assets_add_modelform, name="assets_add_modelform"),
    path('assets/<int:nid>/modify/modelform/', assets_views.assets_modify_modelform, name="assets_modify_modelform"),
    # path('assets/create/', assets_views.create_assets, name=""),
]

permission_urlpatterns = [
    path('permission/', permission_views.permission_list, name="permission_list"),
    path("permission/<int:nid>/del/", permission_views.permission_del, name="permission_del"),
    path('permission/add/', permission_views.permission_add, name="permission_add"),
    path('permission/<int:nid>/modify/', permission_views.permission_modify, name="permission_modify"),
    path('permission/<int:nid>/reset/', permission_views.permission_reset, name="permission_reset"),
    # path('permission/create/', assets_views.create_assets, name=""),
]

login_urlpatterns = [
    path('login/', login_views.login_views, name='login_views'),
    path('signup/', login_views.signup_views, name='signup'),  # 新增 signup 路由
]

urlpatterns =  [
    *index_urlpatterns,
    *depart_urlpatterns,
    *employee_urlpatterns,
    *assets_urlpatterns,
    *permission_urlpatterns,
    *login_urlpatterns,
    ]
