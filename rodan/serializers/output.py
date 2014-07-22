from rest_framework import serializers
from rodan.models.output import Output
from rodan.serializers.user import UserListSerializer
from rodan.serializers.resource import OutputResourceSerializer
from rodan.serializers.outputport import OutputPortSerializer
from rodan.serializers.runjob import RunJobSerializer


class OutputSerializer(serializers.HyperlinkedModelSerializer):
    creator = UserListSerializer(read_only=True)
    resource = OutputResourceSerializer()
    output_port = OutputPortSerializer()
    run_job = RunJobSerializer()

    class Meta:
        model = Output
        fields = ("url",
                  "uuid",
                  "output_port",
                  "run_job",
                  "resource")


class OutputListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Output
        fields = ("url",
                  "uuid",
                  "output_port",
                  "run_job",
                  "resource")