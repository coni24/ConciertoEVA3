from django import forms
from conciertoApp.models import Entrada, Persona, Concierto

class FormEntrada(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['Concierto', 'Persona', 'Categoria', 'Descripcion', 'NumeroAsiento', 'Precio', 'Sector']

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['RUT', 'Nombre', 'Apellido', 'Telefono', 'Edad', 'Correo']

    def clean_Nombre(self):
        nombre = self.cleaned_data['Nombre']
        if len(nombre) > 20:
            raise forms.ValidationError("El largo maximo del nombre son 20 caracteres")
        return nombre
    
    def clean_Apellido(self):
        apellido = self.cleaned_data['Apellido']
        if len(apellido) > 20:
            raise forms.ValidationError("El largo maximo del apellido son 20 caracteres")
        return apellido
    
    def clean_correo(self):
        email = self.cleaned_data['Correo']
        if email.find('@') == -1:
            raise forms.ValidationError("El correo debe contener @")
        return email

class FormConcierto(forms.ModelForm):
    class Meta:
        model = Concierto
        fields = ['Fecha', 'Hora', 'Lugar', 'Categoria', 'Capacidad']

