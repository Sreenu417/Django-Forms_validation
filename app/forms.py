from django import forms
dd1=(('male','male'),('female','female'))
c=(('python','python'),('java','java'),('mern','mern'))
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    url=forms.URLField()
    date=forms.DateField()
    time=forms.TimeField()
    datetime=forms.DateTimeField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea)
    #gender=forms.ChoiceField(choices=dd1)
    gender=forms.ChoiceField(choices=dd1,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)

