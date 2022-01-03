from django.shortcuts import render
from django.core.mail import send_mail
import re

# class datas():
#     "Stores name and place pairs"
#     def __init__(self, Number,Name,Age,Speed,Mass,Radius,Volume,Density,Surface_Temperature,Internal_Temprature):
#         self.Number = Number
#         self.Name = Name
#         self.Age = Age
#         self.Speed = Speed
#         self.Mass = Mass
#         self.Radius = Volume
#         self.Surface_Temprature = Surface_Temperature
#         self.Density = Density
#         self_distancefromsun = Distance_From_Sun




lists = [
    [1,'Sun','4.603 billion years','220 km per second', '1.989 × 10<sup>30</sup> kg','696340','-180 to 427 °C','1.622 x 10<sup>5</sup> kg per m<sup>3</sup>','58','3.7 m/s<sup>2</sup>','0','58 day 15 hour 30 min','87.97 days','2°'],
    [2,'Mercury','4.503 billion years','47.4 km/s', '3.285 × 10<sup>23</sup> kg','2439.7','-180 to 427 °C','5.43 g/cm<sup>3</sup>','58','3.7 m/s<sup>2</sup>','0','58 day 15 hour 30 min','87.97 days','2°'],
    [3,'Venus','4.503 billion years','35.02 km/s', '4.867 × 10<sup>24</sup> kg','6051.8','470 °C','5.24 g/cm<sup>3</sup>','108.2','8.87 m/s<sup>2</sup>','0','116 day 18 hour','224.7 days','3°'],
    [4,'Earth','4.543 billion years','29.78 km/s', '5.972 × 10<sup>24</sup> kg','6378','-89.2 to 58 °C','5.51 g/cm<sup>3</sup>','149.6','9.807 m/s<sup>2</sup>','1','1 day','365.24 days','23.4°'],
    [5,'Mars','4.603 billion years','24 km/s', '6.39 × 10<sup>23</sup> kg','3389','-140 to 21 °C','3.39 g/cm<sup>3</sup>','227.9','3.721 m/s<sup>2</sup>','2','1 day 37 min','1.88 years','25°'],
    [6,'Jupiter','4.603 billion years','13.06 km/s', '1.898 × 1027 kg','69911','-145 °C','1.33 g/cm3','778','24.79 m/s<sup>2</sup>','79','9 hour 56 min','11.86 years','3.13°'],
    [7,'Saturn',' 4.503 billion years','9.68 km/s', '5.683 × 10<sup>26</sup> kg','58232','-138 °C','0.687 g/cm<sup>3</sup>','82','3.7 m/s<sup>2</sup>','1.48','10 hour 42 min','29.46 years','27°'],
    [8,'Uranus','4.503 billion years','6.80 km/s', '8.681 × 10<sup>25</sup> kg','25362','-218 to -153 °C','1.27 g/cm<sup>3</sup>','1.8','8.87 m/s<sup>2</sup>','27','17 hour 14 min','84.01 years','98°'],
    [9,'Neptune','4.503 billion years','5.43 km/s', '1.024 × 10<sup>30</sup> kg','24622','-218 to -200 °C','1.64 g/cm<sup>3</sup>','4.475','11.15 m/s<sup>2</sup>','14','16 hour 06 min','164.79 years','28°'],
    [10,'Pluto','4.603 billion years','4.74 km/s', '1.309 × 10<sup>22</sup> kg','1188.3','-240 to -218 °C','1.88 g/cm<sup>3</sup>','5.9','0.62 m/s<sup>2</sup>','5','6 day 9 hour 36 min','248.59 years','57°']
]

data=lists

def fun_index(request):
    return render(request,'index.html',{})

def fun_sun(request):
    return render(request,'Sun.html',{'data':data[0]})

def fun_mercury(request):
    return render(request,'Mercury.html',{'data':data[1]})

def fun_venus(request):
    return render(request,'Venus.html',{'data':data[2]})

def fun_earth(request):
    return render(request,'Earth.html',{'data':data[3]})

def fun_mars(request):
    return render(request,'Mars.html',{'data':data[4]})

def fun_jupiter(request):
    return render(request,'Jupiter.html',{'data':data[5]})

def fun_saturn(request):
    return render(request,'Saturn.html',{'data':data[6]})

def fun_uranus(request):
    return render(request,'Uranus.html',{'data':data[7]})

def fun_neptune(request):
    return render(request,'Neptune.html',{'data':data[8]})

def fun_pluto(request):
    return render(request,'Pluto.html',{'data':data[9]})


def fun_milkyway(request):
    return render(request,'Milkyway.html',{})

def fun_andromeda(request):
    return render(request,'Andromeda.html',{})

def fun_contact(request):
    msg = ''
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        message = request.POST.get('Message')
        myemail = 'akhilsainiwork@gmail.com'

        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        else:
            message = 'Name : '+ name +'\nEmail : '+email+'\nMessage : '+message
            send_mail('Message From Space Learn',message,'',[myemail])
            msg = 'Your message have been sent successfully. Hope that I see it soon.'

    return render(request,'Contact.html',{'msg':msg})

def fun_login(request):
    return render(request,'Login.html',{})

def fun_register(request):
    return render(request,'Register.html',{})

def fun_questions(request):
    return render(request,'Questions.html',{})