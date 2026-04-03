from django.db import models

class Producto(models.Model):
    
    CATEGORIAS = [
        ('snack', 'Snack'),
        ('bebida', 'Bebida'),
        ('lacteo', 'Lácteo'),
        ('dulce', 'Dulce'),
        ('otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)


    @classmethod
    def filtrar(cls,nombre = None, min_precio = None, max_precio = None, categoria = None):
    
        productos = cls.objects.all()
    
        if nombre:
            productos = productos.filter(nombre__icontains = nombre)
    
        if min_precio is not None:
            productos = productos.filter(precio__gte = min_precio)
        
        if max_precio is not None:
            productos = productos.filter(precio__lte = max_precio)
        
        if categoria:
            productos = productos.filter(categoria = categoria)
        
        return productos                




    def __str__(self):
        return self.nombre