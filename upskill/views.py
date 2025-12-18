from django.shortcuts import render, get_object_or_404
from .models import Course, Subject, Content
from django.views.generic import ListView
from django.http import HttpRequest, HttpResponse

# Asosiy index sahifa
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("upskill ishlayapti 🚀")

# Index sahifasi ListView orqali
class IndexView(ListView):
    template_name = 'upskill/index.html'
    context_object_name = 'subjects'
    
    def get_queryset(self):
        return Subject.objects.all()

# Kurslar sahifasi, subject_slug ixtiyoriy
def course(request, subject_slug=None):  # <-- None qo‘yildi
    if subject_slug:
        courses = Course.objects.filter(subject__slug=subject_slug)
    else:
        courses = Course.objects.all()
    
    context = {
        'courses': courses.order_by('id'),
    }
    return render(request, 'upskill/course.html', context)

# Kurs detali
def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    related_courses = Course.objects.filter(subject=course.subject).exclude(pk=course.pk)[:3]
    all_subjects = Subject.objects.all()

    context = {
        'course': course,
        'related_courses': related_courses,
        'subjects': all_subjects,
    }
    return render(request, 'upskill/detail.html', context)

def about(request):
    return render(request, 'upskill/about.html')
