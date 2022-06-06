import os

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User, Group
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from .models import Section, Archives, Profile
from .models import Ads
from .models import Comments
from .forms import NewAdsForm, CommentsForm, SectionUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Count
from django.views.generic import UpdateView, ListView, DeleteView
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def count_Ads(request):
    if (request.user.is_anonymous):
        return None
    else:

        if request.user.is_superuser == True:
            ads = Ads.objects.filter(active='False')
        else:
            ads = Ads.objects.filter(active='False', created_by=request.user)
        countAds = ads.count()
        return countAds


def count_comment(ads):
    comment = Comments.objects.filter(ads=ads)
    countcomment = comment.count()
    return countcomment


def getSection():
    Sections = Section.objects.all()
    return Sections


def home(request):
    adslast = Ads.objects.filter(active='True').order_by('-created_dt')[:10]
    if(request.user.is_anonymous):
        return render(request, 'home.html', {'adslast': adslast, 'getSection': getSection()})
    else :
        print(request.user)
        return render(request, 'home.html',{'adslast': adslast, 'getSection': getSection(), 'countAds': count_Ads(request)})



# @method_decorator(login_required,name='dispatch')
# class SectionListView(ListView):
#     model = Section
#     context_object_name = 'Section'
#     template_name = 'home.html'
#     paginate_by = 6

def SectionAdsSearch(request, section_id):
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
                              {'l': l, 'SectionAll': SectionAll, 'Section': Sections, 'Ads': ads, 'li': listView,
                               'getSection': getSection(),
                               'countAds': count_Ads(request)})
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

                return render(request, 'Ads.html',
                              {'l': l, 'SectionAll': SectionAll, 'Ads': ads, 'li': listView, 'getSection': getSection(),
                               'countAds': count_Ads(request)})
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
                              {'l': l, 'SectionAll': SectionAll, 'Section': Sections, 'Ads': ads, 'li': listView,
                               'getSection': getSection(),
                               'countAds': count_Ads(request)})
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

                return render(request, 'Ads.html',
                              {'l': l, 'SectionAll': SectionAll, 'Ads': ads, 'li': listView, 'getSection': getSection(),
                               'countAds': count_Ads(request)})


def SectionAds(request, section_id):
    SectionAll = Section.objects.all()

    Archive = Archives.objects.filter(save_by=request.user.id)

    if section_id != 0:
        Sections = get_object_or_404(Section, pk=section_id)
        ads = Sections.ads.filter(active='True').order_by('-created_dt').annotate(commentCount=Count('comments'))
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

        if request.user.id:
            user_profile = get_object_or_404(User, pk=request.user.id)

            return render(request, 'Ads.html',
                          {'user_profile': user_profile, 'l': l, 'SectionAll': SectionAll, 'Section': Sections,
                           'Ads': ads, 'li': listView, 'getSection': getSection(), 'countAds': count_Ads(request)})
        else:
            return render(request, 'Ads.html',
                          {'l': l, 'SectionAll': SectionAll, 'Section': Sections, 'Ads': ads, 'li': listView,
                           'getSection': getSection(), 'countAds': count_Ads(request)})

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

        return render(request, 'Ads.html',
                      {'l': l, 'SectionAll': SectionAll, 'Ads': ads, 'li': listView, 'getSection': getSection(),
                       'countAds': count_Ads(request)})

@login_required
def waitingAds(request):
    if request.user.is_superuser == True:
        ads = Ads.objects.filter(active='False').order_by('-created_dt').annotate(commentCount=Count('comments'))
    else:
        ads = Ads.objects.filter(active='False', created_by=request.user).order_by('-created_dt').annotate(
            commentCount=Count('comments'))

    page = request.GET.get('page', 1)
    paginator = Paginator(ads, 5)
    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    return render(request, 'waitingAds.html', {'Ads': ads, 'countAds': count_Ads(request), 'getSection': getSection()})

@login_required
def UserProfile(request, user_id):
    user_profile = get_object_or_404(User, pk=user_id)
    Archive = Archives.objects.filter(save_by=request.user.id, )

    ads = Ads.objects.filter(created_by=user_id, active='True').order_by('-created_dt').annotate(
        commentCount=Count('comments'))
    CountUserAds = ads.count()
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

    return render(request, 'UserProfile.html',
                  {'li': listView, 'l': l, 'Ads': ads, 'CountUserAds': CountUserAds, 'countAds': count_Ads(request),
                   'user_profile': user_profile, 'getSection': getSection()})

@login_required
def saveArchivesAds(request, ads_id, id):
    ads = get_object_or_404(Ads, pk=ads_id)
    Arch = Archives(ads=ads, save_by=request.user)
    Arch.save()

    if id == 0:
        return redirect('SectionAds', ads.section.pk)
    elif id == 1:
        return redirect('UserProfile', ads.created_by.id)
    elif id == 2:
        return redirect('ArchivesAds')
    else:
        return redirect('adsComments', ads.section.pk, ads.pk, 0)

@login_required
def deleteArchivesAds(request, ads_id, id):
    ads = get_object_or_404(Ads, pk=ads_id)
    archive = Archives.objects.filter(ads=ads, )
    archive.delete()

    if id == 0:
        return redirect('SectionAds', ads.section.pk)
    elif id == 1:
        return redirect('UserProfile', ads.created_by.id)
    elif id == 2:
        return redirect('ArchivesAds')
    else:
        return redirect('adsComments', ads.section.pk, ads.pk, 0)

@login_required
def ArchivesAds(request):
    user_profile = get_object_or_404(User, pk=request.user.id)
    Archive = Archives.objects.filter(save_by=request.user.id, ).order_by('-save_dt')
    # adsAll = Ads.objects.filter(active='True',).order_by('-created_dt').annotate(commentCount=Count('comments'))
    ads = Ads.objects.prefetch_related('archivetest').filter(archivetest__save_by=request.user.id).order_by(
        '-archivetest__save_dt').annotate(commentCount=Count('comments'))

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
                  {'li': listView, 'l': l, 'Ads': ads, 'CountUserAds': CountUserAds, 'countAds': count_Ads(request),
                   'user_profile': user_profile, 'getSection': getSection()})

@login_required
def Accept(request, ads_id):
    if request.user.is_staff:
        ads = get_object_or_404(Ads, pk=ads_id)
        ads.active = 'True'
        ads.save()
        return redirect('waitingAds')
    else:
        return redirect('home')

@login_required
def Rejection(request, ads_id):
    if request.user.is_superuser:
        ads = get_object_or_404(Ads, pk=ads_id)
        ads.delete()
        return redirect('waitingAds')
    else:
        return redirect('home')

@login_required
def BandUserAds(request, section_id, user_id, id):
    user = User.objects.filter(id=user_id).first()
    if user and request.user.is_superuser:
        try:
            group = Group.objects.get(name='user')
            group.user_set.remove(user)
            # user.is_active = False
            # user.save()
        except:
            pass

        return redirect('SectionAds', section_id=section_id)
    else:
        return redirect('home')

@login_required
def BandUserComment(request, section_id, ads_id, user_id):
    user = User.objects.filter(id=user_id).first()
    if user and request.user.is_staff:
        try:
            user.is_active = False
            user.save()
        except:
            pass

        return redirect('adsComments', section_id=section_id, ads_id=ads_id)
    else:
        return redirect('home')


@login_required
def DeleteAds(request, section_id, ads_id, id):
    ads = get_object_or_404(Ads, pk=ads_id)
    if request.user.is_staff or request.user == ads.created_by:
        ads.delete()
        if id == 0:
            return redirect('SectionAds', section_id=section_id)
        elif id == 1:
            return redirect('UserProfile', ads.created_by.id)
        else:
            return redirect('ArchivesAds')

    else:
        return redirect('home')


@login_required
# @permission_required('AdsBoard.add_ads',login_url='login/',raise_exception=True)
def newAds(request, section_id):
    Sections = get_object_or_404(Section, pk=section_id)
    if request.method == "POST":

        form = NewAdsForm(request.POST, )
        if form.is_valid():
            ads = form.save(commit=False)
            ads.section = Sections
            # ads.messageAds=form.cleaned_data.get('message')
            ads.created_by = request.user

            if len(request.FILES) != 0:
                ads.img = request.FILES['img']

            ads.save()
            # comment = Comments.objects.create(
            #     message = form.cleaned_data.get('message'),
            #     created_by = request.user,
            #     ads = ads
            # )
            return redirect('SectionAds', section_id=Sections.pk)

    else:
        form = NewAdsForm()

    return render(request, 'newAds.html', {'Section': Sections, 'form': form})


@login_required
def adsComments(request, section_id, ads_id, id):
    ads = get_object_or_404(Ads, section__pk=section_id, pk=ads_id, )
    # ads = Ads.objects.get(pk=ads_id,active='True').annotate(commentCount=Count('comments'))

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
    if not request.session.get(session_key, False):
        ads.views += 1
        ads.save()
        request.session[session_key] = True

    listView = [""]
    session_key = 'view_ads_{}'.format(ads.pk)
    if not request.session.get(session_key, False):
        listView.append(ads.pk)

    l = [""]
    for ar in Archive:
        if ads.pk == ar.ads.pk:
            l.append(ads.pk)

    idpage = id
    return render(request, 'adsComments.html',
                  {'l': l, 'li': listView, 'Ads': ads, 'comments': comments, 'idpage': idpage,
                   'count_comment': count_comment(ads), 'countAds': count_Ads(request), 'getSection': getSection()})


@login_required
def replyAds(request, section_id, ads_id, id):
    ads = get_object_or_404(Ads, section__pk=section_id, pk=ads_id, )
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.ads = ads
            comments.created_by = request.user
            comments.save()

            return redirect('adsComments', section_id=section_id, ads_id=ads_id, id=id)
    else:
        form = CommentsForm()
    return render(request, 'replyAds.html', {'Ads': ads, 'form': form})


@method_decorator(login_required, name='dispatch')
class SectionEditView(UpdateView):
    model = Section
    form_class = SectionUpdateForm
    template_name = 'editSection.html'
    pk_url_kwarg = 'section_id'
    context_object_name = 'section'

    def form_valid(self, form):
        section = form.save(commit=True)
        section.save()
        return redirect('home', )


@method_decorator(login_required, name='dispatch')
class AdsUpdateView(UpdateView):
    model = Ads
    form_class = NewAdsForm
    template_name = 'editAds.html'
    pk_url_kwarg = 'ads_id'
    context_object_name = 'ads'

    def form_valid(self, form, **kwargs):
        id = self.kwargs['id']

        ads = form.save(commit=True)
        ads.updated_by = self.request.user
        ads.updated_dt = timezone.now()
        ads.save()
        if self.kwargs['id'] == 0:
            return redirect('SectionAds', section_id=ads.section.pk)
        elif self.kwargs['id'] == 1:
            return redirect('UserProfile', ads.created_by.id)
        elif self.kwargs['id'] == 2:
            return redirect('ArchivesAds')
        elif self.kwargs['id'] == 3:
            return redirect('adsComments', section_id=ads.section.pk, ads_id=ads.pk, id=id)
        elif self.kwargs['id'] == 4:
            return redirect('waitingAds')
        else:
            return redirect('home')


@method_decorator(login_required, name='dispatch')
class CommentUpdateView(UpdateView):
    model = Comments
    form_class = CommentsForm
    template_name = 'editComment.html'
    pk_url_kwarg = 'comment_id'
    context_object_name = 'comment'

    def form_valid(self, form, **kwargs):
        id = self.kwargs['id']
        comment = form.save(commit=False)
        comment.updated_by = self.request.user
        comment.updated_dt = timezone.now()
        comment.save()
        return redirect('adsComments', section_id=comment.ads.section.pk, ads_id=comment.ads.pk, id=id)


def CommentDelete(request, section_id, ads_id, comment_id, id):
    comment = get_object_or_404(Comments, pk=comment_id)
    if request.user.is_staff or request.user == comment.created_by:
        comment.delete()
        return redirect('adsComments', section_id=comment.ads.section.pk, ads_id=comment.ads.pk, id=id)
    else:
        return redirect('home')


def listuser(request, user_type):
    name = None
    if 'Search' in request.GET:
        name = request.GET['Search']
        if name:
            if user_type == 0:
                listuser = User.objects.filter(first_name__icontains=name).order_by('first_name')
            elif user_type == 1:
                listuser = User.objects.filter(is_superuser='True', first_name__icontains=name).order_by('first_name')
            elif user_type == 2:
                listuser = User.objects.filter(is_staff='True', first_name__icontains=name).order_by('first_name')
            elif user_type == 3:
                listuser = User.objects.filter(is_staff='False', is_superuser='False',
                                               first_name__icontains=name).order_by('first_name')
        else:
            listuser = User.objects.all().order_by('first_name')
    else:
        if user_type == 0:
            listuser = User.objects.all().order_by('first_name')
        elif user_type == 1:
            listuser = User.objects.filter(is_superuser='True').order_by('first_name')
        elif user_type == 2:
            listuser = User.objects.filter(is_staff='True').order_by('first_name')
        elif user_type == 3:
            listuser = User.objects.filter(is_staff='False', is_superuser='False').order_by('first_name')

    # usertype =Members.objects.raw('select * from User')

    page = request.GET.get('page', 1)
    paginator = Paginator(listuser, 5)
    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    return render(request, 'Users.html', {'userCount': listuser.count(), 'user_type': user_type, 'listuser': listuser,
                                          'getSection': getSection(), 'countAds': count_Ads(request)})


@method_decorator(login_required, name='dispatch')
class usersEditView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']
    template_name = 'edituser.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'users'

    def form_valid(self, form):
        users = form.save(commit=True)
        users.save()
        return redirect('listuser', 0)



# @login_required
# def EditeUser(request):
#     subject = None
#     if 'user_id' in request.GET:
#         subject = request.GET['user_id']
#         print(subject)
#         if subject:
#             if request.method == 'GET':
#                 form = EditeUserForm(request.GET, instance=request.GET['user_id'])
#
#                 if form.is_valid():
#                     form.save()
#                     # messages.success(request, 'Your profile is updated successfully')
#                     return redirect(to='EditeUser')
#             else:
#                 form = EditeUserForm(instance=request.GET['user_id'])
#
#             return render(request, 'edituser.html', {'form': form, })
#         else:
#             return redirect('home')
#     else:
#         return redirect('home')


# def get_Profile_id(user_id):
#     profile_id = Profile.objects.filter(user_id = user_id).first()
#     print(profile_id.id)
#     return profile_id.id
#

# def update_Profile_view0(request, user_id):
#     context = {}
#     id = get_Profile_id(user_id)
#     print(id.id)
#     obj = get_object_or_404(Profile, id=id)
#
#     form = ProfileUpdateForm(request.POST or None, instance=obj)
#
#     if form.is_valid():
#         form.save()
#         return redirect('update_Profile_view',context)
#
#     context["form"] = form
#
#     return render(request, "ProfileUpdate.html", context)
#
# def update_Profile_view(request, user_id):
#
#     profile_id = Profile.objects.filter(id=id).first()
#
#     data = get_object_or_404(Profile, id=user_id)
#
#     form = ProfileUpdateForm(instance=data)
#
#     if request.method == "POST":
#         form = ProfileUpdateForm(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
#             return redirect ('home')
#     context = {
#         "form":form
#     }
#     return render(request, 'ProfileUpdate.html', context)
#
# @method_decorator(login_required,name='dispatch')
# class ProfileUpdateview(UpdateView):
#     model =  Profile
#     form_class = ProfileUpdateForm
#     template_name = 'ProfileUpdate.html'
#     pk_url_kwarg = 'id'
#     context_object_name = 'profile'
#
#     def form_valid(self, form):
#
#         profile = form.save(commit=False)
#         profile.save()
#         return redirect('ProfileUpdate',self.id)
