from django.shortcuts import render
from .models import Project, Technology

def index(request):
    technologies = Technology.objects.all()
    selected_tech_ids = request.GET.getlist('technologies')
    if selected_tech_ids:
        projects = Project.objects.filter(technologies__id__in=selected_tech_ids).distinct()
    else:
        projects = Project.objects.all()

    context = {
        'projects': projects,
        'technologies': technologies,
        'selected_tech_ids': [int(id) for id in selected_tech_ids]
    }
    return render(request, 'portfolio/landing-page.html', context)

def about(request):
    return render(request, 'portfolio/about.html')

def about_website(request):
    return render(request, 'portfolio/about_website.html')