from rest_framework import serializers

class UserActivitySerializer(serializers.Serializer):
    mouseMovementCount = serializers.IntegerField()
    keystrokeCount = serializers.IntegerField()
    timeOnPage = serializers.IntegerField()
    js_enabled = serializers.BooleanField()
