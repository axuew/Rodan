import urlparse
from django.core.urlresolvers import resolve
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rodan.models.job import Job
from rodan.models.inputporttype import InputPortType
from rodan.serializers.inputporttype import InputPortTypeSerializer


class InputPortTypeList(generics.ListCreateAPIView):
    model = InputPortType
    serializer_class = InputPortTypeSerializer
    permission_classes = (permissions.IsAuthenticated, )
    paginate_by = None

    def post(self, request, *args, **kwargs):
        minimum = request.DATA.get('minimum', None)
        maximum = request.DATA.get('maximum', None)
        resource_type = request.DATA.get('resource_type', None)

        if not minimum or not maximum:
            return Response({"message": "You must specify minimum and maximum for this InputPortType"}, status=status.HTTP_400_BAD_REQUEST)

        job = request.DATA.get('job', None)
        try:
            job_obj = self._resolve_to_object(job, Job)
        except Exception as e:
            return Response({'message': "Error resolving job object. {0}".format(e)}, status=status.HTTP_400_BAD_REQUEST)

        InputPortType(job=job_obj,
                      resource_type=resource_type,
                      minimum=minimum,
                      maximum=maximum).save()
        return Response(status=status.HTTP_201_CREATED)

    def _resolve_to_object(self, request_url, model):
        value = urlparse.urlparse(request_url).path
        o = resolve(value)
        obj_pk = o.kwargs.get('pk')
        return model.objects.get(pk=obj_pk)


class InputPortTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = InputPortType
    serializer_class = InputPortTypeSerializer
    permission_classes = (permissions.IsAuthenticated, )
