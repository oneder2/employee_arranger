from django.shortcuts import redirect, render
from app_one import models
from app_one.utils.page_data import PageData
from django import forms

# page showing information about Employees
def employee_list(request):
    queryset = models.Employee.objects.all()
    page_object = PageData(request=request, 
                           queryset=queryset,
                           page_size=2,
                           edge=1
                           )

    dict_data_list = {
        "data_list": page_object.get_queryset(),
        "page_html": page_object.get_pagehtml()
        }

    return render(request, "employee/employee_list.html", dict_data_list)

# MID-page to add Employees
def employee_del(request, nid):
    models.Employee.objects.filter(id=nid).delete()
    return redirect("/employee/")

# ModelForm
class EmployeeModelForm(forms.ModelForm):
    name = forms.CharField(min_length=2, label="name")

    # extra appended Field
    class Meta:
        model = models.Employee
        #  read Field in sheet
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control"
            }
    
    def __str__(self):
        return super().__str__()
        

def user_add_modelform(request):
    if request.method == "GET":
        content = {
            "form": EmployeeModelForm(),
            "title": "KISS add info"
        }

        return render(request, "employee/employee_modify.html", content)
    
    # accept data from sheet
    form = EmployeeModelForm(data=request.POST)
    # validate if data is valid
    if form.is_valid():
        #  store into database
        form.save()
        return redirect("/employee/")
    
    # if data is invalid
    # 1. back to original page
    # 2. show error info
    return render(request, "employee/employee_modify.html", {"form": form})



def user_modify_modelform(request, nid):
    obj = models.Employee.objects.filter(id=nid).first()
    if request.method == "GET":
        form = EmployeeModelForm(instance=obj)
        title = "KISS modify info"
        content = {
            "form": form,
            "title": title
        }
        return render(request, "employee/employee_modify.html", content)
    
    # accept data from sheet
    form = EmployeeModelForm(data=request.POST, instance=obj)
    # validate if data is valid
    if form.is_valid():
        #  store into database
        form.save()
        return redirect("/employee/")
    