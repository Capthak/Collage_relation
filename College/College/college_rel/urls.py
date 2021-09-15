from django.urls import path
from .views import AddLecturerView, AddStudentView, AdddepartmentView, DeleteLecturerView, DeleteStudentView, Search_view, ShowLecturerView, ShowStudentView, UpdateLecturerView, UpdateStudentView,Home_view


urlpatterns=[
    path('adddep/',AdddepartmentView,name='Adddepartment'),
    path('addstu/',AddStudentView,name='Addstudent'),
    path('addlec/',AddLecturerView,name='Addlecturer'),
    path('showstu/',ShowStudentView,name='Showstudent'),
    path('showlec/',ShowLecturerView,name='Showlecturer'),
    path('updatestu/<int:update>',UpdateStudentView,name='Updatestudent'),
    path('updatelecturer/<int:update>',UpdateLecturerView,name='Updatelecturer'),
    path('deletestu/<int:delete>',DeleteStudentView,name='Deletestudent'),
    path('deletelecturer/<int:delete>',DeleteLecturerView,name='Deletelecturer'),
    path('search/',Search_view,name='Search'),
    

    path('/',Home_view, name='home')


]
# path('search/',Search_view,name='Search'),
