from django.shortcuts import render,redirect,HttpResponse
from app.models import tbl_volunteers,tbl_idgen,tbl_beneficiar,tbl_login,tbl_fooddonation,tbl_donor,tbl_publicrequest,tbl_review,tbl_complaint,tbl_publicreview,tbl_donorcomplaint,tbl_donorreview
from app.models import tbl_benefeciarrequest,tbl_beneficiarfoodallot
from django.core.files.storage import FileSystemStorage
import datetime
from django.core.mail import send_mail
from django.db.models import F

#response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')

def project(hello):
    return render(hello,"index.html")
def forms(request):
    return render(request,"form.html")
def admin1(request):
    return render(request,"admin1.html")
def adminheader(request):
    return render(request,"adminheader.html")
# Create your views here.

#public
def publicvolunteerregistration(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.vid
    id = int(id+1)
    vid = "VID_00" + str(id)
    request.session['vid'] = id    
    return render(request,"publicvolunteerregistration.html",{'vid':vid})
#inserting into tbl_valunteer from public
def publicinsertvolunteer(request):
    if request.method == 'POST':
        data=tbl_volunteers()
        data.volunteer_id = request.POST.get('volunteer_id')
        data.name = request.POST.get('name')
        data.age = request.POST.get('age')
        data.gender = request.POST.get('gender')
        data.location = request.POST.get('location')
        data.natureofjob = request.POST.get('natureofjob')
        data.phone =  request.POST.get('phone')
        photo=request.FILES['photo']
        fs=FileSystemStorage()
        filename=fs.save(photo.name,photo)
        uploaded_file_url=fs.url(filename)
        data.photo=uploaded_file_url
        data.email = request.POST.get('email')
        data.status="notverified"
        data.save()

        data1 = tbl_idgen.objects.get(id=1)
        data1.vid = request.session['vid']
        data1.save()

        data1=tbl_login()
        data1.username=data.volunteer_id
        data1.password=data.phone
        data1.catagory="volunteer"
        data1.save()

        return redirect('/publicvolunteerregistration')
# inserting into tbl_beneficiar from public
def publicbeneficiarregistration(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.bid
    id = int(id+1)
    bid = "BID_00" + str(id)
    request.session['bid'] = id 
    return render(request,"publicbeneficiarregistration.html",{'bid':bid})
def publicinsertbeneficiar(request):
    if request.method == 'POST':
       data = tbl_beneficiar()
       data.beneficiar_id = request.POST.get('beneficiar_id')
       data.name = request.POST.get('name')
       data.location = request.POST.get('location')
       data.address = request.POST.get('address')
       data.contact_person = request.POST.get('phone1')
       data.pincode = request.POST.get('pincode')
       data.phone = request.POST.get('phone')
       data.email = request.POST.get('email')
       data.status = "notverified"
       photo = request.FILES['proof']
       fs = FileSystemStorage()
       filename = fs.save(photo.name,photo)
       uploaded_file_url = fs.url(filename)
       data.proof = uploaded_file_url
       data.description = request.POST.get('description')
       data.save()

       data1 = tbl_idgen.objects.get(id=1)
       data1.bid = request.session['bid']
       data1.save()
       
       return render(request,"login.html",{'data':1})

#admin directly insert into tbl_benefeciar
def adminvolunteerregistration(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.vid
    id = int(id+1)
    vid = "VID_00" + str(id)
    request.session['vid'] = id 
    return render(request,"adminvolunteerregistration.html",{'vid':vid})
def admininsertvolunteer(request):
    if request.method == 'POST':
        data=tbl_volunteers()
        data.volunteer_id = request.POST.get('volunteer_id')
        data.name = request.POST.get('name')
        data.age = request.POST.get('age')
        data.gender = request.POST.get('gender')
        data.location = request.POST.get('location')
        data.natureofjob = request.POST.get('natureofjob')
        photo=request.FILES['photo']
        fs=FileSystemStorage()
        filename=fs.save(photo.name,photo)
        uploaded_file_url=fs.url(filename)
        data.photo=uploaded_file_url
        data.phone = request.POST.get('phone')
        data.email = request.POST.get('email')
        data.status="verified"
        data.save()

        data1 = tbl_idgen.objects.get(id=1)
        data1.vid = request.session['vid']
        data1.save()

        data1=tbl_login()
        data1.username=data.volunteer_id
        data1.password=data.phone
        data1.catagory="volunteer"
        data1.save()


        return redirect('/adminvolunteerregistration')
# admin remove voldata=catagory.objects.get(id=id1)
def adminvolunteerviewremove(request):
    data = tbl_volunteers.objects.filter(status="verified")
    return render(request,"adminvolunteerviewremove.html",{'data':data})

def removevolunteer(request,name):
        data=tbl_volunteers.objects.get(name=name)
        data.delete()
        return redirect('/adminvolunteerviewremove')


 # admin accept or reject volunteers
def adminvolunteerviewverification(request):
    data = tbl_volunteers.objects.filter(status="notverified")
    return render(request,"adminvolunteerviewverification.html",{'data':data})

def accept(request,id1):
    data = tbl_volunteers.objects.get(volunteer_id=id1)
    data.status="verified"
    data.save()


    data1=tbl_login()
    data1.username=data.volunteer_id
    data1.password=data.phone
    data1.catagory="volunteer"
    data1.save()
    return redirect('/adminvolunteerviewverification')

def reject(request,id1):
    data = tbl_volunteers.objects.get(volunteer_id=id1)
    data.delete()
    return redirect('/adminvolunteerviewverification')

#admin verify benefeciar
def adminverifybeneficiar(request):
    data = tbl_beneficiar.objects.filter(status="notverified")
    return render(request,"adminverifybeneficiar.html",{'data':data})

def accept_beneficiar(request,bid):
    data = tbl_beneficiar.objects.get(beneficiar_id = bid)
    data.status = "verified"
    data.save()
    
    data1=tbl_login()
    data1.username=data.email
    data1.password=data.phone
    data1.catagory="beneficiar"
    data1.save()

    email=data.email
    request.session['s1']=email
    link = "<a href='http://192.168.112.176:8000/login/'>Login now</a>"
    send_mail('Verified Beneficiar:FoodExtra','Successfully Verified as Beneficiar\nUse below username and Password to login\n''username:\t'+data1.username+'\nPassword:'+data1.password+ '\nClick to login'+link,'from@example.co',[email,])

    return redirect('/adminverifybeneficiar')

def reject_beneficiar(request,bid):
    data = tbl_beneficiar.objects.get(beneficiar_id = bid)
    data.delete()

    data2 = tbl_login.objects.get(beneficiar_id = bid)
    return redirect('/adminverifybeneficiar')

#admin remove beneficiar
def adminremovebeneficiar(request):
    data = tbl_beneficiar.objects.filter(status="verified")
    return render(request,"adminremovebeneficiar.html",{'data':data})  

def removebeneficiar(request,id1):
    data = tbl_beneficiar.objects.get(beneficiar_id=id1)
    data.delete()
    data1 = tbl_login.objects.get(beneficiar_id=id1)
    data1.delete()
    email=data.email
    request.session['s1']=email
    send_mail('Beneficiary account removed:FoodExtra','Your Beneficiary account was removed by admin due to violation of our terms,if you think thats a mistake kindly contact us:\nPhone:\t7594066757\nEmail:\tfoodextra.in@gmail.com','from@example.co',[email,])

    return redirect('/adminremovebeneficiar')

#volunteer's activities
def volunteers(request):
    volunteer_id=request.session['vlid']
    return render(request,"volunteers.html")

def orderstatus(request):
    return render(request,"orderstatus.html")


def orderstatuspublicdon(request):
    
    return render(request,"orderstatuspublicdon.html")

def orderstatuspublicdontable(request):
    d=request.POST.get('phone')
    data=tbl_publicrequest.objects.filter(phone=d)

    return render(request,"orderstatuspublicdontable.html",{'data':data})



#beneficiar's activities
#home
def beneficiars(request):
    beneficiar_id = request.session['bnid']
    return render(request,"beneficiars.html")    


#beneficiar give review



    

# login 
def login(request):
    return render(request,"login.html")

def log(request):
    if request.method == "POST":
        data=tbl_login.objects.all()
        user=request.POST.get('username')
        pwd=request.POST.get('password')

        flag=0
        for da in data:
            if user==da.username and pwd==da.password:
                type=da.catagory
                flag = 1
                if type=="admin":
                    return render(request,"admin1.html")
                elif type=="donor":
                    d=tbl_donor.objects.get(email=user)
                    request.session['did']=d.donor_id

                    return render(request,"donor.html")
                elif type=="beneficiar":
                    d=tbl_beneficiar.objects.get(email=user)
                    request.session['bnid']=d.beneficiar_id
                    
                    return render(request,"beneficiaryhome.html")   
                else:
                    return HttpResponse("Invalid acc type")
        if flag==0:
            return HttpResponse("Invalid user")
#pulic donating food 
def fooddonation(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.fid
    id = int(id+1)
    fid = "FDID_00" + str(id)
    request.session['fid'] = id   
    return render(request,"fooddonation.html",{'fid':fid})

def publicinsertdonation(request):
    if request.method =='POST':
        data = tbl_fooddonation()
        data.donor_id = request.POST.get('donor_id')
        data.name = request.POST.get('name')
        data.address = request.POST.get('address')
        data.pincode = request.POST.get('pincode')
        data.location = request.POST.get('location')
        data.phone = request.POST.get('phone')
        data.email = request.POST.get('email')
        data.foodcatagory = request.POST.get('foodcatagory')
        data.quatity = request.POST.get('quatity')
        data.description = request.POST.get('Description')
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name,photo)
        uploaded_file_url = fs.url(filename)
        data.photo = uploaded_file_url
        data.preparation_time = request.POST.get('preparationtime')
        data.date = request.POST.get('date')
        data.required_time = request.POST.get('requiredtime')
        data.remark = request.POST.get('remark')
        data.status = "pending"
        data.save()

        data1 = tbl_idgen.objects.get(id=1)
        data1.fid = request.session['fid']
        data1.save()

        return render(request,'orderstatuspublicdon.html',{'data':1})


#public select which type of food        

            
#benefeciar select which type of food required
def beneficiarselectcatagory(request):
    return render(request,"beneficiarselectcatagory.html")

def beneficiarviewavailability(request):
    if request.method=='POST':
        n2 = request.POST.get('foodcatagory')
        data = tbl_fooddonation.objects.filter(foodcatagory=n2)
        return render(request,'beneficiarviewavailability.html',{'data':data})
    
def beneficiargeneraterequest(request,id1):
    data = tbl_idgen.objects.get(id=1)
    id = data.brid
    id = int(id+1)
    brid = "BRID_00" + str(id) 
    request.session['brid'] = id 
    bnid =  request.session['bnid']
    return render(request,"beneficiarrequest.html",{'brid':brid,'fid':id1,'bnid':bnid})

#beneficar request food
def beneficiarinsertfoodrequest(request):
    if request.method == 'POST':
        data = tbl_benefeciarrequest()
        data.request_id = request.POST.get('request_id')
        data.donor_id_id = request.POST.get('donor_id')
        data.beneficiar_id_id = request.POST.get('beneficiar_id')
        data.required_date = request.POST.get('required_date')
        data.required_time = request.POST.get('required_time')
        data.required_quatity = request.POST.get('required_quatity')
        data.remark = request.POST.get('remark')
        data.status = "pending"
        data.save()

        data1 = tbl_idgen.objects.get(id=1)
        data1.brid = request.session['brid']
        data1.save()
        return redirect('/beneficiarselectcatagory')


def adminviewcomplaint(request):
    data = tbl_complaint.objects.all()
    return render(request,"adminviewcomplaint.html",{'data':data})

def adminpublicrequestprocess(request):
    data = tbl_publicrequest.objects.filter(status="pending")
    return render(request,"adminpublicrequestprocess.html",{'data':data})

def accept(request,id1):
    data = tbl_publicrequest.objects.get(request_id=id1)
    data.status = "accepted"
    data.save()
    return redirect('/adminpublicrequestprocess')

def reject(request,id1):
    data = tbl_publicrequest.objects.get(request_id=id1)
    data.status ="rejected"
    data.save()
    return redirect('/adminpublicrequestprocess')

def admindutyallotment(request):
    data = tbl_benefeciarrequest.objects.filter(status="pending")
    return render(request,"admindutyallotment.html",{'data':data})
#admin accept or beneficiar request
def accept_beneficiarrequest(request,id1):
    data = tbl_benefeciarrequest.objects.get(request_id=id1)
    did = data.donor_id_id
    qty = data.required_quatity
    data.status = "accepted"
    data.save()

    data2 = tbl_volunteers.objects.all()

    data1 = tbl_idgen.objects.get(id=1)
    id = data1.alid
    id = int(id+1)
    alid = "ALID_00" + str(id) 
    request.session['alid'] = id 
    return render(request,'adminbeneficiarfoodallot.html',{'alid':alid,'rid':id1,'did':did,'qty':qty,'data2':data2})

def adminallotfoodbeneficiars(request):
    if request.method == 'POST':
        data = tbl_benefeciarfoodallot()
        data.allotment_id = request.POST.get('allotment_id')
        data.request_id_id = request.POST.get('request_id')
        data.donor_id_id = request.POST.get('donor_id')
        data.request_quatity = request.POST.get('request_quatity')
        data.allotment_quatity = request.POST.get('allotment_quatity')
        data.remark = request.POST.get('remark')
        data.volunteer_id_id = request.POST.get('volunteers')
        data.allotment_date = request.POST.get('allotment_date')
        data.allotment_time = request.POST.get('allotment_time')
        data.save()
        

        data1 = tbl_idgen.objects.get(id=1)
        data1.alid = request.session['alid']
        data1.save()
        return redirect('/adminbeneficiarfoodallot')


def reject_beneficiarrequest(request):
    data = tbl_beneficiarrequest.objects.get(request_id=id1) 
    data.status = "rejected"
    data.save()
    return redirect('/admindutyallotment') 

def publicrequesttypeselect(request):
     return render(request,"publicfoodrequest.html")

def viewfooddonation(request):
    category=request.POST.get('foodcatagory')
    pincode=request.POST.get('pincode')
    print(category)
    data=tbl_fooddonation.objects.filter(pincode=pincode).filter(foodcatagory=category)
    print("ddddddddddddddddddd")
    print(data)
    return render(request,"viewfooddonation.html",{'data':data})


def foodrequest(request,id):
    #do="DID_001"
    data=tbl_fooddonation.objects.get(donation_id=id)
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.prid
    id = int(id+1)
    prid = "REQUEST_00" + str(id) 
    request.session['prid1'] = prid 
    request.session['prid'] = id 
    return render(request,"publicfoodconfirm.html",{'data':data,'id':prid})

def publicrequestupdation(request,id):
    # donation_id="FDID_002"
    data=tbl_publicrequest()
    data.request_id =request.session['prid1']
    d=tbl_fooddonation.objects.get(donation_id=id)
    data.donor_id_id=d.donor_id_id
    data.donation_id_id = id
    data.request_food = request.POST.get('food')
    data.location = request.POST.get('location')
    data.phone = request.POST.get('phone')
    data.email = request.POST.get('email')
    data.contact_person= request.POST.get('name')
    data.quantity= request.POST.get('quantity')
    data.status="pending"
    data.save()
    data1 = tbl_idgen.objects.get(id=1)
    data1.prid = request.session['prid']
    data1.save()
   # send_mail('CONFIRMATION','REQUEST GENERATED','from@example.co',[items.Email,])
    return render(request,"orderstatuspublicdon.html",{'data':2})
    
def beneficiaryhome(request):
    return  render (request,"beneficiaryhome.html")

def beneficiaryfoodreq(request):
    data=tbl_beneficiar.objects.get(beneficiar_id=request.session['bnid'])
    pincode = data.pincode
    return render (request,"beneficiaryfoodreq.html",{'data':pincode})
    
def beneficiaryfoodreqcomplete(request):
    category=request.POST.get('foodcatagory')
    pincode=request.POST.get('pincode')
    print(category)
    data=tbl_fooddonation.objects.filter(foodcatagory=category).filter(pincode=pincode)
    return render(request,"benviewdonation.html",{'data':data})
#edithere
def benfoodrequest(request,id):

    data=tbl_fooddonation.objects.get(donation_id=id)
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.brid
    id = int(id+1)
    brid = "REQUEST_00" + str(id) 
    request.session['brid1'] = brid 
    request.session['brid'] = id 
    print("ggggggggggggggggggggg"+request.session['bnid'])
    return render(request,"benfoodconfirm.html",{'data':data,'id':brid})

def benrequestupdation(request,id):
    data=tbl_benefeciarrequest()
    data.request_id =request.session['brid1']
    data.donation_id_id = id
    data5=tbl_fooddonation.objects.get(donation_id=id)
    data.donor_id_id=data5.donor_id_id
    data.beneficiar_id_id = request.session['bnid']
    data.required_date= datetime.datetime.now().strftime ("%Y-%m-%d")
    data.required_time= datetime.datetime.now().strftime('%H:%M:%S')
    data.required_quatity= request.POST.get('quantity')
    data.remark = request.POST.get('remark')
    data.status="pending"
    data.save()
    data1 = tbl_idgen.objects.get(id=1)
    data1.brid = request.session['brid']
    data1.save()
    return redirect('/beneficiaryhome')
    #return render(request,"index.html")

def beneficiarycompl(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.cid
    id = int(id+1)
    cid = "CID_00" + str(id)
    request.session['cid'] = id
    return render(request,"beneficiarycompl.html",{'cid':cid})

def beneficiarycomplupdate(request):
    data=tbl_complaint()
    data.complaint_id =request.POST.get('complaint_id')
    data.complaint =request.POST.get('complaint')
    data.beneficiar_id_id=request.session['bnid']
    data.date =datetime.datetime.now().strftime ("%Y-%m-%d")
    data.save()

    data1 = tbl_idgen.objects.get(id=1)
    data1.cid = request.session['cid']
    data1.save()

    return render(request,"beneficiaryhome.html")

def beneficiaryreview(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.rid
    id = int(id+1)
    rid = "RID_00" + str(id)
    request.session['rid'] = id
    return render(request,"beneficiaryreview.html",{'rid':rid})

def beneficiaryreviewupdate(request):
    data=tbl_review()
    data.review_id =request.POST.get('review_id')
    data.review =request.POST.get('review')
    data.beneficiar_id_id=request.session['bnid']
    data.date =datetime.datetime.now().strftime ("%Y-%m-%d")
    data.save()

    data1 = tbl_idgen.objects.get(id=1)
    data1.rid = request.session['rid']
    data1.save()
    

    return render(request,"beneficiaryhome.html")

def adminpublicfoodrequest(request):
    data = tbl_publicrequest.objects.filter(status="pending")
    return render(request,"adminpublicviewreq.html",{'data':data})

def adminbeneficiaryfoodreq(request):
   data = tbl_benefeciarrequest.objects.filter(status="pending")
   return render(request,"adminbeneficiaryviewreq.html",{'data':data})
 
def acceptpublicfoodreq(request,id2):
    data = tbl_publicrequest.objects.get(request_id=id2)
    data.status="accepted"
    data.save()

    email=data.email
    request.session['s1']=email
    send_mail('Food is Ready','Food is Ready\nDonor Details:\n''Name:\t'+data.donation_id.donor_id.organization_name+ '\nPhone:'+data.donation_id.donor_id.phone+ '\nAddress:'+data.donation_id.donor_id.address ,'from@example.co',[email,])

    return redirect('/adminpublicfoodrequest')

def rejectpublicfoodreq(request,id3):
    data = tbl_publicrequest.objects.get(request_id=id3)
    data.status="rejected"
    data.save()

    email=data.email
    request.session['s1']=email
    send_mail('Rejected','Sorry we cannot process your food request now due to Incorrect/Improper details entered.\nPlease try again with exact details. Still facing issues? reach out to us at foodextra.in@gmail.com','from@example.co',[email,])

    return redirect('/adminbeneficiaryfoodreq')

def acceptbeneficiaryfoodrequest(request,id4):
    data = tbl_benefeciarrequest.objects.get(request_id=id4)
    data.status="accepted"
    data.save()
    # donor_name=id4.donor_id_id.name
    email=data.beneficiar_id.email
    request.session['s1']=email
    send_mail('Food is Ready','Donor Details:\n''Name:\t'+data.donation_id.donor_id.organization_name+ '\nPhone:'+data.donation_id.donor_id.phone+ '\nAddress:'+data.donation_id.donor_id.address ,'from@example.co',[email,])
    # send_mail('change','Your food request has been accepted\nDonor details has been given below:\nName:'+donor_name 'Click to login'+link,'from@example.co',[email,])


    return redirect('/adminbeneficiaryfoodreq')

def rejectbeneficiaryfoodrequest(request,id5):
    data = tbl_benefeciarrequest.objects.get(request_id=id5)
    data.status="rejected"
    data.save()

    return redirect('/adminbeneficiaryfoodreq')



def beneficiaryfoodstatus(request):
    beneficiaryid=request.session['bnid']
    data= tbl_benefeciarrequest.objects.filter(beneficiar_id=beneficiaryid)
    return render(request,"beneficiaryfoodstatus.html",{'data':data})

def donordonationstatus(request):
    donor_id=request.session['did']
    data= tbl_fooddonation.objects.filter(donor_id_id=request.session['did'])
    #data2= tbl_benefeciarrequest.objects.filter(donor_id_id=donor_id)
    return render(request,"donorstatus.html",{'data':data})



def admindonation(request):
    data = tbl_fooddonation.objects.filter(status ="pending")
    return render(request,"admindonation.html",{'data':data})

def accept_food(request,id6):
    data = tbl_fooddonation.objects.get(donation_id = id6)
    data.status = "verified"
    data.save()

    return redirect('/admindonation')

def publicdonorregistration(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.did
    id = int(id+1)
    did = "DID_00" + str(id)
    request.session['did'] = id 

    return render(request,"publicdonorregistration.html",{'data':did})

def publicinsertdonor(request):
    if request.method == 'POST':
       data = tbl_donor()
       data.donor_id = request.POST.get('donor_id')
       data.organization_name = request.POST.get('name')
       data.person_in_charge_name = request.POST.get('Person in charge')
       data.pincode = request.POST.get('pincode')
       data.address = request.POST.get('address')
       data.phone = request.POST.get('phone')
       data.alternative_phone = request.POST.get('phone1')
       data.email = request.POST.get('email')
       data.status = "notverified"
       photo = request.FILES['proof']
       fs = FileSystemStorage()
       filename = fs.save(photo.name,photo)
       uploaded_file_url = fs.url(filename)
       data.proof = uploaded_file_url
       data.save()

       data1 = tbl_idgen.objects.get(id=1)
       data1.did = request.session['did']
       data1.save()


       data1=tbl_login()
       data1.username=data.donor_id
       data1.password=data.phone
       data1.catagory="donor"
       data1.save()

       return render(request,"login.html",{'data':1})

def forget(request):
    return render(request,"forget.html")
def forget2(request):
    return render(request,"forget1.html") 
def forget1(request):
    
    email=request.POST.get('username')
    request.session['s1']=email
    link = "<a href='http://http://192.168.112.176:8000//forget1/'>Click To Reset password</a>"
    send_mail('change','username'+link,'from@example.co',[email,])
    return render(request,"login.html") 

def forget3(request):
    print("ddddddddddddddddddddddddddddddddd")
    print(request.session['s1'])
    username=request.session['s1']
    data=tbl_login.objects.get(username=username)   
    data.password=request.POST.get('password')
    data.save()
    return render(request,"login.html") 

# admin verify donor
def adminverifydonor(request):
    data = tbl_donor.objects.filter(status="notverified")
    return render(request,"adminverifydonor.html",{'data':data})

def accept_donor(request,did):
    data = tbl_donor.objects.get(donor_id = did)
    data.status = "verified"
    data.save()
    
    data1=tbl_login()
    data1.username=data.email
    data1.password=data.phone
    data1.catagory="donor"
    data1.save()

    email=data.email
    request.session['s1']=email
    link = "<a href='http://192.168.112.176:8000/login/'>Login now</a>"
    send_mail('FoodXtra','Successfully Verified as Donor\nUse below username and Password to login\n''username:\t'+data1.username+'\nPassword:'+data1.password+ '\nClick to login'+link,'from@example.co',[email,])

    return redirect('/adminverifydonor')

def reject_donor(request,did):
    data = tbl_donor.objects.get(donor_id = did)
    email=data.email
    data.delete()

    
    request.session['s1']=email
    # link = "<a href='http://192.168.112.176:8000/index/'>Foodextra</a>"
    send_mail('Removed:Foodextra','Your request become donor has been rejected by Foodextra due to inproper/insufficient details.\nIf you still think its our mistake,pls contact us:\nPhone:\t7594066757\nEmail:\tfoodextra.in@gmail.com','from@example.co',[email,])

    return redirect('/adminverifydonor')

def adminremovedonor(request):
    data = tbl_donor.objects.filter(status="verified")
    return render(request,"adminremovedonor.html",{'data':data})  

def removedonor(request,id1):
    data = tbl_donor.objects.get(donor_id=id1)
    email=data.email
    data.delete()

    request.session['s1']=email
    send_mail('Donor account removed:FoodExtra','Your Donor account was removed by admin due to violation of our terms,if you think thats a mistake kindly contact us:\nPhone:\t7594066757\nEmail:\tfoodextra.in@gmail.com','from@example.co',[email,])

    return redirect('/adminremovedonor')

#donor page
def donorhome(request):
    beneficiar_id = request.session['bnid']
    return render(request,"donor.html")

def donordonation(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.fid
    id = int(id+1)
    fid = "FDID_00" + str(id)
    request.session['fid'] = id   
    return render(request,"donordonation.html",{'fid':fid})

def donorinsertdonation(request):
    if request.method =='POST':
        data = tbl_fooddonation()
        data.donation_id = request.POST.get('donation_id')
        data.donor_id_id=request.session['did']
        data.foodcatagory = request.POST.get('foodcatagory')
        data.quantity = request.POST.get('quatity')
        data.name = request.POST.get('name')
        d=tbl_donor.objects.get(donor_id=request.session['did'])
        data.pincode=d.pincode
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name,photo)
        uploaded_file_url = fs.url(filename)
        data.photo = uploaded_file_url
        data.preparation_time = request.POST.get('preparationtime')
        data.date = request.POST.get('date')
        data.required_time = request.POST.get('requiredtime')
        data.remark = request.POST.get('remark')
        data.status = "pending"
        data.save()

        data1 = tbl_idgen.objects.get(id=1)
        data1.fid = request.session['fid']
        data1.save()

        return render(request,'donor.html',{'data':1})

def donations(request):
    data=tbl_benefeciarrequest.objects.filter(donor_id_id=request.session['did'])
    return render(request,"donation.html",{'data':data})
def editquantity(request,id):
    return render(request,'editquantity.html',{'id':id})
def edit(request,id):
    data=tbl_fooddonation.objects.get(donation_id=id)
    data.quantity=request.POST.get('qty')
    data.save()
    return redirect('/donordonationstatus')

#donor remove food

def donorremovefood(request,id2):
    data = tbl_fooddonation.objects.get(donation_id=id2)
    data.delete()

    return redirect('/donordonationstatus')

def publicpickup(request):
    donor_id = request.session['did']
    data = tbl_publicrequest.objects.filter(donor_id_id=donor_id)
    return render(request,'publicpickup.html',{'data':data})

def publicreview(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.alid
    id = int(id+1)
    data.alid=id
    alid = "GUEST_00" + str(id)
    request.session['alid']= id
    return render(request,"publicreview.html",{'data':alid})

def publicreviewinsert(request):
    data=tbl_publicreview()
    data.publicreview_id =request.POST.get('publicreview_id')
    data.phone =request.POST.get('phone')
    data.review =request.POST.get('review')
    data.date =datetime.datetime.now().strftime ("%Y-%m-%d")
    data.save()

    return render(request,"index.html")

def admincomplaint(request):
    data=tbl_complaint.objects.filter()

    return render(request,"admincomplaint.html",{'data':data})

def donorcomplaint(request):
    data=tbl_donorcomplaint.objects.filter()
    
    return render(request,"donorcomplaint.html",{'data':data})

#donor page compl
def donorcompl(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.dcid
    id = int(id+1)
    dcid = "DCID_00" + str(id)
    request.session['dcid'] = id
    return render(request,"donorcompl.html",{'dcid':dcid})

def donorcomplupdate(request):
    data=tbl_donorcomplaint()
    data.complaint_id =request.POST.get('complaint_id')
    data.complaint =request.POST.get('complaint')
    data.donor_id_id_id=request.session['did']
    data.date =datetime.datetime.now().strftime ("%Y-%m-%d")
    data.save()

    data1 = tbl_idgen.objects.get(id=1)
    data1.dcid = request.session['dcid']
    data1.save()

    return render(request,"donor.html")

def donorreview(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.drid
    id = int(id+1)
    drid = "DRID_00" + str(id)
    request.session['drid'] = id
    return render(request,"donorreview.html",{'drid':drid})

def donorreviewupdate(request):
    data=tbl_donorreview()
    data.review_id =request.POST.get('review_id')
    data.review =request.POST.get('review')
    data.donor_id_id=request.session['did']
    data.date =datetime.datetime.now().strftime ("%Y-%m-%d")
    data.save()

    data1 = tbl_idgen.objects.get(id=1)
    data1.rid = request.session['drid']
    data1.save()
    return render(request,"donor.html")

def publicre(request):
    data=tbl_publicreview.objects.filter()
    
    return render(request,"publicre.html",{'data':data})
     
def donorre(request):
    data=tbl_donorreview.objects.filter()
    
    return render(request,"donorre.html",{'data':data})

def benre(request):
    data=tbl_review.objects.filter()
    
    return render(request,"benre.html",{'data':data})

def indextesting(request):
    return render(request,"indextesting.html")

# def logout_request(request):
#     nadiya if 'uid' not in request.session:
#         return render(request,"index.html")
#     else:
# def amlogout(request):
#     del request.session['amuid']
#     return render(request,"index.html")


def profile(request):
    return render(request,"profile.html")