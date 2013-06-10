from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Feligres

class FeligresCreateRead(ListCreateAPIView):
	model = Feligres

class FeligresCreateReadUpdateDelete(ListCreateAPIView):
	model = Feligres