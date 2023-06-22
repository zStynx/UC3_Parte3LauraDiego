from django.shortcuts import render, redirect, HttpResponse
layout = """
    <div class="flex">
            <div class="imagen">
                <img src="../static/images/logo.png" alt="logo">
            </div>
            <hr>
            <div class="navegacion">
                <a href="/inicio">INICIO</a>
                <a href="/primos">PRIMOS</a>
                <a href="">EXAMEN</a>
            </div>
    </div>
"""
def index(request):
    return render(request,"index.html")

def inicio(request):
    lista=["Matemática","Programación","Diseño Web","Gestion de Procesos","Algoritmos","Requerimientos","Tesis"]
    resultado = """
        Mostrando la lista de los cursos: 
        <br>
        <ul>
    """
    for i in lista:
        resultado+=f"<li>{i}</li>"
    resultado+="</ul>"
    return HttpResponse(layout +resultado)

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos(request,a=1,b=100):
    if a>b:
        return redirect('primos',a=b,b=a)
    resultado = f"""
        <h2>Números primos de [{a}, {b}]</h2>
        Resultado:<br>
        <ul>
    """

    for numero in range(a, b + 1):
        if es_primo(numero):
            resultado += f"<li>{numero}</li>"

    resultado += "</ul>"
    
    return HttpResponse(layout+resultado)
    
