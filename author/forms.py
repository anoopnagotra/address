from django.forms import ModelForm, Select, ImageField
# from django.contrib.auth.models import User
from author.models import Author
from bootstrap_datepicker_plus import DateTimePickerInput


class AuthorForm(ModelForm):
    author_image = ImageField()

    class Meta:
        model = Author
        fields = '__all__'
        # widgets = {
        #     'user': Select(choices=User.objects.all())
        # }
