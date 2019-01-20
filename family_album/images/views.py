from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import DeleteView
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .forms import UploadForm
from .models import Image
import os


def index(request, user_id=None):
    if user_id:
        images = Image.objects.filter(user_id=user_id)
    else:
        images = Image.objects.all()
    # Show 8 contacts per page
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    return render(request, 'index.html', {'images': images})


class UploadView(LoginRequiredMixin, FormView):
    template_name = 'images/upload.html'
    form_class = UploadForm
    success_url = reverse_lazy('images:home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


class DeleteView(DeleteView):
    template_name = 'images/delete.html'
    model = Image
    success_url = reverse_lazy('images:home')

    def get_object(self, queryset=None):
        obj = super(DeleteView, self).get_object()
        path = obj.image.url
        if os.path.exists(path):
            os.remove(path)
        return obj


class DetailView(DetailView):
    context_object_name = 'image'
    queryset = Image.objects.all()
    template_name = 'images/detail.html'
