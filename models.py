from django.db import models
#from ckeditor.fields import RichTextField
from datetime import date

# Create your models here.




# Post--Acerca de
class About(models.Model):
    id = models.AutoField(primary_key = True)
    empresa = models.CharField('Nombre de la Empresa', max_length=100, blank=False, null=False)
    direccion = models.CharField('Dirección', max_length=100, blank=False, null=False)
    #contenido = RichTextField()
    estado = models.BooleanField('Publicado/no Publicado', default = True)

    def __str__(self):
        return self.contenido


# Post--Noticias
class Noticia(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título', max_length= 90, blank = False, null= False)
    slug_new = models.CharField('Slug', max_length=100, blank=False, null=False)
    descripcion = models.CharField('Descripción', max_length= 100, blank = False, null = False)
    #contenido = RichTextField()
    imagen = models.ImageField(upload_to= 'static')
    imagen_name = models.CharField('Imagen.extención', max_length= 225, blank= True, null= True)
    autor = models.CharField('Autor', max_length= 100, blank = False, null = False)
    estado = models.BooleanField('Publicado/no Publicado', default = True)
    destacada = models.BooleanField('Destacada/no Destacada', default = False)
    fecha = models.DateField('Fecha de creación', default= date.today())

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo



# Post--Proyectos
class Proyecto(models.Model):
    id = models.AutoField(primary_key = True)
    proyecto = models.CharField('Proyecto', max_length= 90, blank = False, null= False)
    slug_proj = models.CharField('Slug', max_length= 100, blank= False, null= False)
    descripcion = models.CharField('Descripción', max_length= 100, blank = False, null = False)
    #contenido = RichTextField()
    imagen = models.ImageField(upload_to= 'static')
    imagen_name = models.CharField('Imagen.extención', max_length= 225, blank= True, null= True)
    estado = models.BooleanField('Publicado/no Publicado', default = True)
    fecha = models.DateField('Fecha', default= date.today())

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.proyecto



# Post--Servicio
class Servicio(models.Model):
    id = models.AutoField(primary_key = True)
    servicio = models.CharField('Servicio', max_length= 90, blank = False, null= False)
    tipo_servicio = models.CharField('Tipo de servicio', max_length=100, blank=False, null=False)
    slug_serv = models.CharField('Slug', max_length= 100, blank= False, null= False)
    descripcion = models.CharField('Descripción', max_length= 100, blank = False, null = False)
    #contenido = RichTextField()
    imagen = models.ImageField(upload_to= 'static')
    imagen_name = models.CharField('Imagen.extención', max_length= 225, blank= True, null= True)
    estado = models.BooleanField('Publicado/no Publicado', default = True)
    fecha = models.DateField('Fecha', default= date.today())

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.servicio



# Post--Tramites
class Tramite(models.Model):
    id = models.AutoField(primary_key = True)
    tramite = models.CharField('Trámite', max_length= 90, blank = False, null= False)
    slug_tram = models.CharField('Slug', max_length=100, blank=False, null=False)
    descripcion = models.CharField('Descripción', max_length= 100, blank = False, null = False)
    #contenido = RichTextField()
    imagen = models.ImageField(upload_to= 'static')
    imagen_name = models.CharField('Imagen.extención', max_length= 225, blank= True, null= True)
    estado = models.BooleanField('Publicado/no Publicado', default = True)
    fecha = models.DateField('Fecha', default= date.today())

    class Meta:
        verbose_name = 'Tramite'
        verbose_name_plural = 'Tramites'

    def __str__(self):
        return self.tramite



