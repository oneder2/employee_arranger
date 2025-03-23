from django.db import models

# Create your models here.
# department table
class Department(models.Model):
    title = models.CharField(verbose_name="department name", max_length=128)

    def __str__(self):
        return self.title

# employee table
class Employee(models.Model):
    name = models.CharField(verbose_name="name", max_length=32)
    age = models.IntegerField(verbose_name="age")
    gender_choice = (
        (1, "Male"),
        (2, "Female")
    )
    gender = models.SmallIntegerField(verbose_name="gender", choices=gender_choice)
    salary = models.CharField(verbose_name="salary", max_length=32)
    create_time = models.DateField(verbose_name="employed date")
    department = models.ForeignKey(verbose_name="department", 
                                   to="Department", 
                                   to_field="id", 
                                   on_delete=models.SET_NULL, 
                                   null=True, 
                                   blank=True
                                   )
    
    def __str__(self):
        return self.name


class Assets(models.Model):
    phone_num = models.CharField(verbose_name="Phone_num", max_length=11)
    start_code_choice = (
        (1, "has_been_occupied"),
        (2, "not_been_occupied")
    )
    status = models.IntegerField(verbose_name="Usage_condition", choices=start_code_choice)
    create_time = models.DateField(verbose_name="Created_time")
    user = models.ForeignKey(verbose_name="user_name",
                             to="Employee", 
                             to_field="id", 
                             on_delete=models.SET_NULL, 
                             null=True, 
                             blank=True
                             )
    price = models.CharField(verbose_name="Price", max_length=64)


class Permission(models.Model):
    user_name = models.CharField(verbose_name="user_name", max_length=32)
    password = models.CharField(verbose_name="password", max_length=64)
    ROLE_CHOICES = (
        (0, "Visitor"),
        (1, "User"),
        (2, "Root")
    )
    role = models.IntegerField(verbose_name="role", choices=ROLE_CHOICES)

