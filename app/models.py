from django.db import models
# Create your models here.

#public donor registration
class tbl_donor(models.Model):
    donor_id = models.CharField(max_length=90,primary_key=True)
    organization_name = models.CharField(max_length=90)
    person_in_charge_name = models.CharField(max_length=90)
    address = models.CharField(max_length=90)
    phone = models.CharField(max_length=90)
    alternative_phone = models.CharField(max_length=90)
    pincode = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    description = models.CharField(max_length=90)  
    status = models.CharField(max_length=90)
    proof = models.CharField(max_length=90) 

class Meta:
        db_table="tbl_donor"

#public volunteer registration
class tbl_volunteers(models.Model):
    volunteer_id = models.CharField(max_length=90,primary_key=True)
    name = models.CharField(max_length=90)
    age = models.CharField(max_length=90)
    gender = models.CharField(max_length=90)
    location = models.CharField(max_length=90)
    natureofjob = models.CharField(max_length=90)
    photo = models.CharField(max_length=90)
    email = models.CharField(max_length=90) 
    phone = models.CharField(max_length=90) 
    status = models.CharField(max_length=90) 

class Meta:
        db_table="tbl_volunteers"
 
# id generation
class tbl_idgen(models.Model):
    vid = models.IntegerField()
    did = models.IntegerField()
    bid = models.IntegerField()
    fid = models.IntegerField()
    prid = models.IntegerField() 
    rid = models.IntegerField()     #ben rev
    drid = models.IntegerField()  #donor revw
    alid = models.IntegerField() #public revie
    cid = models.IntegerField()  #ben cmpl  
    dcid = models.IntegerField()  #dnr cmpl
    brid = models.IntegerField() 
    
class Meta:
        db_table="tbl_idgen"


#public beneficiar registration
class tbl_beneficiar(models.Model):
    beneficiar_id = models.CharField(max_length=90,primary_key=True)
    name = models.CharField(max_length=90)
    description = models.CharField(max_length=90)
    location = models.CharField(max_length=90)
    address = models.CharField(max_length=90)
    contact_person = models.CharField(max_length=90)
    phone = models.CharField(max_length=90)
    email = models.CharField(max_length=90)  
    status = models.CharField(max_length=90) 
    pincode = models.CharField(max_length=90)
    proof = models.CharField(max_length=90)

class Meta:
        db_table="tbl_beneficiar"
    
#login lable

class tbl_login(models.Model):
    username=models.CharField(max_length=90)
    password=models.CharField(max_length=90)
    catagory=models.CharField(max_length=90)

class Meta:
        db_table="tbl_login"

#public food donation

class tbl_fooddonation(models.Model):
    donation_id = models.CharField(max_length=90,primary_key=True)
    donor_id = models.ForeignKey(tbl_donor,on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    foodcatagory = models.CharField(max_length=90)
    quantity = models.CharField(max_length=90)
    photo = models.CharField(max_length=90)
    preparation_time = models.CharField(max_length=90)
    date = models.CharField(max_length=90)
    required_time = models.CharField(max_length=90)
    remark = models.CharField(max_length=90)
    status = models.CharField(max_length=90)
    pincode = models.CharField(max_length=90)


    class Meta:
        db_table="tbl_fooddonation"

#public request

class tbl_publicrequest(models.Model):
    request_id = models.CharField(max_length=90,primary_key=True)
    donation_id = models.ForeignKey(tbl_fooddonation,on_delete=models.CASCADE)
    location = models.CharField(max_length=90)
    phone = models.CharField(max_length=90)
    contact_person = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    request_food = models.CharField(max_length=90)
    remark = models.CharField(max_length=90)  
    status = models.CharField(max_length=90)
    quantity= models.CharField(max_length=30)
    donor_id = models.ForeignKey(tbl_donor,on_delete=models.CASCADE)


    class Meta:
        db_table="tbl_publicrequest"
#beneficiar give review
class tbl_review(models.Model):
    review_id = models.CharField(max_length=90,primary_key=True)
    beneficiar_id = models.ForeignKey(tbl_beneficiar,on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    review = models.CharField(max_length=90)
    date = models.CharField(max_length=90)
    address = models.CharField(max_length=90)
      

    class Meta:
        db_table="tbl_review"

class tbl_donorreview(models.Model):
    review_id = models.CharField(max_length=90,primary_key=True)
    donor_id = models.ForeignKey(tbl_donor,on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    review = models.CharField(max_length=90)
    date = models.CharField(max_length=90)
    address = models.CharField(max_length=90)
      

    class Meta:
        db_table="tbl_donorreview"

class tbl_complaint(models.Model):
    complaint_id = models.CharField(max_length=90,primary_key=True)
    complaint = models.CharField(max_length=90)
    beneficiar_id = models.ForeignKey(tbl_beneficiar,on_delete=models.CASCADE)
    date = models.CharField(max_length=90)
    status = models.CharField(max_length=90)
     

    class Meta:
        db_table="tbl_complaint"

class tbl_donorcomplaint(models.Model):
    complaint_id = models.CharField(max_length=90,primary_key=True)
    complaint = models.CharField(max_length=90)
    donor_id_id = models.ForeignKey(tbl_donor,on_delete=models.CASCADE)
    date = models.CharField(max_length=90)
    status = models.CharField(max_length=90)
     

    class Meta:
        db_table="tbl_donorcomplaint"
    
#beneficiar check food availability

class tbl_benefeciarrequest(models.Model):
    request_id = models.CharField(max_length=90,primary_key=True)
    donation_id = models.ForeignKey(tbl_fooddonation,on_delete=models.CASCADE)
    donor_id = models.ForeignKey(tbl_donor,on_delete=models.CASCADE)
    beneficiar_id =  models.ForeignKey(tbl_beneficiar,on_delete=models.CASCADE)
    required_date = models.CharField(max_length=90)
    required_time = models.CharField(max_length=90)
    required_quatity = models.CharField(max_length=90)
    remark = models.CharField(max_length=90)
    status = models.CharField(max_length=90)

    class Meta:
        db_table="tbl_benefeciarrequest"

class tbl_beneficiarfoodallot(models.Model):
    allotment_id = models.CharField(max_length=90,primary_key=True)
    request_id = models.ForeignKey(tbl_benefeciarrequest,on_delete=models.CASCADE)
    donation_id = models.ForeignKey(tbl_fooddonation,on_delete=models.CASCADE)
    request_quatity = models.CharField(max_length=90)    
    allotment_quatity =  models.CharField(max_length=90)
    remark = models.CharField(max_length=90)
    volunteer_id = models.ForeignKey(tbl_volunteers,on_delete=models.CASCADE)
    allotment_date = models.CharField(max_length=90)
    allotment_time =models.CharField(max_length=90)
    status = models.CharField(max_length=90)


    class Meta:
        db_table="tbl_beneficiarfoodallot"


class tbl_publicreview(models.Model):
    publicreview_id = models.CharField(max_length=90,primary_key=True)
    phone = models.CharField(max_length=90)
    review = models.CharField(max_length=90)
    date = models.CharField(max_length=90)      

    class Meta:
        db_table="tbl_publicreview"



