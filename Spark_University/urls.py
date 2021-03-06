"""Spark_University URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Spark_University import settings
from django.conf import settings
from student_management_app import views,hodviews,staffviews,studentviews

urlpatterns = [
    path('demo/',views.showDemoPage),
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage, name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),
    path('admin_home',hodviews.admin_home,name="admin_home"),
    path('add_staff',hodviews.add_staff,name="add_staff"),
    path('add_staff_save',hodviews.add_staff_save,name="add_staff_save"),
    path('add_course',hodviews.add_course,name="add_course"),
    path('add_course_save',hodviews.add_course_save,name="add_course_save"),
    path('add_student',hodviews.add_student,name="add_student"),
    path('add_student_save',hodviews.add_student_save,name="add_student_save"),
    path('add_subject',hodviews.add_subject,name="add_subject"),
    path('add_subject_save',hodviews.add_subject_save,name="add_subject_save"),
    path('manage_staff',hodviews.manage_staff,name="manage_staff"),
    path('manage_student',hodviews.manage_student,name="manage_student"),
    path('manage_course',hodviews.manage_course,name="manage_course"),
    path('manage_subject',hodviews.manage_subject,name="manage_subject"),
    path('edit_staff/<str:staff_id>', hodviews.edit_staff,name="edit_staff"),
    path('edit_staff_save', hodviews.edit_staff_save,name="edit_staff_save"),
    path('edit_student/<str:student_id>', hodviews.edit_student,name="edit_student"),
    path('edit_student_save', hodviews.edit_student_save,name="edit_student_save"),
    path('edit_subject/<str:subject_id>', hodviews.edit_subject,name="edit_subject"),
    path('edit_subject_save', hodviews.edit_subject_save,name="edit_subject_save"),
    path('edit_course/<str:course_id>', hodviews.edit_course,name="edit_course"),
    path('edit_course_save', hodviews.edit_course_save,name="edit_course_save"),
    #staff url Path
    path('staff_home', staffviews.staff_home,name="staff_home"),
    path('student_home', studentviews.student_home,name="student_home"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
