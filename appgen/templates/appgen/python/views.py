from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

{{ model_import }}


class {{ model_name }}List(ListView):
    model = {{ model_name }}


class {{ model_name }}Create(CreateView):
    model = {{ model_name }}
    fields = ({% for field in field_names %}'{{ field }}', {% endfor %})


class {{ model_name }}Update(UpdateView):
    model = {{ model_name }}
    fields = ({% for field in field_names %}'{{ field }}', {% endfor %})


class {{ model_name }}Delete(DeleteView):
    model = {{ model_name }}
