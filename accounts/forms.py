from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from random import choices

class LoginForm(forms.Form):
    username= forms.CharField(max_length=100, label= 'Username')
    password= forms.CharField(max_length=100, label= 'Password', widget= forms.PasswordInput)
    
    def clean(self):
        username= self.cleaned_data.get('username')
        password= self.cleaned_data.get('password')
        if username and password:
            user= authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('You entered invalid Username or Password!')
        return super(LoginForm, self).clean()
    
class RegisterForm(forms.ModelForm):
    
     username= forms.CharField(max_length=100, label= 'Username')
     first_name= forms.CharField(max_length=100, label= 'First Name')
     last_name= forms.CharField(max_length=100, label= 'Last Name')
     password1= forms.CharField(max_length=100, label= 'Password', widget= forms.PasswordInput)
     password2= forms.CharField(max_length=100, label= 'Password Verification', widget= forms.PasswordInput)
     #email= forms.EmailField(max_length=100, label= 'Email')
     
     class Meta:
         model= User
         field=   fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
                  
     def clean_password2(self):
         password1= self.cleaned_data.get('password1')
         password2= self.cleaned_data.get('password2')
         if password1 and password2 and password1 != password2:
             raise forms.ValidationError("Entered passwords do not match!")
         return password2
   
class UserProfile(forms.ModelForm): 
    MALE='M'
    FEMALE='F'
    OTHER='O'
    SEX=((MALE,'MALE'), (FEMALE,'FEMALE'),(OTHER,'OTHER'))
    
    sex= forms.CharField(widget=forms.Select(choices=SEX))
    description= forms.CharField(widget=forms.Textarea,max_length=500,label='Description',required=False)
    birth= forms.DateField(widget=forms.SelectDateWidget,label='Birth Date',required=False)
    phone_number= forms.CharField(max_length=11,label='Phone Number',required=False)
    
    class Meta:
        model= User
        fields=['username','first_name','last_name','email','birth','phone_number','sex','description']  
        
    def __init__(self,*args,**kwargs):
        super(UserProfile,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}   
            
        self.fields['description'].widget.attrs['rows']=10
        self.fields['description'].widget.attrs['cols']=10