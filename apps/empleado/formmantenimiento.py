from django import forms
from apps.empleado.models import Mantenimiento



class FormMantenimiento (forms.ModelForm):

    class Meta:
        model = Mantenimiento

        fields = (
            'EmpleadoId',
            'EquipoId',
            'fecha',
            'tipoMantenimiento',
        )

        labels = {
            'EmpleadoId' : 'seleccione',
            'EquipoId' : 'seleccione',
            'fecha' : 'Ingrese una fecha',
            'tipoMantenimiento' : 'Ingrese una descripcion'
        }

        widgets = {
            'EmpleadoId' : forms.Select(attrs={'class': 'form-control'}),
            'EquipoId' : forms.Select(attrs={'class': 'form-control'}),
            'fecha' : forms.TextInput(attrs={'class': 'form-control'}),
            'tipoMantenimiento' : forms.TextInput(attrs={'class': 'form-control'}),
        }