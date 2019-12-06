from import_export import resources
from .models import Sq

class SqResource(resources.ModelResource):
    class Meta:
        model = Sq