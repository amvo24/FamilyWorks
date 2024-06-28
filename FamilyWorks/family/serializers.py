from rest_framework import serializers
from .models import Family, FamilyMembership, Invitation

class FamilySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.full_name')

    class Meta:
        model = Family
        fields = [
            "id",
            "name",
            "description",
            "created_by"
        ]
        read_only_fields = ['created_by']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        # family = self.context['request'].family
        # FamilyMembership.objects.create(user=user)
        # return super().create(validated_data)
        family = Family.objects.create(**validated_data)  # Create the Family instance
        FamilyMembership.objects.create(user=user, family=family)
        return family
