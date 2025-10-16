from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto # Cambiado de Comic a Producto

# Listar productos
def index(request):
    productos = Producto.objects.all() # Cambiado de Comic a Producto, y comics a productos
    return render(request, 'listar_productos.html', {'Producto': productos}) # Cambiado de comics a productos

# Agregar producto
def agregar_producto(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        editorial = request.POST['editorial']
        genero = request.POST['genero']
        precio = request.POST['precio']
        stock = request.POST['stock']
        fecha_publicacion = request.POST['fecha_publicacion']
        isbn = request.POST['isbn']
        tipo_producto = request.POST['tipo_producto']
        Producto.objects.create( # Cambiado de Comic a Producto
            titulo=titulo,
            autor=autor,
            editorial=editorial,
            genero=genero,
            precio=precio,
            stock=stock,
            fecha_publicacion=fecha_publicacion,
            isbn=isbn,
            tipo_producto=tipo_producto
        )
        return redirect('inicio')
    return render(request, 'agregar_producto.html')

# Editar producto
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id) # Cambiado de Comic a Producto
    if request.method == 'POST':
        producto.titulo = request.POST['titulo']
        producto.autor = request.POST['autor']
        producto.editorial = request.POST['editorial']
        producto.genero = request.POST['genero']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.fecha_publicacion = request.POST['fecha_publicacion']
        producto.isbn = request.POST['isbn']
        producto.tipo_producto = request.POST['tipo_producto']
        producto.save()
        return redirect('inicio')
    return render(request, 'editar_producto.html', {'producto': producto}) # Cambiado de comic a producto

# Borrar producto
def borrar_producto(request, id):
    producto = get_object_or_404(Producto, id=id) # Cambiado de Comic a Producto
    if request.method == 'POST':
        producto.delete()
        return redirect('inicio')
    return render(request, 'borrar_producto.html', {'producto': producto}) # Cambiado de comic a producto