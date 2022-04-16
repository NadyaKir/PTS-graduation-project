
from dataclasses import Field
from import_export import resources
from .models import GVS
from import_export.fields import Field


class GVSResource(resources.ModelResource):
    id = Field(attribute='id', column_name='№')
    street = Field(attribute='street', column_name='Улица')
    build = Field(attribute='build',  column_name='Дом')
    region = Field(attribute='region', column_name='Сетевой район')
    date_disconnect = Field(attribute='date_disconnect',
                            column_name='Дата отключения')
    date_connect = Field(attribute='date_connect',
                         column_name='Ориетировочная дата устранения')
    reason = Field(attribute='reason', column_name='Причина отсутствия ГВС')

    class Meta:
        model = GVS
        fields = ('id', 'street', 'build', 'region',
                  'date_disconnect', 'date_connect', 'reason')
        export_order = ('id', 'region', 'street', 'build',
                        'date_disconnect', 'date_connect', 'reason')
        widgets = {
            'date_disconnect': {'format': '%Y.%m.%d'},
            'date_connect': {'format': '%Y.%m.%d'},
        }
