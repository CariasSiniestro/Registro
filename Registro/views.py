from django.shortcuts import render
from django.http import HttpResponse 
from django.http import HttpResponseRedirect

from Registro.models import *

def Rifa(request):
	import random
	Premios=Price.objects.filter(status=False)

	Persona=list(Student.objects.filter(assistence=True, solvence=True, Winner=False))
    
	random.shuffle(Persona)
	
	if request.method == 'POST': 
		if request.POST.get('Seleccion',''):
			ID=request.POST['id']	#es el ID del alumno que ganó
			Student.objects.filter(id=ID).update(Winner=True)
			Student.objects.filter(id=ID).update(Price_Winned=request.POST['Seleccion'])#'Seleccion' trae elID del premio
			if Price.objects.get(id=request.POST['Seleccion']).description!='Ninguno':
				Price.objects.filter(id=request.POST['Seleccion']).update(status=True)
            
			return HttpResponseRedirect('/admin/') 

	if Persona:
		return render(request, 'rifa.html',{'Student':Persona[0],'Prices':Premios}) 
	else:
		return HttpResponseRedirect('/admin/') 

