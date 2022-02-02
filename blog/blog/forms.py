from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=200, widget=forms.Textarea(attrs={"rows": 2, "cols": 5})
    )
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    age = forms.IntegerField(min_value=18, required=False)
