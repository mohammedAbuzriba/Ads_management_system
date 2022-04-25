from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Section
from .models import Comments
from .forms import NewAdsForm
# Create your views here.

def home(request):
    Sections = Section.objects.all()
    return render(request,'home.html',{'Section':Sections})


def SectionAds(request,section_id):
    # try:
    #     Sections = Section.objects.get(pk=section_id)
    # except Section.DoesNotExist:
    #     raise Http404
    Sections = get_object_or_404(Section,pk=section_id)
    return render(request,'Ads.html',{'Section':Sections})


def newAds(request, section_id):
    Sections = get_object_or_404(Section,pk=section_id)
    user = User.objects.first()
    if request.method == "POST":
        form = NewAdsForm(request.POST)
        if form.is_valid():
            ads = form.save(commit=False)
            ads.section = Sections
            ads.created_by = user
            ads.save()
            comment = Comments.objects.create(
                message = form.cleaned_data.get('message'),
                created_by = user,
                ads = ads
            )
            return redirect('SectionAds',section_id=Sections.pk)
    else:
        form = NewAdsForm()

    return render(request,'newAds.html',{'Section':Sections,'form':form})
