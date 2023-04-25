from django import forms



def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('name started with a')

def check_for_len(value):
    if len(value)<6:
        raise forms.ValidationError('len is less')

class studentForm(forms.Form):
    Name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField(max_length=100)