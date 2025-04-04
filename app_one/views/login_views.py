from django.shortcuts import render, redirect
from app_one.utils import pwd_encrypt
from app_one import models
from django.contrib.auth import authenticate, login, get_user_model
from django import forms


# 登录表单
class LoginForm(forms.Form):
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return pwd_encrypt.md5(pwd)


    username = forms.CharField(
        label="username",
        max_length=100,
        widget=forms.TextInput(attrs={'label':'username', 'class': 'form-control', 'placeholder': '请输入用户名'})
    )
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={'label': 'password', 'class': 'form-control', 'placeholder': '请输入密码'})
    )


# 注册表单
class RegisterForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名'})
    )
    password1 = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'})
    )
    password2 = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请再次输入密码'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("两次输入的密码不一致")
        return cleaned_data

# 登录视图
def login_views(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login/login.html", {"form": form})
    
    form = LoginForm(data=request.POST)
    if form.is_valid():
        admin_object = models.Permission.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "wrong username or password")
            return render(request, "login/login.html", {"form": form})

        request.session["info"] = {"id":admin_object.id, 
                                   "username":admin_object.username, 
                                   "password":admin_object.password, 
                                   "role":admin_object.role
                                   }
        
        request.session.set_expiry(60)

        return redirect("/")
    
    return render(request, "login/login.html", {"form": form})

# 注册视图
def signup_views(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "login/register.html", {"form": form})
    
    form = RegisterForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        User = get_user_model()
        if User.objects.filter(username=username).exists():
            form.add_error("username", "该用户名已被占用")
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect("/")
    return render(request, "login/register.html", {"form": form})