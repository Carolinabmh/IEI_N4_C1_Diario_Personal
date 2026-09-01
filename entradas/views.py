from django.http import HttpResponse


def inicio(request):
    return HttpResponse(
        "<h1>Diario Personal</h1>"
        "<p>Bienvenido a Diario Personal, un espacio para gestionar y organizar tus entradas personales.</p>"
    )

def error_404(request, exception):
    return HttpResponse(
        "<h1>Error 404</h1>"
        "<p>Lo sentimos, la página que buscas no existe en Diario Personal.</p>",
        status=404
    )
