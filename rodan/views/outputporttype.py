from rest_framework import generics
from rodan.models.outputporttype import OutputPortType
from rodan.serializers.outputporttype import OutputPortTypeSerializer


class OutputPortTypeList(generics.ListCreateAPIView):
    model = OutputPortType
    serializer_class = OutputPortTypeSerializer
    paginate_by = None


class OutputPortTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = OutputPortType
    serializer_class = OutputPortTypeSerializer
