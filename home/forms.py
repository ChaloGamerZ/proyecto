from django import forms
from django.contrib.auth.models import User
from .models import *
class login_form (forms.Form):
	user = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre de Usuario'}))
	password= forms.CharField(widget=forms.PasswordInput(render_value=False))
#formulario de la tabla material
class agregar_material_form(forms.ModelForm):
	tipo_elemento = forms.ChoiceField(choices=([('Devolutivo','Devolutivo'), ('Consumible','Consumible') ]), initial='1', required = True,)
	class Meta:
		model = Material
		fields = '__all__'
#fromulario de la tabla material
class agregar_marca_form(forms.ModelForm):
	class Meta:
		model = Marca
		fields = '__all__'
#formularios de la tabla prestamo
class agregar_prestamoF(forms.ModelForm):
	class Meta:
		model=Prestamo
		fields='__all__'

class agregar_DPrestamoF(forms.ModelForm):
	class Meta:
		model=Detalle_Prestamo
		fields='__all__'

#formulario de la tabla categoria
class categoria_form(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = '__all__'

#formulario de la tabla bodega
class agregar_bodega_form(forms.ModelForm):
	class Meta:
		model= Bodega
		fields= '__all__'

#formulario de la tabla cuentadante
class cuentadante_form(forms.ModelForm):
	class Meta:
		model = Cuentadante
		fields = '__all__' 

#formulario de la tabla programa
class agregar_programas_form(forms.ModelForm):
	class Meta:
		model = Programa
		fields ='__all__'

class ficha_form(forms.ModelForm):
	class Meta:
		model = Ficha
		fields = '__all__'

class Bodega_Material_form(forms.ModelForm):
	class Meta:
		model = Bodega_Material
		fields = '__all__'


class agregar_aprendiz_form(forms.ModelForm):
	class Meta:
		model = Aprendiz
		fields = '__all__'
			