from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# ao retornar o token, irá retornar o id do usuario tambem
class JWTSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["id"] = self.user.id
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data
