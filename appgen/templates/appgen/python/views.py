from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import {{ model_name }}Form
from .models import {{ model_name }}


class {{ model_name }}List(ListView):
    model = {{ model_name }}


class {{ model_name }}Detail(DetailView):
    model = {{ model_name }}


class {{ model_name }}Create(CreateView):
    model = {{ model_name }}
    form_class = {{ model_name }}Form
    success_url = reverse_lazy('{{ app_label }}:list')


class {{ model_name }}Update(UpdateView):
    model = {{ model_name }}
    form_class = {{ model_name }}Form
    success_url = reverse_lazy('{{ app_label }}:list')


class {{ model_name }}Delete(DeleteView):
    model = {{ model_name }}
    success_url = reverse_lazy('{{ app_label }}:list')
