from django import forms
from blog.models import UserBlog,Comments
import pickle

class EnterBlog(forms.ModelForm):
	title=forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'placeholder':'Title',

		}
		))
	body=forms.CharField(widget=forms.Textarea(
		attrs={
		'class':'form-control',
		'placeholder':'Body',
		'rows':"20",
		'column':"50",

		}
		))
	picture = forms.ImageField(help_text="Upload image: ", required=False)

	class Meta:
		model= UserBlog
		fields=('title','body','picture',)



class EnterComments(forms.ModelForm):
	comment=forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'placeholder':'Type your message here..',
		'aria-describedby':'sizing-addon3',

		}
		))

	class Meta:
		model= Comments
		fields=('comment',)


class ComplexMultiWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
            forms.TextInput(),
            forms.TextInput(),
            
        )
        super(ComplexMultiWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            data = value.split(',')
            return [data[0],data[1]]
        return [None, None]
    def format_output(self, rendered_widgets):
        return u'\n'.join(rendered_widgets)


class ComplexField(forms.MultiValueField):
    def __init__(self, required=True, widget=None, label=None, initial=None):
        fields = (
            forms.CharField(),
            forms.CharField(),
        )
        super(ComplexField, self).__init__(fields, required,
                                           widget, label, initial)

    def compress(self, data_list):
        if data_list:
            return '%s,%s' % (data_list[0],data_list[1])
        return None
 		
class ComplexFieldForm(forms.Form):
            field1 = ComplexField(widget=ComplexMultiWidget())

