from rest_framework import serializers

class UserActivitySerializer(serializers.Serializer):
    mouse_movements = serializers.IntegerField()
    keyboard_inputs = serializers.IntegerField()
    time_on_page = serializers.IntegerField()
    js_enabled = serializers.BooleanField()
