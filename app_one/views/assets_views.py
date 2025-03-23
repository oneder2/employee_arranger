from django.core.validators import RegexValidator

from django.core.exceptions import ValidationError

from django.utils.safestring import mark_safe

from app_one.utils.page_data import PageData
from django.http import HttpResponse
from django .shortcuts import redirect, render
from django import forms
from app_one import models

from datetime import datetime
import random

def assets_list(request):
    # dict_data = {"mobile": "what I want to search"}
    dict_data = {}
    # access info in seacrch block
    phone_num_search = request.GET.get("search_phone_num")
    status_search = request.GET.get("search_status")

    if phone_num_search is not None:
        # search data with string in "value"
        dict_data["phone_num__contains"] = phone_num_search

    if status_search is not None:
        # search data with string in "value"
        dict_data["status__contains"] = status_search
    
    queryset = models.Assets.objects.filter(**dict_data)
    asset_page_object = PageData(request=request, 
                           queryset=queryset,
                           page_size=10
                           )
    
    dict_data_list = {
        "data_asset_list": asset_page_object.get_queryset(),
        "page_html": asset_page_object.get_pagehtml()
        }

    return render(request, "assets/asset_list.html", dict_data_list)

class AssetsModelForm(forms.ModelForm):
    phone_num = forms.CharField(
        label="phone_num",
        validators=[RegexValidator(r"^1[3-9]\d{9}", "Please input valid phone num")]
    )
    # # no edit
    # price = forms.CharField(disabled=True, label="price")

    class Meta:
        model = models.Assets
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control"
            }
    
    def clean_phone_num(self): 
        new_phone_num = self.cleaned_data["phone_num"]
        
        # 获取当前实例（如果有的话）
        instance = getattr(self, 'instance', None)

        # 检查新输入的 phone_num 是否已存在
        if_exists = models.Assets.objects.filter(phone_num=new_phone_num).exists()
        if if_exists and instance.phone_num != new_phone_num:
            raise ValidationError("phone# exists")
        
        return new_phone_num

    def __str__(self):
        return super().__str__()


# add information
def assets_add_modelform(request):
    if request.method == "GET":
        content = {
            "form": AssetsModelForm(),
            "title": "KISS add assets"
        }

        return render(request, "assets/asset_modify.html", content)
    
    # accept data from sheet
    form = AssetsModelForm(data=request.POST)
    # validate if data is valid
    if form.is_valid():
        #  store into database
        form.save()
        return redirect("/assets/")
    
    # if data is invalid
    # 1. back to original page
    # 2. show error info
    return render(request, "assets/asset_modify.html", {"form": form})


# modify information
def assets_modify_modelform(request, nid):
    data_list=  models.Assets.objects.filter(id=nid).first()
    title = "KISS add info"
    if request.method == "GET":
        content = {
            "form": AssetsModelForm(instance=data_list),
            "title": title
        }

        return render(request, "assets/asset_modify.html", content)
    
    # accept data from sheet
    form = AssetsModelForm(data=request.POST, instance=data_list)
    # validate if data is valid
    if form.is_valid():
        #  store into database
        form.save()
        return redirect("/assets/")
    
    # if data is invalid
    return render(request, "assets/asset_modify.html", {"form": form, "title": title})

# MID-page to add Employees
def assets_del(request, nid):
    models.Assets.objects.filter(id=nid).delete()
    return redirect("/assets/")

def create_assets(request):
    for _ in range(200):
        phone_num = "133" + str(random.randint(10000000, 99999999))
        
        status = random.randint(1,2)

        now = datetime.now()
        create_time = now.strftime("%Y-%m-%d")
        
        price = random.randint(5000, 7000)
        
        user_id = random.randint(2, 5)
        try:
            print(phone_num, status, create_time, price, user_id)
            models.Assets.objects.create(
                phone_num=phone_num,
                status=status,
                create_time=create_time,
                price=price,
                user_id=user_id,
            )
        except ValidationError:
            print("replicates")
            continue
    return redirect("/assets/")
