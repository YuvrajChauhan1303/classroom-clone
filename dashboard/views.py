from django.shortcuts import render, redirect
from helpers import random_str
from itertools import chain

from .models import Classroom, StudentClassroom, TeacherClassroom

# Create your views here.
def view_all_classroom(request):
    s = StudentClassroom.objects.filter(user=request.user).all()
    t = TeacherClassroom.objects.filter(user=request.user).all()
    classroom = list(chain(s, t))

    print(f"Classrooms: {classroom}")

    return render(request, "dashboard/index.html", {
        "classrooms": classroom
    })

def create_classroom(request):
    if request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["desc"]
        join_code = random_str(7)

        cls = Classroom.objects.create(title=title, desc=desc, owner=request.user, join_code=join_code)
        TeacherClassroom.objects.create(user=request.user, classroom=cls)
        return redirect("/")
    
    else:
        return render(request, "dashboard/create.html")