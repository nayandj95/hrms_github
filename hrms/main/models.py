from django.db import models
# Create your models here.




class User(models.Model):
    email = models.EmailField(unique=True,blank=False)
    password = models.CharField(max_length=20,blank=False)
    roll_user = models.CharField(max_length=15,blank=False)
    employee_id = models.CharField(max_length=7, blank=False)
    created_tm = models.TimeField(auto_now=True,blank=False)
    created_at = models.DateField(auto_now=True,blank=False)

    def __str__(self):
        return self.email

class User_Data(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,blank=False)
    last_name = models.CharField(max_length=20,blank=True)
    user_name = models.CharField(max_length=20,blank=False)
    j_date = models.DateField(auto_now=False,auto_now_add=True)
    mobile_no = models.CharField(max_length=13,blank=False,default='+91')
    department = models.CharField(max_length=25,blank=False)
    joining_date = models.CharField(max_length=10,blank=False)

    def __str__(self):
        return self.first_name
