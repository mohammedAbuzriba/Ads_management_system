from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from .models import Section
from .models import Ads
from .models import Comments
from .forms import NewAdsForm,CommentsForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

# def home(request):
#     Sections = Section.objects.all()
#     return render(request,'home.html',{'Section':Sections})

class SectionListView(ListView):
    model = Section
    context_object_name = 'Section'
    template_name = 'home.html'

def SectionAds(request,section_id):
    Sections = get_object_or_404(Section,pk=section_id)
    ads = Sections.ads.order_by('-created_dt').annotate(commentCount=Count('comments'))
    page = request.GET.get('page',1)
    paginator = Paginator(ads,10)
    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    return render(request,'Ads.html',{'Section':Sections,'Ads':ads})

@login_required
def newAds(request, section_id):
    Sections = get_object_or_404(Section,pk=section_id)
    if request.method == "POST":
        form = NewAdsForm(request.POST)
        if form.is_valid():
            ads = form.save(commit=False)
            ads.section = Sections
            ads.created_by = request.user
            ads.save()
            comment = Comments.objects.create(
                message = form.cleaned_data.get('message'),
                created_by = request.user,
                ads = ads
            )
            return redirect('SectionAds',section_id=Sections.pk)
    else:
        form = NewAdsForm()

    return render(request,'newAds.html',{'Section':Sections,'form':form})


def adsComments(request, section_id,ads_id):
    ads = get_object_or_404(Ads, section__pk=section_id ,pk=ads_id,)

    sessionKey = 'viewAds_{}'.format(ads.pk)

    if not request.session.get(sessionKey,False):
        ads.views +=1
        ads.save()
        request.session[sessionKey]=True
    return render(request, 'adsComments.html', {'Ads': ads})

@login_required
def replyAds(request, section_id,ads_id):
    ads = get_object_or_404(Ads, section__pk=section_id ,pk=ads_id,)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.ads = ads
            comments.created_by = request.user
            comments.save()

            ads.updated_by=request.user
            ads.updated_dt= timezone.now()
            ads.save()

            return redirect('adsComments',section_id=section_id, ads_id=ads_id)
    else:
        form = CommentsForm()
    return render(request, 'replyAds.html',{'Ads':ads,'form':form})


@method_decorator(login_required,name='dispatch')
class CommentUpdateView(UpdateView):
    model =  Comments
    fields = {'message',}
    template_name = 'editComment.html'
    pk_url_kwarg = 'comment_id'
    context_object_name = 'comment'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.updated_by = self.request.user
        comment.updated_dt = timezone.now()
        comment.save()
        return redirect('adsComments',section_id=comment.ads.section.pk,ads_id=comment.ads.pk)
