from rest_framework import viewsets
from .serializers import AlumnoSerializer
from .serializers import ReservaSerializer
from .serializers import LaboratorioSerializer
from .models import Alumno
from .models import Reserva
from .models import Laboratorio

# Create your views here.
class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class LaboratorioViewSet(viewsets.ModelViewSet):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer
