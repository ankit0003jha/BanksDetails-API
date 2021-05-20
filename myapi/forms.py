###  if u want to add data from frontend you can use this form method...


from django import forms  
from myapi.models import Branches
class BranchesForm(forms.ModelForm):  
    class Meta:  
        model = Branches 
        fields = ['ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state','bank_name'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'ifsc': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'branch': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'address': forms.TextInput(attrs={ 'class': 'form-control' }),
      }