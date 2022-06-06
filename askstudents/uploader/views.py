from pathlib import Path

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
import openpyxl

from django.conf import settings
from django.conf.urls.static import static
from .models import Upload

class UploadView(CreateView):
    model = Upload
    fields = ['upload_file', ]
    success_url = reverse_lazy('fileupload')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Upload.objects.all()[:1]
        result_str = list()
        for document in context['documents']:
            xslx_file = document.upload_file.name
            wb_obj = openpyxl.load_workbook(Path(settings.MEDIA_ROOT,xslx_file))
            sheet = wb_obj.active
            for row in sheet.iter_rows(max_row=6):
                temp_str = ''
                for cell in row:
                    if type(cell.value) == type(''):
                        temp_str += cell.value + ' '
                result_str.append(temp_str)
        context['result_str'] = result_str
        return context

