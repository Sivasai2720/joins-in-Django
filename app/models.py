from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    dlocation=models.CharField(max_length=200)
    def __str__(self):
        return self.dname

class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=80)
    job=models.CharField(max_length=150)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    hiredate=models.DateField()
    sal=models.DecimalField(max_digits=7,decimal_places=2)
    comm=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)


    def __str__(self):
        return self.ename

class SalGrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    lowsal=models.DecimalField(max_digits=7,decimal_places=2)
    highsal=models.DecimalField(max_digits=7,decimal_places=2)

