from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView
from web_app.models import RegisterModel, Institute
from members.forms import InstituteRegisterForm, InstituteProfileForm


class InstituteRegisterView(CreateView):
    model = RegisterModel
    template_name = 'institutes/institute_register.html'
    form_class = InstituteRegisterForm

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'institute'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class ShowProfilePage(DetailView):
    model = Institute
    template_name = 'institutes/institute_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePage, self).get_context_data(*args, **kwargs)
        institute_user = get_object_or_404(Institute, user=self.kwargs['pk'])
        context['institute_user'] = institute_user
        return context


class InstituteUpdateProfilePage(UpdateView):
    model = Institute
    form_class = InstituteProfileForm
    template_name = 'institutes/update_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(InstituteUpdateProfilePage, self).get_context_data(*args, **kwargs)
        institute_user = get_object_or_404(Institute, user=self.kwargs['pk'])
        context['institute_user'] = institute_user
        return context
