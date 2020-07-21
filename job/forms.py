from django import forms

from .models import Apply,Job
from ckeditor.widgets import CKEditorWidget

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields=['name','email','website','cv','cover_letter']

class JobForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model=Job
        fields = '__all__'
        exclude = ('slug','owner')