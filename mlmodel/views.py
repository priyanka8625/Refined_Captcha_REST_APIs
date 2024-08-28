from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import joblib
import numpy as np
from .serializers import UserActivitySerializer

# to load the model.pkl file
import os
from django.conf import settings

# Load the trained model (ensure the model is saved as model.pkl in the same directory)
# Construct the absolute path to the model.pkl file
MODEL_PATH = os.path.join(settings.BASE_DIR, 'mlmodel', 'captcha_model', 'model.pkl')

# Load the trained model
model = joblib.load(MODEL_PATH)

class PredictView(APIView):
    def post(self, request):
        serializer = UserActivitySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            input_data = np.array([[data['mouseMovementCount'],
                                    data['keystrokeCount'],
                                    data['timeOnPage'],
                                    int(data['js_enabled'])]])
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1]
            return Response({
                "prediction": int(prediction),
                "probability": float(probability)
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
