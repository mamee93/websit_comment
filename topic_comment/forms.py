from django import forms
from .models import Topic,Comments
#from ckeditor.widgets import CKEditorWidget



class CommentForm(forms.ModelForm):
	
	comments = forms.CharField(label='', widget = forms.Textarea(attrs={'class':'from-control','placeholder':'Text here ','rows':'3', 'cols':'50'}))
	class Meta:
		model= Comments
		fields = ['comments']

 
