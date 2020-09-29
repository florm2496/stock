from .models import Cepa , Bodega,Reserva,Unidad,Vino
from django import forms

class CepaNewForm(forms.ModelForm):
    class Meta:
        model=Cepa
        fields=['nombre','descripcion','estado']
        labels={'nombre':'Nombre','descripcion': 'Descipcion de la cepa' , 'estado':'Estado'}
        widget={'descripcion':forms.TextInput}

def __init__(self, *args, **kwargs): #SE SOBRESCRIBE EL CONSTRUCTOR DEL FORMULARIO
    super().__init__(*args, **kwargs) #SE INVOCA EL CONSTRUCTOR
    for field in iter(self.fields):
        self.fields[field].widget.attrs.update({
            'class':'form-control',
        })

class BodegaNewForm(forms.ModelForm):
    class Meta:
        model=Bodega
        fields=['nombre','numero','email']
        labels={'nombre':'Nombre', 'estado':'Numero','email': 'Email' }
        #widget={'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs): #SE SOBRESCRIBE EL CONSTRUCTOR DEL FORMULARIO
        super().__init__(*args, **kwargs) #SE INVOCA EL CONSTRUCTOR
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
            })
class ReservaNewForm(forms.ModelForm):
    class Meta:
        model=Reserva
        fields=['tipo','descripcion']
        labels={'tipo':'Tipo', 'descripcion':'Descripcion' }
        #widget={'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs): #SE SOBRESCRIBE EL CONSTRUCTOR DEL FORMULARIO
        super().__init__(*args, **kwargs) #SE INVOCA EL CONSTRUCTOR
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
            })
class UnidadNewForm(forms.ModelForm):
    class Meta:
        model=Unidad
        fields=['medida']
        labels={'medida':'Medida'}
        #widget={'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs): #SE SOBRESCRIBE EL CONSTRUCTOR DEL FORMULARIO
        super().__init__(*args, **kwargs) #SE INVOCA EL CONSTRUCTOR
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
            })
class VinoNewForm(forms.ModelForm):
    class Meta:
        model=Vino
        fields=['descripcion','codigo','precioventa','foto','reserva','bodega','cepa','unidad','existencia','ultimacompra','sm']
        #labels={'medida':'Medida'}
        #widget={'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs): #SE SOBRESCRIBE EL CONSTRUCTOR DEL FORMULARIO
        super().__init__(*args, **kwargs) #SE INVOCA EL CONSTRUCTOR
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
            })
            self.fields['ultimacompra'].widget.attrs['readonly']=True
            self.fields['existencia'].widget.attrs['readonly']=True


    
