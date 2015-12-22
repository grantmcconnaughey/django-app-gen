from django import forms

{{ model_import }}


class {{ model_name }}Form(forms.ModelForm):
    class Meta:
        model = {{ model_name }}
        fields = ({% for field in field_names %}'{{ field }}', {% endfor %})
