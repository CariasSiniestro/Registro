from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Price(models.Model):
    description = models.CharField('Description', max_length=500)
    order = models.CharField('Orden',max_length='10')
    status = models.BooleanField('Estado', default=False, editable=False)
	
    def __unicode__(self):
		return "%s" % (self.description)

    def save(self):
        self.description=self.description.upper()
        super(Price,self).save()


    class Meta:
		db_table = 'Price'
		verbose_name_plural = 'Premios'
		verbose_name = 'Premio'

        

class Workshop(models.Model):
    name = models.CharField('Nombre', max_length=50)
    manager = models.CharField('Encargado', max_length=50)
    max_capacity = models.IntegerField('Capacidad', max_length=5)
    registered = models.IntegerField('Registrados',max_length=5,  editable=False,default=0)


    def __unicode__(self):
        return "%s" % (self.name) 

    def save(self):
        self.name=self.name.upper()
        self.manager=self.manager.upper()
        super(Workshop,self).save()


    class Meta:
        db_table = 'Workshop'
        verbose_name_plural = 'Talleres'
        verbose_name = 'Taller'



class Student(models.Model):
    first_name = models.CharField('Nombre', max_length=75)
    last_name = models.CharField('Apellido', max_length=75)
    licence = models.CharField('Carnet', max_length=75)
    assistence = models.BooleanField('Asistencia', default=False, editable=False)
    solvence = models.BooleanField('Solvente', default=False, editable=False)
    Winner = models.BooleanField('Ganador', default=False, editable=False)
    Payment = models.FloatField('Abono', max_length=10)
    Price_Winned = models.ForeignKey(Price, null=True, blank=True, editable=False)
    Workshop_assigned= models.ForeignKey(Workshop, null=True, blank=True, editable=True)

    def __unicode__(self):
    	return "%s %s" % (self.first_name,self.last_name)


    def clean(self):
    	if self.id is not None:
            saved=Student.objects.get(id=self.id)
            if saved.Workshop_assigned!=self.Workshop_assigned:
                if self.Workshop_assigned.registered==self.Workshop_assigned.max_capacity:
                    raise ValidationError("Cupo lleno")
                else:
                    if saved.Workshop_assigned:
                        saved.Workshop_assigned.registered-=1
                        saved.Workshop_assigned.save()
    	else:
    		if self.Workshop_assigned:
    			if self.Workshop_assigned.registered==self.Workshop_assigned.max_capacity:
    				raise ValidationError("Cupo lleno")
	

    def save(self):
    	if self.Payment==175:
    		self.solvence=True
        else:
            self.solvence=False

        if self.Workshop_assigned:
           self.first_name=self.first_name.upper()
           self.last_name=self.last_name.upper()
    	   self.Workshop_assigned.registered+=1
    	   self.Workshop_assigned.save()
     	
        super(Student,self).save()

    def delete(self):
        if self.Workshop_assigned:
            self.Workshop_assigned.registered-=1
            self.Workshop_assigned.save()
        super(Student,self).delete()

    class Meta:
        db_table = 'Student'
        verbose_name_plural = 'Estudiantes'
        verbose_name = 'Estudiante'
