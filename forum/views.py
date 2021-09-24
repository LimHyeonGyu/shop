from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from forum.models import Forum
from forum.forms import forumcreateForm
from django.contrib.auth.mixins import UserPassesTestMixin


class ForumListView(ListView):
    model = Forum
    template_name = 'forum/list.html'


class ForumDetailView(DetailView):
    model = Forum
    template_name = 'forum/detail.html'

class ForumCreateView(CreateView):
    model = Forum
    form_class = forumcreateForm
    template_name = 'forum/add.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()        
        return redirect('home')

class ForumUpdateView(UserPassesTestMixin, UpdateView):
    model = Forum
    form_class = forumcreateForm
    template_name = 'forum/edit.html'
    success_url = '/forum'

    def test_func(self):
        if self.request.user.id == self.author_id:
            return True
        else :
            return redirect('home')

class ForumDeleteView(DeleteView):
    model = Forum
    success_url = '/forum'
