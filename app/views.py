from django.shortcuts import render
from app.models import *
# Create your views here.

def equijoins(request):

    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=1981)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__gt=1250)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True,sal__lt=1250)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()

    #------For Writing Conditions-------
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename='SMITH')   #syn--> Col name= value,   which do u want, when u writing condtion for Child table
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')  #syn--> CommonColumn__col name which do u want, when u writing condtion for parent table



    #--------For Printing the Data----------
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)    #syn--> obj name.colname,   which do u want, when u printing the data for Child table
    #syn--> Obj name.deptno.Col name, which do u want, when u printing the data for parent table

    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)





