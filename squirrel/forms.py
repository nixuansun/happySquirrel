from django.forms import ModelForm
from .models import happySquirrel

class squirrelForm(ModelForm):
	class Meta:
		model = happySquirrel
		fields = '__all__'
