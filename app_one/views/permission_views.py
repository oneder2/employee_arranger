from django.core.exceptions import ValidationError

from django import forms
from django.shortcuts import redirect, render
from app_one import models
from app_one.utils.page_data import PageData
from app_one.views.forms.permission import PermissionModelForm, AdminModifyModelForm, AdminResetModelForm


def permission_list(request):
    data_list = models.Permission.objects.all()
    page_object = PageData(request=request, queryset=data_list)
    dict_data_list = {
        "data_list": page_object.get_queryset(),
        "page_html": page_object.get_pagehtml()
        }
    
    return render(request, "permission/permission_list.html", dict_data_list)

# MID-page to del permission
def permission_del(request, nid):
    models.Permission.objects.filter(id=nid).delete()
    return redirect("/permission/")


# add information
def permission_add(request):
    title = "KISS add assets"
    if request.method == "GET":
        content = {
            "form": PermissionModelForm(),
            "title": title
        }

        return render(request, "permission/permission_modify.html", content)
    
    # accept data from sheet
    form = PermissionModelForm(data=request.POST)
    # validate if data is valid
    if form.is_valid():
        #  store into database
        form.save()
        return redirect("/permission/")
     
    # if data is invalid
    # 1. back to original page
    # 2. show error info
    return render(request, "permission/permission_modify.html", {"title": title,"form": form})
    
def permission_modify(request, nid):
    title = "modify"
    title_obj = models.Permission.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = AdminModifyModelForm(instance=title_obj)
        content = {
            "title": title,
            "form": form
        }
        return render(request, "permission/permission_modify.html", content)
    form = AdminModifyModelForm(data=request.POST, instance = title_obj)
    if form.is_valid():
        form.save()
        return redirect("/permission/")
    content = {
            "title": title,
            "form": form
        }
    return render(request, "permission/permission_modify.html", content)

def permission_del(request, nid):
    models.Permission.objects.filter(id=nid).delete()
    return redirect("/permission/")

def permission_reset(request, nid):
    title_object = models.Permission.objects.filter(id=nid).first()
    title = f"reset password of <{title_object.username}>"
    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, "permission/permission_modify.html", {"title": title, "form": form})
    
    form = AdminResetModelForm(data=request.POST, instance = title_object)
    if form.is_valid():
        form.save()
        return redirect("/permission/")
    content = {
            "title": title,
            "form": form
        }
    return render(request, "permission/permission_modify.html", content)