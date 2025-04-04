from django.shortcuts import render, redirect, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class AuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info in ["/login/"]:
            return 
        
        info_dict = request.session.get("info")
        if info_dict:
            request.unicom_id = info_dict["id"]
            request.unicom_username = info_dict["username"]
            request.unicom_role = info_dict["role"]
            return 
        
        return redirect("/login/")
    
    def process_view(self, request, view_func, args, kwargs):
        if request.path_info in ["/login/", "/logout/"]:
            return 
        
        role = request.unicom_role

        user_permission_list = settings.UNICOM_PERMISSION[role]

        # Current domain requested is not comtained
        if request.resolver_match.url_name not in user_permission_list:
            return 
        return HttpResponse("Access Denied")