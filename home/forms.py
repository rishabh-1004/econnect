from django import forms

class ContactForm(forms.Form):
	name=forms.CharField(required=False,max_length=100,help_text='100 charecters max',widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Write a Post',

		}
		))
	email=forms.EmailField(required=True,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Write a Post',

		}
		))
	comment=forms.CharField(required=True,widget=forms.Textarea(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Write a Post',

		}
		))
