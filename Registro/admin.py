from django.contrib import admin
from Registro.models import *

# Register your models here.

class PriceAdmin(admin.ModelAdmin):
	list_display=['__unicode__','order','status']

class WorkShopAdmin(admin.ModelAdmin):
	list_display=['__unicode__','manager','max_capacity','registered']

class StudentAdmin(admin.ModelAdmin):
	actions = ['Ok_assistence']

	search_fields = ['first_name', 'last_name'] #segundo_nombre
	list_filter = ['solvence']
	list_display = ['__unicode__', 'id','licence','assistence','Workshop_assigned','solvence','Payment','Winner','Price_Winned']

	#acciones
	def Ok_assistence(self, request, queryset):
		if queryset.filter(solvence=True):
			for row in queryset.filter(assistence=False):
				self.log_change(request, row,'Marcar Asistencia')
				rows_updated = queryset.update(assistence=True)
				if rows_updated == 1:
					message_bit = "1 alumno marcado"
				else:
					message_bit = "%s alumnos fueron marcados" % rows_updated
				self.message_user(request, "%s con asistencia exitosa" % message_bit)
		else:
			self.message_user(request,"Imposible marcar asistencia, Alumno no solvente")
	Ok_assistence.short_description = 'Marcar Asistencia'

	

admin.site.register(Student,StudentAdmin)
admin.site.register(Workshop,WorkShopAdmin)
admin.site.register(Price,PriceAdmin)
