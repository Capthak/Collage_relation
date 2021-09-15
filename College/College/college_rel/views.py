from django.http import request
from django.shortcuts import redirect, render
from .models import Student,Department,Lecturer
from .forms import Departmentform, Studentform,Lecturerform
from django.contrib import messages


def AdddepartmentView(request):
    form=Departmentform()
    if request.method == 'POST':
        form=Departmentform(request.POST)
        if form.is_valid():
            dep=request.POST.get('depname')
            dep1=Department.objects.filter(depname=dep).first()
            print(dep1)
            if dep1 is not None:
                messages.error(request,'Department is already present')
                return redirect('Adddepartment')
            form.save()
            return redirect('Adddepartment')
    template_name='adddepartment.html'
    context={'form':form}
    return render(request,template_name,context)

def AddStudentView(request):
    form=Studentform()
    if request.method == 'POST':
        form=Studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Addstudent')
    template_name='addstudent.html'
    context={'form':form}
    return render(request,template_name,context)

def AddLecturerView(request):
    form=Lecturerform()
    if request.method == 'POST':
        form=Lecturerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Addlecturer')
    template_name='addlecturer.html'
    context={'form':form}
    return render(request,template_name,context)

def ShowStudentView(request):
    stu=Student.objects.all()
    template_name='showstudent.html'
    context={'stu':stu}
    return render(request,template_name,context)

def ShowLecturerView(request):
    stu=Lecturer.objects.all()
    template_name='showlecturer.html'
    context={'stu':stu}
    return render(request,template_name,context)

def UpdateStudentView(request,update):
    stu=Student.objects.get(id=update)
    form=Studentform(instance=stu)
    if request.method == 'POST':
        form=Studentform(request.POST,instance=stu)
        if form.is_valid():
            form.save()
            return redirect('Showstudent')
    template_name='addstudent.html'
    context={'form':form}
    return render(request,template_name,context)

def UpdateLecturerView(request,update):
    lec=Lecturer.objects.get(id=update)
    form=Lecturerform(instance=lec)
    if request.method == 'POST':
        form=Lecturerform(request.POST,instance=lec)
        if form.is_valid():
            form.save()
            return redirect('Showlecturer')
    template_name='addlecturer.html'
    context={'form':form}
    return render(request,template_name,context)

def DeleteStudentView(request,delete):
    stu=Student.objects.get(id=delete)
    stu.delete()
    return redirect('Showstudent')

def DeleteLecturerView(request,delete):
    stu=Lecturer.objects.get(id=delete)
    stu.delete()
    return redirect('Showlecturer')

# def Searchview(request):
#     if request.method == 'POST':
#         radio=request.POST.get('dep')
#         if radio == 'Department':
#             search=request.POST.get('search')
#             dep_obj=Department.objects.filter(depname=search).first()
            
#             dep_id=dep_obj.id
#             lecresult=Lecturer.objects.filter(department=dep_id)
#             sturesult=Student.objects.filter(department_id=dep_id)
#             template_name='DeparmentSearch.html'
#             context={'lecresult':lecresult,'sturesult':sturesult}
#             return render(request,template_name,context)
            

#         elif radio == 'Student':
#             search=request.POST.get('search')
#             sturesult=Student.objects.filter(stuname=search)
#             template_name='StudentSearch.html'
#             context={'sturesult':sturesult}
#             return render(request,template_name,context)

#         elif radio == 'Lecturer':
#             search=request.POST.get('search')
#             lecresult=Lecturer.objects.filter(lecname=search)
#             template_name='LectureSearch.html'
#             context={'lecresult':lecresult}
#             return render(request,template_name,context)


#     template_name='search.html'
#     context={}
#     return render(request,template_name,context)

def Search_view(request):
    if request.method=='POST':
        search=request.POST.get('search')
        stu=Student.objects.filter(stuname__contains=search)
        lec=Lecturer.objects.filter(lecname__contains=search)
        dep=Department.objects.filter(depname__contains=search).first()
        print(dep)
        if dep is not None:
            stu_dep=Student.objects.filter(department_id=dep)
            lec_dep=Lecturer.objects.filter(department=dep.id)
            template_name='isearch.html'
            context={'stu_dep':stu_dep,'lec_dep':lec_dep,'dep':dep}
            return render(request,template_name,context)
        template_name='isearch.html'
        context={'stu':stu,'lec':lec}
        return render(request,template_name,context)
    template_name='isearch.html'
    cd='else'
    context={'cd':cd}
    return render(request,template_name,context)

def Home_view(request):
    template_name='Home.html'
    context={}
    return render(request,template_name,context)


