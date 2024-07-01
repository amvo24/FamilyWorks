from rest_framework import serializers
from .models import Task
from family.models import Family
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.full_name')
    family = serializers.ReadOnlyField(source='family.name')

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "created_by",
            "created_at",
            "family",
            "assigned_to",
            "status",
            "priority",
        ]
        read_fields_only = [
            "created_by", "created_at"
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        family_id = self.context['request'].data.get('family')

        try:
            family = Family.objects.get(id=family_id)
        except Family.DoesNotExist:
            raise serializers.ValidationError("Family with this ID does not exist")

        validated_data['family'] = family
        task = Task.objects.create(**validated_data)
        return task
