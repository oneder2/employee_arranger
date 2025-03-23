from django.shortcuts import redirect, render
from app_one import models
from app_one.utils.page_data import PageData

# index page (main page)
def index(request):
    return render(request, "index/index.html") 

# page showing information about departments
def depart_list(request):
    queryset = models.Department.objects.all()
    page_object = PageData(request=request, 
                           queryset=queryset,
                           page_size=10,
                           edge=1
                           )

    dict_data_list = {
        "data_list": page_object.get_queryset(),
        "page_html": page_object.get_pagehtml()
        }

    return render(request, "depart/depart_list.html", dict_data_list)

# page to add departments
def depart_add(request):
    if request.method == "GET":
        title = "Add info"
        return render(request, "depart/depart_edit.html", {'title':title})
    title = request.POST.get("title")
    models.Department.objects.create(title=title)
    return redirect("/depart/")

# MID-page to add departments
def depart_del(request, nid):
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/")

# MID-page to add departments
def depart_modify(request, nid):
    if request.method == "GET":
        title = "Modify info"
        name = models.Department.objects.filter(id=nid).first()
        return render(request, 
                      "depart/depart_edit.html", 
                      {'title':title, 'name':name}
                      )
    title = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect('/depart/')