import os

from django.contrib.auth.models import User,Group
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from .models import Section,Archives
from .models import Ads
from .models import Comments
from .forms import NewAdsForm,CommentsForm
from django.contrib.auth.decorators import login_required , permission_required
from django.db.models import Count
from django.views.generic import UpdateView, ListView, DeleteView
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def count_Ads():
    ads = Ads.objects.filter(active='False')
    countAds = ads.count()
    return countAds


def home(request):
    Sections = Section.objects.all()
    adslast = Ads.objects.filter(active='True').order_by('-created_dt')[:10]
    return render(request,'home.html',{'adslast':adslast,'Section':Sections,'countAds':count_Ads()})

#@method_decorator(login_required,name='dispatch')
# class SectionListView(ListView):
#     model = Section
#     context_object_name = 'Section'
#     template_name = 'home.html'
#     paginate_by = 6

def SectionAdsSearch(request,section_id):
    SectionAll = Section.objects.all()
    Archive = Archives.objects.filter(save_by=request.user.id)

    subject = None
    if 'Search' in request.GET:
        subject = request.GET['Search']
        if subject:
            if section_id != 0:
                Sections = get_object_or_404(Section, pk=section_id)
                ads = Sections.ads.filter(active='True', subject__icontains=subject).order_by('-created_dt').annotate(
                    commentCount=Count('comments'))
                page = request.GET.get('page', 1)
                paginator = Paginator(ads, 5)
                try:
                    ads = paginator.page(page)
                except PageNotAnInteger:
                    ads = paginator.page(1)
                except EmptyPage:
                    ads = paginator.page(paginator.num_pages)

                listView = [""]
                for a in ads:
                    session_key = 'view_ads_{}'.format(a.pk)
                    if not request.session.get(session_key, False):
                        listView.append(a.pk)
                l = [""]
                for ar in Archive:
                    for a in ads:
                        if a.pk == ar.ads.pk:
                            l.append(a.pk)

                return render(request, 'Ads.html',
                              {'l':l,'SectionAll': SectionAll, 'Section': Sections, 'Ads': ads, 'li': listView,
                               'countAds': count_Ads()})
            else:
                ads = Ads.objects.filter(active='True', subject__icontains=subject).order_by('-created_dt').annotate(
                    commentCount=Count('comments'))
                page = request.GET.get('page', 1)
                paginator = Paginator(ads, 5)
                try:
                    ads = paginator.page(page)
                except PageNotAnInteger:
                    ads = paginator.page(1)
                except EmptyPage:
                    ads = paginator.page(paginator.num_pages)

                listView = [""]
                for a in ads:
                    session_key = 'view_ads_{}'.format(a.pk)
                    if not request.session.get(session_key, False):
                        listView.append(a.pk)

                l = [""]
                for ar in Archive:
                    for a in ads:
                        if a.pk == ar.ads.pk:
                            l.append(a.pk)

                return render(request, 'Ads.html', {'l':l,'SectionAll': SectionAll, 'Ads': ads, 'li': listView,
                                                    'countAds': count_Ads()})
        else:
            if section_id != 0:
                Sections = get_object_or_404(Section, pk=section_id)
                ads = Sections.ads.filter(active='True', subject__icontains=subject).order_by('-created_dt').annotate(
                    commentCount=Count('comments'))
                page = request.GET.get('page', 1)
                paginator = Paginator(ads, 5)
                try:
                    ads = paginator.page(page)
                except PageNotAnInteger:
                    ads = paginator.page(1)
                except EmptyPage:
                    ads = paginator.page(paginator.num_pages)

                listView = [""]
                for a in ads:
                    session_key = 'view_ads_{}'.format(a.pk)
                    if not request.session.get(session_key, False):
                        listView.append(a.pk)

                l = [""]
                for ar in Archive:
                    for a in ads:
                        if a.pk == ar.ads.pk:
                            l.append(a.pk)

                return render(request, 'Ads.html',
                              {'l':l,'SectionAll': SectionAll, 'Section': Sections, 'Ads': ads, 'li': listView,
                               'countAds': count_Ads()})
            else:
                ads = Ads.objects.filter(active='True', subject__icontains=subject).order_by('-created_dt').annotate(
                    commentCount=Count('comments'))
                page = request.GET.get('page', 1)
                paginator = Paginator(ads, 5)
                try:
                    ads = paginator.page(page)
                except PageNotAnInteger:
                    ads = paginator.page(1)
                except EmptyPage:
                    ads = paginator.page(paginator.num_pages)

                listView = [""]
                for a in ads:
                    session_key = 'view_ads_{}'.format(a.pk)
                    if not request.session.get(session_key, False):
                        listView.append(a.pk)

                l = [""]
                for ar in Archive:
                    for a in ads:
                        if a.pk == ar.ads.pk:
                            l.append(a.pk)

                return render(request, 'Ads.html', {'l':l,'SectionAll': SectionAll, 'Ads': ads, 'li': listView,
                                                    'countAds': count_Ads()})



def SectionAds(request,section_id):
    SectionAll = Section.objects.all()

    Archive = Archives.objects.filter(save_by=request.user.id)




    if section_id!=0:
        Sections = get_object_or_404(Section,pk=section_id)
        ads = Sections.ads.filter(active='True').order_by('-created_dt').annotate(commentCount=Count('comments'))
        page = request.GET.get('page',1)
        paginator = Paginator(ads,5)
        try:
            ads = paginator.page(page)
        except PageNotAnInteger:
            ads = paginator.page(1)
        except EmptyPage:
            ads = paginator.page(paginator.num_pages)

        listView=[""]
        for a in ads:
            session_key = 'view_ads_{}'.format(a.pk)
            if not request.session.get(session_key, False):
                listView.append(a.pk)

        l=[""]
        for ar in Archive:
            for a in ads:
                if a.pk == ar.ads.pk:
                    l.append(a.pk)

        if request.user.id:
            user_profile = get_object_or_404(User, pk=request.user.id)

            return render(request,'Ads.html',{'user_profile':user_profile,'l':l,'SectionAll':SectionAll,'Section':Sections,'Ads':ads,'li':listView,'countAds':count_Ads()})
        else:
            return render(request,'Ads.html',{'l':l,'SectionAll':SectionAll,'Section':Sections,'Ads':ads,'li':listView,'countAds':count_Ads()})

    else:
        ads = Ads.objects.filter(active='True').order_by('-created_dt').annotate(commentCount=Count('comments'))
        page = request.GET.get('page', 1)
        paginator = Paginator(ads, 5)
        try:
            ads = paginator.page(page)
        except PageNotAnInteger:
            ads = paginator.page(1)
        except EmptyPage:
            ads = paginator.page(paginator.num_pages)

        listView = [""]
        for a in ads:
            session_key = 'view_ads_{}'.format(a.pk)
            if not request.session.get(session_key, False):
                listView.append(a.pk)

        l = [""]
        for ar in Archive:
            for a in ads:
                if a.pk == ar.ads.pk:
                    l.append(a.pk)



        return render(request, 'Ads.html', {'l':l,'SectionAll': SectionAll, 'Ads': ads, 'li': listView,
                                            'countAds': count_Ads()})


def waitingAds(request):
    if request.user.is_staff:
        ads = Ads.objects.filter(active='False').order_by('-created_dt').annotate(commentCount=Count('comments'))
        page = request.GET.get('page',1)
        paginator = Paginator(ads,5)
        try:
            ads = paginator.page(page)
        except PageNotAnInteger:
            ads = paginator.page(1)
        except EmptyPage:
            ads = paginator.page(paginator.num_pages)

        return render(request,'waitingAds.html',{'Ads':ads,'countAds':count_Ads()})

    else:
        return redirect('home')


def UserProfile(request,user_id):
    user_profile = get_object_or_404(User,pk=user_id)
    Archive = Archives.objects.filter(save_by=request.user.id,)


    ads = Ads.objects.filter(created_by=user_id).order_by('-created_dt').annotate(commentCount=Count('comments'))
    CountUserAds = ads.count()
    page = request.GET.get('page',1)
    paginator = Paginator(ads,5)
    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    l = [""]
    for ar in Archive:
        for a in ads:
            if a.pk == ar.ads.pk:
                l.append(a.pk)
    listView = [""]
    for a in ads:
        session_key = 'view_ads_{}'.format(a.pk)
        if not request.session.get(session_key, False):
            listView.append(a.pk)


    return render(request,'UserProfile.html',{'li': listView,'l':l,'Ads':ads,'CountUserAds':CountUserAds,'countAds':count_Ads(),'user_profile':user_profile})


def saveArchivesAds(request,ads_id,id):
    ads = get_object_or_404(Ads, pk=ads_id)
    Arch = Archives(ads=ads,save_by=request.user)
    Arch.save()

    if id ==0:
        return redirect('SectionAds',ads.section.pk)
    elif id ==1:
        return redirect('UserProfile',ads.created_by.id)
    else:
        return redirect('ArchivesAds')


def deleteArchivesAds(request,ads_id,id):
    ads = get_object_or_404(Ads, pk=ads_id)
    archive = Archives.objects.filter(ads=ads,)
    archive.delete()

    if id ==0:
        return redirect('SectionAds',ads.section.pk)
    elif id ==1:
        return redirect('UserProfile',ads.created_by.id)
    else:
        return redirect('ArchivesAds')


def ArchivesAds(request):
    user_profile = get_object_or_404(User, pk=request.user.id)
    Archive = Archives.objects.filter(save_by=request.user.id,).order_by('-save_dt')
    adsAll = Ads.objects.filter(active='True',).order_by('-created_dt').annotate(commentCount=Count('comments'))
    ads=Ads.objects.prefetch_related('archivetest').filter(archivetest__save_by=request.user.id).order_by('-archivetest__save_dt')

    CountUserAds = len(ads)
    page = request.GET.get('page', 1)
    paginator = Paginator(ads, 5)
    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    l = [""]
    for ar in Archive:
        for a in ads:
            if a.pk == ar.ads.pk:
                l.append(a.pk)

    listView = [""]
    for a in ads:
        session_key = 'view_ads_{}'.format(a.pk)
        if not request.session.get(session_key, False):
            listView.append(a.pk)

    return render(request, 'Archive.html',
                  {'li': listView,'l':l,'Ads': ads, 'CountUserAds': CountUserAds, 'countAds': count_Ads(), 'user_profile': user_profile})


def Accept(request,ads_id):
    if request.user.is_staff:
        ads = get_object_or_404(Ads, pk=ads_id)
        ads.active='True'
        ads.save()
        return redirect('waitingAds')
    else:
        return redirect('home')

def Rejection(request,ads_id):
    if request.user.is_staff:
        ads = get_object_or_404(Ads, pk=ads_id)
        ads.delete()
        return redirect('waitingAds')
    else:
        return redirect('home')

def BandUserAds(request,section_id,user_id,id):
    user = User.objects.filter(id=user_id).first()
    if user and request.user.is_staff:
        try:
            group = Group.objects.get(name='user')
            group.user_set.remove(user)
            user.is_active=False
            user.save()
        except:
            pass

        return redirect('SectionAds',section_id=section_id)
    else:
        return redirect('home')


def BandUserComment(request,section_id,ads_id,user_id):
    user = User.objects.filter(id=user_id).first()
    if user and request.user.is_staff:
        try:
            group = Group.objects.get(name='user')
            group.user_set.remove(user)
            user.is_active=False
            user.save()
        except:
            pass

        return redirect('adsComments', section_id=section_id, ads_id=ads_id)
    else:
        return redirect('home')

@login_required
def DeleteAds(request,section_id,ads_id,id):
    ads = get_object_or_404(Ads, pk=ads_id)
    if request.user.is_staff or request.user == ads.created_by :
        ads.delete()
        if id == 0:
            return redirect('SectionAds',section_id=section_id)
        elif id == 1:
            return redirect('UserProfile', ads.created_by.id)
        else:
            return redirect('ArchivesAds')

    else:
        return redirect('home')


@login_required
#@permission_required('AdsBoard.add_ads',login_url='login/',raise_exception=True)
def newAds(request, section_id):
    Sections = get_object_or_404(Section,pk=section_id)
    if request.method == "POST":
        form = NewAdsForm(request.POST)
        if form.is_valid():
            ads = form.save(commit=False)
            ads.section = Sections
            # ads.messageAds=form.cleaned_data.get('message')
            ads.created_by = request.user

            if len(request.FILES)!=0:
                ads.img=request.FILES['img']

            ads.save()
            # comment = Comments.objects.create(
            #     message = form.cleaned_data.get('message'),
            #     created_by = request.user,
            #     ads = ads
            # )
            return redirect('SectionAds',section_id=Sections.pk)
    else:
        form = NewAdsForm()

    return render(request,'newAds.html',{'Section':Sections,'form':form})

@login_required
def adsComments(request, section_id,ads_id,id):
    ads = get_object_or_404(Ads, section__pk=section_id ,pk=ads_id,)
    Archive = Archives.objects.filter(save_by=request.user.id)
    comments = ads.comments.all().order_by('-created_dt')

    page = request.GET.get('page', 1)
    paginator = Paginator(comments, 5)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    session_key = 'view_ads_{}'.format(ads.pk)
    if not request.session.get(session_key,False):
        ads.views +=1
        ads.save()
        request.session[session_key]=True


    idpage=id
    return render(request, 'adsComments.html', {'Ads': ads,'comments':comments,'idpage':idpage,'countAds':count_Ads()})

@login_required
def replyAds(request, section_id,ads_id,id):

    ads = get_object_or_404(Ads, section__pk=section_id ,pk=ads_id,)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.ads = ads
            comments.created_by = request.user
            comments.save()

            return redirect('adsComments',section_id=section_id, ads_id=ads_id,id=id)
    else:
        form = CommentsForm()
    return render(request, 'replyAds.html',{'Ads':ads,'form':form})


@method_decorator(login_required,name='dispatch')
class SectionEditView(UpdateView):
    model =  Section
    fields = ['name','description','img']
    template_name = 'editSection.html'
    pk_url_kwarg = 'section_id'
    context_object_name = 'section'

    def form_valid(self, form):
        section = form.save(commit=True)
        section.save()
        return redirect('home',)

@method_decorator(login_required,name='dispatch')
class AdsUpdateView(UpdateView):
    model =  Ads
    fields = ['subject','messageAds','img']
    template_name = 'editAds.html'
    pk_url_kwarg = 'ads_id'
    context_object_name = 'ads'


    def form_valid(self, form,**kwargs):
        id = self.kwargs['id']

        ads = form.save(commit=True)
        ads.updated_by = self.request.user
        ads.updated_dt = timezone.now()
        ads.save()
        if self.kwargs['id'] == 0:
            return redirect('SectionAds',section_id=ads.section.pk)
        elif self.kwargs['id'] == 1:
            return redirect('UserProfile', ads.created_by.id)
        elif self.kwargs['id'] == 2:
            return redirect('ArchivesAds')
        elif self.kwargs['id'] == 3:
            return redirect('adsComments', section_id=ads.section.pk, ads_id=ads.pk, id=id)
        else:
            return redirect('home')




@method_decorator(login_required,name='dispatch')
class CommentUpdateView(UpdateView):
    model =  Comments
    fields = {'message',}
    template_name = 'editComment.html'
    pk_url_kwarg = 'comment_id'
    context_object_name = 'comment'

    def form_valid(self, form,**kwargs):
        id = self.kwargs['id']
        comment = form.save(commit=False)
        comment.updated_by = self.request.user
        comment.updated_dt = timezone.now()
        comment.save()
        return redirect('adsComments',section_id=comment.ads.section.pk,ads_id=comment.ads.pk, id=id)


def CommentDelete(request,section_id,ads_id,comment_id,id):
    comment = get_object_or_404(Comments, pk=comment_id)
    if request.user.is_staff or request.user == comment.created_by :
        comment.delete()
        return redirect('adsComments',section_id=comment.ads.section.pk,ads_id=comment.ads.pk, id=id)
    else:
        return redirect('home')




