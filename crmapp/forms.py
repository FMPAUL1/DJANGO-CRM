from django.contrib.auth.forms import UserCreationForm
from django import forms 

from django.contrib.auth.models import User
from .models import Record

class SignupForm(UserCreationForm):
    Email =forms.EmailField(max_length=200,label="", widget=forms.TextInput(attrs={'class':'forms-control','placeholder':'Enter Email Address'}));
    
    Firstname=forms.CharField(max_length=100,label="", widget=forms.TextInput(attrs={'class':'forms-control','placeholder':'Enter Firstname'}))
    Lastname =forms.CharField(max_length=150,label="", widget=forms.TextInput(attrs={'class':'forms-control','placeholder':'Enter Lastname'}))
    
    class Meta:
        model = User;
        fields= ('username','Firstname','Lastname','Email','password1','password2')
        
        def __init__(self,*args, **kwargs):
            super(SignupForm,self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['class']='forms-control'
            self.fields['username'].widget.attrs['placeholder']='username'
            self.fields['username'].label=''
            self.fields['username'].help_text='<span class="form-text text-muted"> Username 100</span>'
            
            
            self.fields['password1'].widget.attrs['class']='forms-control'
            self.fields['password1'].widget.attrs['placeholder']='password1'
            self.fields['password1'].label=''
            self.fields['password1'].help_text='<span class="form-text text-muted"> hey your password too short </span>'
            
            self.fields['password2'].widget.attrs['class']='forms-control'
            self.fields['password2'].widget.attrs['placeholder']='confirm password'
            self.fields['password2'].label=''
            self.fields['password2'].help_text='<span class=" form-text text-muted">passord must match </span>'
            
            
            
#creating a form to add record

class Add_record(forms.ModelForm):
   email =forms.EmailField(max_length=200,label="", widget=forms.widgets.TextInput(attrs={'class':'forms-control','placeholder':'Enter Email Address'}));
   firstname=forms.CharField(max_length=100,label="", widget=forms.widgets.TextInput(attrs={'class':'forms-control','placeholder':'Enter Firstname'}))
   lastname=forms.CharField(max_length=100,label="", widget=forms.widgets.TextInput(attrs={'class':'forms-control','placeholder':'Enter lastname'}))
   phone =forms.CharField(max_length=150,label="", widget=forms.widgets.TextInput(attrs={'class':'forms-control','placeholder':'Enter phone number'}))
   state  =forms.CharField(max_length=150,label="", widget=forms.widgets.TextInput(attrs={'class':'forms-control','placeholder':'Enter State of origin'}))
   zipcode =forms.CharField(max_length=150,label="", widget=forms.widgets.TextInput(attrs={'class':'forms-control','placeholder':'Zip code section'}))
    
   address =forms.CharField(max_length=150,label="", widget=forms.widgets.TextInput(attrs={'class':'forms-control','placeholder':'Enter address'}))
    
   class Meta:
        model = Record
        fields= ['email','firstname','lastname','phone','state', 'address','zipcode']
        