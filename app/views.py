from django.shortcuts import render

# Create your views here.
from app.models import *

def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__gte=1500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='RESEARCH')
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='CHICAGO')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='RESEARCH',hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)


def selfjoins(request):
    empmgrobjects=Emp.objects.select_related('mgr').all()
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__gte=1500)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__deptno=20)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__deptno=10,hiredate__year=2024)
    empmgrobjects=Emp.objects.select_related('mgr').filter(comm__isnull=True)
    #empmgrobjects=Emp.objects.select_related('mgr').all()
    empmgrobjects=Emp.objects.select_related('mgr').filter(comm__gte=100)
    empmgrobjects=Emp.objects.select_related('mgr').filter(hiredate__day=30)
    empmgrobjects=Emp.objects.select_related('mgr').filter(ename__contains='A')
    #empmgrobjects=Emp.objects.select_related('mgr').all()
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename__contains='A')
    #empmgrobjects=Emp.objects.select_related('mgr').all()
    empmgrobjects=Emp.objects.select_related('mgr').filter(ename__startswith='J')
    empmgrobjects=Emp.objects.select_related('mgr').filter(job='MANAGER')
    empmgrobjects=Emp.objects.select_related('mgr').filter(hiredate__year=2023)
    empmgrobjects=Emp.objects.select_related('mgr').filter(job__endswith='R')
    empmgrobjects=Emp.objects.select_related('mgr').filter(hiredate__month=1)
    empmgrobjects=Emp.objects.select_related('mgr').filter(hiredate__month=1,deptno=20)
    empmgrobjects=Emp.objects.select_related('mgr').all()
    d={'empmgrobjects':empmgrobjects}
    return render(request,'selfjoins.html',d)
