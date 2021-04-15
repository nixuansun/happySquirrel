from django.forms import ModelForm
from .models import happySquirrel

class SquirrelForm(ModelForm):
	class Meta:
		model = happySquirrel
		fields = '__all__'
