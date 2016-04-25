from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.template.response import TemplateResponse

from tareas.models import Tarea
from django.http import HttpResponseRedirect

class TareaListView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'tarea_list': Tarea.objects.all()
        }
        return TemplateResponse(request, 'tarea_list.html', context)


class TareaAddView(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request,'tarea_add.html', {})

    def post(self, request, *args, **kwargs):
        descripcion=request.POST['descripcion']
        Tarea.objects.create(descripcion=descripcion)
        return HttpResponseRedirect('/')

class TareaDoneView(View):
    def get(self, request, *args, **kwargs):
        tarea=Tarea.objects.get(id=kwargs['tarea_id'])
        tarea_done=True
        tarea.save()
        return HttpResponseRedirect('/')

