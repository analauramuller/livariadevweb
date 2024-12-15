from rest_framework.serializers import ModelSerializer

from core.models import Editora


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = ('email', 'site', 'nome')
        
    def validate_email(self, email):
        return email.lower()