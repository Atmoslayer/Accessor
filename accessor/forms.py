from django import forms

class ShowData(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Введите имя', 'class': 'form__input'}
        )
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Введите номер телефона', 'class': 'form__input'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Введите электронную почту', 'class': 'form__input'}
        )
    )

