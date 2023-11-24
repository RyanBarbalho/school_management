from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from api.serializers.jwtSerializer import JWTSerializer


@method_decorator(csrf_exempt, name="dispatch")
class CustomJWTView(TokenObtainPairView):
    serializer_class = JWTSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        response_data = {
            "user_id": data["id"],
            "tokens": {
                "refresh": data["refresh"],
                "access": data["access"],
            },
        }

        return Response(response_data, status=status.HTTP_200_OK)
