from django.forms import ModelForm
from cust.models import Document

class DocumentForm(ModelForm):
  class Meta:
    model = Document
    fields = ['file_obj']