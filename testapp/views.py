from django.shortcuts import render
from testapp.models import Student

# Create your views here.
def student_view(request):
    student_list = Student.objects.all()
    # student_list = Student.objects.filter(marks__It=35)
    # student_list = Student.objects.filter(name__startswith='A')
    # student_list = Student.objects.all().order_by('marks')
    # student_list = Student.objects.all().order_by('-marks')
    my_dict = {'student_list':student_list}
    return render(request,'mytest/std.html',my_dict)
