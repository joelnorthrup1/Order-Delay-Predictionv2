
# import the standard Django Forms
# from built-in library
from django import forms
   
# creating a form 
class InputForm(forms.Form):
   
    pca_components = forms.IntegerField(help_text = "Enter PCA Components")
    epochs = forms.IntegerField(help_text = "Enter Number of Epochs")
    days_delayed = forms.IntegerField(
                     help_text = "Enter days delayed threshold"
                     )
    