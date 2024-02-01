from django.shortcuts import render
from app.models import *
# Create your views here.


from django.db.models import Q


 #--------Dispaly Two tables data-------------
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



#--------Dispaly Self tables data, with relation cols-------------

def selfjoin(request):
    EMobjects=Emp.objects.select_related('mgr').all()
    EMobjects=Emp.objects.select_related('mgr').filter(hiredate__year=1981)
    EMobjects=Emp.objects.select_related('mgr').filter(sal__gt=1250)
    EMobjects=Emp.objects.select_related('mgr').filter(comm__isnull=True)
    EMobjects=Emp.objects.select_related('mgr').filter(comm__isnull=True,sal__lt=1250)
    EMobjects=Emp.objects.select_related('mgr').all()

    #------For Writing Conditions-------
    EMobjects=Emp.objects.select_related('mgr').filter(ename='SMITH')   #syn--> Col name= value,   which do u want, when u writing condtion for Child table
    EMobjects=Emp.objects.select_related('mgr').filter(sal__lte=1500)  



    #--------For Printing the Data----------
    EMobjects=Emp.objects.select_related('mgr').filter(deptno=10)    #syn--> obj name.colname,   which do u want, when u printing the data for Child table
    #syn--> Obj name.deptno.Col name, which do u want, when u printing the data for parent table

    EMobjects=Emp.objects.select_related('mgr').all()

    

    d={'EMobjects':EMobjects}
    return render(request,'selfjoin.html',d)



  #--------Dispaly Three tables data-------------

def emp_mgr_dept(request):

    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('mgr','deptno').filter(ename='ALLEN')
    emd=Emp.objects.select_related('mgr','deptno').filter(ename='SMITH',deptno__dname='ACCOUNTING') #This is a AND operator , diffenitate with comma(,)
    
    emd=Emp.objects.select_related('mgr','deptno').filter(Q(ename='SMITH') | Q(deptno__dname='ACCOUNTING'))#This is a OR operator , 1st import Q and diffenitate with pipe(|)
    emd=Emp.objects.select_related('mgr','deptno').filter(Q(ename='KING') | Q(deptno__dname='RESEARCH'))
    emd=Emp.objects.select_related('mgr','deptno').filter(ename='KING',deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('mgr','deptno').filter(ename='KING',deptno__dname='ACCOUNTING')
    emd=Emp.objects.select_related('mgr','deptno').filter(ename='KING',deptno__deptno='10')
    emd=Emp.objects.select_related('mgr','deptno').filter(ename='KING',deptno='10')
    emd=Emp.objects.select_related('mgr','deptno').filter(ename='KING',deptno__dname='SALES')
    emd=Emp.objects.select_related('mgr','deptno').filter(Q(ename='KING') | Q(deptno__dname='SALES'))



    emd=Emp.objects.select_related('mgr','deptno').filter(Q(ename='KING') | Q(sal__gt=4500)) #king actual salary 5000
    emd=Emp.objects.select_related('mgr','deptno').filter(ename='KING',sal__gt=1000)
    emd=Emp.objects.select_related('mgr','deptno').filter(ename='ALLEN',mgr__ename='BLAKE')
    emd=Emp.objects.select_related('mgr','deptno').filter(ename='KING',deptno__deptno='20')
    emd=Emp.objects.select_related('mgr','deptno').filter(Q(ename='KING') | Q(comm__lte=0))
    emd=Emp.objects.select_related('mgr','deptno').filter(~Q(ename='KING')) #   ~Q is a not EQUALSTO OPERATOR(!=)
    emd=Emp.objects.select_related('deptno','mgr').all()



    d={'emd':emd}
    return render(request,'emp-mgr-dept.html',d)