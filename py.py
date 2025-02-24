
@ -6,6 +6,7 @@ from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from django.db.models import Q

from student_management_app.models import CustomUser, Staffs, Courses, Subjects, Students, SessionYearModel, FeedBackStudent, FeedBackStaffs, LeaveReportStudent, LeaveReportStaff, Attendance, AttendanceReport
from .forms import AddStudentForm, EditStudentForm
@ -133,6 +134,20 @@ def edit_staff(request, staff_id):
    
    return render(request, "hod_template/edit_staff_template.html", context)

def search_staff(request):
    query = request.GET.get('query')
    staffs = Staffs.objects.filter(
        Q(admin__first_name__icontains=query) |
        Q(admin__last_name__icontains=query) |
        Q(admin__email__icontains=query) |  
        Q(address__icontains=query) 
        
    )
    context = {
        'staffs': staffs,
        'query': query,
    }
    return render(request, 'hod_template/manage_staff_template.html', context)

def edit_staff_save(request):
    if request.method != "POST":
@ -167,7 +182,6 @@ def edit_staff_save(request):
            return redirect('/edit_staff/'+staff_id)



def delete_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    try:
@ -380,7 +394,20 @@ def add_student_save(request):
                return redirect('add_student')
        else:
            return redirect('add_student')

def search_student(request):
    query = request.GET.get('query')
    students = Students.objects.filter(
        Q(admin__first_name__icontains=query) |
        Q(admin__last_name__icontains=query) |
        Q(admin__email__icontains=query) |
        Q(address__icontains=query) |
        Q(course_id__course_name__icontains=query)
    )
    context = {
        'students': students,
        'query': query,
    }
    return render(request, 'hod_template/manage_student_template.html', context)

def manage_student(request):
    students = Students.objects.all()
