from django import forms
from app_one import models
from django.core.exceptions import ValidationError
from app_one.utils import pwd_encrypt


class PermissionModelForm(forms.ModelForm):
    """添加信息验证表格"""
    new_password = forms.CharField(label="RE-input_password", widget=forms.PasswordInput)

    class Meta:
        model = models.Permission
        fields = ["id", "username", "password", "new_password", "role"]
        widgets = {
            "password": forms.PasswordInput
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control"
            }
    
    def clean_username(self): 
        new_username = self.cleaned_data["username"]
        
        # 获取当前实例（如果有的话）
        instance = getattr(self, 'instance', None)

        # 检查新输入的 username 是否已存在
        if_exists = models.Permission.objects.filter(username=new_username).exists()
        if if_exists and instance.username != new_username:
            raise ValidationError("username# exists")
        return new_username        
    
    def clean_password(self):
        """获取MD5加密原密码"""
        pwd = self.cleaned_data.get("password")
        # print(pwd)
        return pwd_encrypt.md5(pwd)
    
    def clean_new_password(self):
        """获取MD5加密之后的原密码，以及重新输入的密码"""
        new_pwd = pwd_encrypt.md5(self.cleaned_data.get("new_password"))
        pwd = self.cleaned_data.get("password")
        if pwd != new_pwd:
            raise ValidationError("passwords are not same")
        return new_pwd

    def __str__(self):
        return super().__str__()
    

class AdminModifyModelForm(forms.ModelForm):
    """修改信息验证表格"""
    class Meta:
        model = models.Permission
        fields = ["username", "role"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control"
            }

    def clean_username(self): 
        new_username = self.cleaned_data["username"]
        
        # 获取当前实例（如果有的话）
        instance = getattr(self, 'instance', None)

        # 检查新输入的 username 是否已存在
        if_exists = models.Permission.objects.filter(username=new_username).exists()
        if if_exists and instance.username != new_username:
            raise ValidationError("username# exists")
        return new_username
    

class AdminResetModelForm(forms.ModelForm):
    """修改密码"""
    new_second_password = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = models.Permission
        fields = ["password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control"
            }
    
    def clean_password(self):
        """获取MD5加密原密码"""
        pwd = self.cleaned_data.get("password")
        print(pwd)
        return pwd_encrypt.md5(pwd)
    
    def clean_new_second_password(self):
        """获取MD5加密之后的原密码，以及重新输入的密码"""
        new_pwd = pwd_encrypt.md5(self.cleaned_data.get("new_second_password"))
        pwd = self.cleaned_data.get("password")
        print(pwd)
        print(new_pwd)
        if pwd != new_pwd:
            raise ValidationError("passwords are not same")
        return new_pwd

    def __str__(self):
        return super().__str__()

