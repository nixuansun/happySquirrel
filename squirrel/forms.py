from django.forms import ModelForm

from .models import happySquirrel


class squirrelUpdateForm(ModelForm):
	class Meta:
		model = happySquirrel
		fields = [
			'latitude',
			'longitude',
			'unique_squirrel_id',
			'shift',
			'date',
			'age',
		]
