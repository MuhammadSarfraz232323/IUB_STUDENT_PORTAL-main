from django import forms
class signup(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Enter your name "}))
    father_name=forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Enter your father name " }))
    phone_number=forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Enter your phone number "}))
    email_address=forms.EmailField(label='',widget=forms.EmailInput(attrs={"placeholder":"Enter your email adress "}))
    password=forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Enter your password "}))
    cnic=forms.CharField(label='',widget=forms.TextInput(attrs={"pattern":"[0-9]{5}-[0-9]{7}-[0-9]{1}","placeholder":"Enter your CNIC"}))
class Admissionf(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your name "
        }))
    father_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your father name "
         }))
    father_occupation=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter father occupation",
    "cols-span":3
    }))
    phone_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your phone number "
        }))
    email_address=forms.EmailField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your email adress "
        }))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={
        "placeholder":"Enter your password "
        }))
    matric_school_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your matric school name ",
        'cols-span':3
    }))
    matric_marks=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your matric marks ",
        "cols-span":3
    }))
    matric_roll_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your matric roll number ",
        "cols-span":3
    }))
    matric_board=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your matric board "
    }))
    inter_college_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your college name ",
        "cols-span":3
    }))
    inter_marks=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your inter marks ",
        "cols-span":3
    }))
    inter_roll_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your inter roll number ",
        "cols-span":3
    }))
    department=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter the name of department"
    }))
    gender_choice=[
        ("Male","Male"),
        ("Female","Female"),
        ("other","Other")
    ]
    Gender=forms.ChoiceField(choices=gender_choice,label='',widget=forms.Select(attrs={
        "class":"form-control"
    }))
    image=forms.ImageField(label='',widget=forms.ClearableFileInput(attrs={
        "class":"form-control"
    }))
    
class Myform(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your name "
    }))    
    email_address=forms.EmailField(label='',widget=forms.EmailInput(attrs={
        "placeholder":"Enter your email adress"
    }))
    password=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your password "
    }))
    cnic=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your CNIC "
    }))
class Adminf(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your name"
    }))
    first_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your first name  "
    }))
    last_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your last name "
    }))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={
        "placeholder":"Enter your password "
    }))
class Car_parkingf(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your name "
    }))    
    father_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your father name "
    }))
    phone_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your phone number "
    }))
    registration_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter registration number "
    }))
    vehicle_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter vehicle number"
    }))
    vehicel_choice=[
        ("Car","Car"),
        ("Motor Bike","Motor Bike"),
        ("Bicycle","Bicycle"),
        ("Van","Van"),
        ("Rikshaw","Rikshaw")
    ]
    vehicle_type=forms.ChoiceField(choices=vehicel_choice,widget=forms.Select(attrs={
        "class":"form-control"
    }))
    upload_paid_challan_pic=forms.ImageField(label='',widget=forms.ClearableFileInput(attrs={
        "class":"form-control"
    }))
class Libraryf(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter name "
    }))    
    father_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter father name "
    }))
    registration_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter registartion number "
    }))
    password=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter password "
    }))
    email=forms.EmailField(label='',widget=forms.EmailInput(attrs={
        "placeholder":"Enter your email adress"
        }))
    department=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter department  name "
    }))
    section=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter the section name"
    }))

class Feef(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter name "
    }))    
    father_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter father name "
    }))
    phone_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter phone number "
    }))
    registration_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter registration "
    }))
    department=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter department name "
    }))
    section=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter name of  your section "
    }))
    monthly_income=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your monthly income "
    }))
    gender_choice=[
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    ]
    email=forms.EmailField(label='',widget=forms.EmailInput(attrs={
        "placeholder":"Enter your email adress "
    }))
    gender=forms.ChoiceField(choices=gender_choice,widget=forms.Select(attrs={
        "class":"form-control"
    }))
    fee_challan=forms.ImageField(label='',widget=forms.ClearableFileInput(attrs={
        "class ":"form-control"
    }))

class Repeat_coursef(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter name "
    }))
    father_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your father name "
    }))
    phone_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your phone number "
    }))
    department=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your department"
    }))
    semester=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your semester"
    }))
    section=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your section"
    }))
    email=forms.EmailField(label='',widget=forms.EmailInput(attrs={
        "placeholder":"Enter your email adress "
    }))
    image=forms.ImageField(label='',widget=forms.ClearableFileInput(attrs={
        "class":"form-control"
    }))

class scholarshipf(forms.Form):
    image=forms.ImageField(label='',widget=forms.ClearableFileInput(attrs={
        "class":"form-control"
            }))    

class scholarship_dataf(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter name "
    }))
    father_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter father name "
    }))
    phone_number=forms.IntegerField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter phone number "
    }))
    email_address=forms.EmailField(label='',widget=forms.EmailInput(attrs={
        "placeholder":"Enter your email adress"
    }))
    password=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter password "
    }))
    roll_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter phone roll number "
    }))
    department=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter the name of your department "
    })) 
    semester=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your semester number"
    }))
    section=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter the name of your section "
    }))
    monthly_income=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your monthly income "
    }))
    gardian_profession=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter profession of your gardian "
    }))
    gender_select=[
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    ]
    gender=forms.ChoiceField(choices=gender_select,widget=forms.Select(attrs={
        "class":"form-control"
    }))
            
class otp_form(forms.Form):
    otp_variable=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your OTP"
    }))            