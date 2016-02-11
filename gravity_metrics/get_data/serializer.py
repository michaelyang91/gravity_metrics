from rest_framework import serializers
from gravity_metrics.get_data.models import Delta

class DeltaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Delta
		fields = ('id', 'timestamp', 'delta')