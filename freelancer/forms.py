from django import forms
from freelancer.models import FreelancerProfile,Test




class FreelancerProfileForm(forms.ModelForm):
	
	college1=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	
	college2=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))

	
	college3=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))

	school1=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	
	school2=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	job1=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	job2=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	job3=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	job4=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	internship1=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	internship2=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	internship3=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	internship4=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	project1=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	project2=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	project3=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	project4=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	skill1=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	skill2=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	skill3=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	skill4=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	research1=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	research2=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	research3=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	research4=forms.CharField(required=False,max_length=200,widget=forms.TextInput(
		attrs={
		'class':'form-control col-md-6',
		'placeholder':'Sample text',

		}
		))
	additional=forms.CharField(widget=forms.Textarea(
		attrs={
		'class':'form-control',
		'placeholder':'About You',
		'rows':"5",
		'column':"30",

		}
		))
	picture = forms.ImageField(help_text="Upload image: ", required=False)

	class Meta:
		model=FreelancerProfile
		fields=[
			 'picture','phone','school1','school2','college1','college2','college3','job1','job2','job3','job4','internship1',
			 'internship2','internship3','internship4','project1','project2','project3','project4','skill1',
			 'skill2','skill3','skill4','research1','research2','research3','research4','additional',
			   	]	

	def clean(self):

		self.cleaned_data["jobs"]=self.cleaned_data['job1']+","+self.cleaned_data['job2']+","+self.cleaned_data['job3']+","+self.cleaned_data['job4']
		self.cleaned_data["college"]=self.cleaned_data['college1']+","+self.cleaned_data['college2']+","+self.cleaned_data['college3']
		self.cleaned_data["school"]=self.cleaned_data['school1']+","+self.cleaned_data['school2']
		self.cleaned_data["internships"]=self.cleaned_data['internship1']+","+self.cleaned_data['internship2']+","+self.cleaned_data['internship3']+","+self.cleaned_data['internship4']
		self.cleaned_data["projects"]=self.cleaned_data['project1']+","+self.cleaned_data['project2']+","+self.cleaned_data['project3']+","+self.cleaned_data['project4']
		self.cleaned_data["skills"]=self.cleaned_data['skill1']+","+self.cleaned_data['skill2']+","+self.cleaned_data['skill3']+","+self.cleaned_data['skill4']
		self.cleaned_data["research"]=self.cleaned_data['research1']+","+self.cleaned_data['research2']+","+self.cleaned_data['research3']+","+self.cleaned_data['research4']

		return self.cleaned_data


class TestForm(forms.ModelForm):

	job1=forms.CharField(max_length=120)
	job2=forms.CharField(max_length=120)
	job3=forms.CharField(max_length=120)
	job4=forms.CharField(max_length=120)

	class Meta:
		model=Test
		fields=[
		'jobs','job1','job2','job3','job4','school',

		]

	def clean(self):

		self.cleaned_data["jobs"]=self.cleaned_data['job1']+self.cleaned_data['job2'],self.cleaned_data['job3']+self.cleaned_data['job4']
		return self.cleaned_data