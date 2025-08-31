#PROJECT SHARDA HOSPITAL MANAGEMENT

def main_menu():

    print("*********************************************************")
    print("*********************************************************")
    print("*******************WELCOME*******************************")
    print("**********************TO*********************************")
    print("***************SHARDA HOSPITAL***************************")
    print("*********************************************************")
    print("*********************************************************")

main_menu()

#put everything in while

print("SELECT                       FOR")
print(    "1"    "\t" "\t" "\t"                    "APPOINTMENT")
print(    "2"    "\t" "\t" "\t"                    "DOCTOR")
print(    "3"    "\t" "\t" "\t"                    "PATIENT")
print(    "4"    "\t" "\t" "\t"                    "PAYMENT")
print(    "5"    "\t" "\t" "\t"                    "NOTICE")
print(    "6"    "\t" "\t" "\t"                    "ABOUT HOSPITAL")
print("-"*40)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

print("-"*40)
jk=True
while jk==True:  
    select=int(input("ENTER THE DESIRED OPTION   :"))

    if select==1:
        appointment()
    elif select==2:
        doc()
    elif select==3:
        patient()
    elif select==4:
        payment()
    elif select==5:
        notice()
    elif select==6:
        about()  
    else:
        print("********************************THANK YOU********************************")
    ans=input("TO KEEP REPEATING PRESS 'Y' ")
    if ans=="Y":
        continue
    else:
        break
        
     
 #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        
 #to create a file before appendinfd new data
def appointment_entry():
    jk=True
    while jk==True:
        print("-"*40)
        print("---------------APPOINTMENT------------------")
        print("-"*40)

        f2=open("appointment.txt","a") #is it possible to create any file throuh append mode?
        print("-"*40)
        n=input("ENTER THE PATIENT NAME         :")
        ag=input("ENTER THE PATIENT AGE         :")
        pn=input("ENTER THE PHONE NUMBER        :")
        s=input("ENTER THE PATIENT SEX          :")
        add=input("ENTER THE PATIENT ADDRESS    :")
        date=input("ENTER THE DATE              :")
        
        print("-"*40)
        
        f2.append("\n\n")
        f2.append("n\n")
        f2.append("ag\n")
        f2.append("pn\n")
        f2.append("s\n")
        f2.append("add\n")
        
        f2.close()
        ans=input("TO KEEP REPEATING PRESS 'Y' ")
        if ans=="Y":
            continue
        else:
            break 
def appointment_watch():
    print("-"*40)
    print("---------------APPOINTMENT------------------")
    print("-"*40)
    f=open("appointment.txt","r")
    f.read()
    f.close()

def appointment():
    print("Type 1 to enter new appointment    :")
    print("Type 2 to see previous appointments:")
    b=int(input("ENTER THE DESIRED OPTION     :"))
    if b==1:
        appointment_watch()
        
    else:
        appointment_entry()
        
  
    
    
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
    
    
    
    
docfile=open("doc.txt","a")  
def doc():  #this fuction is for adding new doctor in hosapital
    jk=True
    while jk==True:
        
        docname=input("ENTER THE NAME OF DOCTOR    :")
        spclst=input("ENTERB THE BRANCH            :")
        time=input("ENTER THE TIME OF DOCTOR       :")
        
        print("-"*40)
         
        docfile.append("\n\n")
        docfile.append("docname")
        docfile.append("spclst")
        docfile.append("time")
        
        docfile.close()
        
        ans=input("TO KEEP REPEATING PRESS 'Y'  : ")
        if ans=="Y" or ans=="y":
            continue
        else:
            exit()




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

patient=open("patient.txt","a")
def patient():
    jk=True
    while jk==True:
       
        name=input("ENTER THE NAME OF PATIENT     :")
        age=int(input("ENTER THE AGE OF PATIENT   :"))
        sex=int(input("ENTER THE GENDER           :"))
        date=input("ENETR THE DATE                :")
        room_no=int(input("ENTER THE ROOM NUMBER  :"))
        floor_no=int(input("ENTER THE FLOOR NUMBER:"))
        
        print("-"*40)
        
        patient.append("\n\n")
        patient.append("name\n")
        patient.append("age\n")
        patient.append("sex\n")
        patient.append("date\n")
        patient.append("room_no\n")
        patient.append("floor_no\n")
        
        ans=input("TO KEEP REPEATING PRESS 'Y' :")
        if ans=="Y":
            continue
        else:
            exit()
      
        
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
            
            
file=open("bill.txt","a")
def bill():
    jk=True
    while jk==True:
        main_menu()
    #name     | room_service | doc_charge | treatment_charge | medicine_charge
        name=input("ENTER THE NAME                                :")
        room_service=int(input("ENTER THE ROOM SERVICE COST       :"))
        doc_charge=int(input("ENTER THE DOCTOR CHARGE             :"))
        treatment_charge=int(input("ENTER THE TREATMENT CHARGE    :"))
        medicine_charge=(input("ENTER THE MEDICINE CHARGE         :"))
        
        print("-"*40)
        
        file.append("\n\n")
        file.append("name\n")
        file.append("room_service\n")
        file.append("doc_charge\n")
        file.append("medicine_charge\n")
        file.append("l\n") #how to get more than two line to start new data entery in file?
       
        l=name+room_service+doc_charge+treatment_charge+medicine_charge
       
        
        print("YOUR TOTAL AMOUNT IS:",l)
        print("----------------VISIT AGAIN-------------------- ")
        ans=input("TO KEEP REPEATING PRESS 'Y' ")
        if ans=="Y":
            continue
        else:
            exit()
     
    
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def notice():
    
    print("-"*40)
    noticee=("""Patients have the responsibility to:
        
        

        Provide accurate information about their health, including past illnesses or health problems,
        hospitalizations, allergies and the current or past use of medication.
        Read and understand all medical forms including consent forms thoroughly prior signing.
        Follow the prescriptions and agreed treatment plan, and comply with the instructions given.
        Observe facility policies and procedures.
        Make the payment of the bills on time as directed by the hospital.
        Respect the visiting timings and not to bring children below 10 years as visitors.
        Show consideration for the rights for the other patients and the hospital by following the hospital
        rules concerning patient conduct.
        Not to ask to provide incorrect information or certificates.
        Not to litter the hospital.
        Use garbage bins.
        Keep toilets clean after use.
        Not to smoke or spit inside the hospital premises.
        Support the hospital in keeping the environment clean.
        Wait patiently for their turn.
        Maintain Silence.
        Responsibility for following the treatment plan recommended by those responsible for their care.
        Responsible for their action if they refuse treatment or do not follow the health care provider’s instruction.
        Responsible for participating in best of your ability in making decision about your medical treatment
        and to comply with the agreed upon care.
        Responsible for asking questions to your physician or other health care providers when you do not understand 
        any instruction or information.
        Responsible to inform your physician or other care provider 
        if you desire a transfer of care to another physician or care giver or facility.
        Never hurting or threatening another patient, family member or member of staff, or conduct of any
        activity that will disrupt the work of the hospital.
        Not bring any weapons into the hospital.
        Never bringing alcohol or unauthorized drugs into the hospital.
        Responsible for excepting financial responsibility for health care services and to settle the bills promptly.
        Responsible for respecting the autonomy of doctors, nurses & health care
        professionals and treat them with respect.
        Responsible for signing the informed consent as and when required during 
        the treatment plan and asks to have the information explained to them prior to signing if they do not understand.
        To refrain your guests from visiting the hospital in case they are suffering from any disease or infection.
        Responsible for being on time for appointments and inform the hospital staff if you cannot keep your appointment.
        The patient/relatives responsible for his/her actions and the outcomes of those actions
        if he/she refuses treatment or does not follow the agreed.
        The patient is responsible for following the rules and regulations affecting patient care and conduct.
        Understand that the hospital is not responsible for
        the personal property or for valuables kept on the person, unless they are received and stored for 
        the patient by hospital personnel.""")
    print(noticee)
    print("-"*40)
    
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
def about():
    print("-"*40)
    aboutt=("""Sharda Hospital, a state-of-the-art multi superspeciality hospital,
        offers medical care at par the global excellence. Equipped with all modern facilities and 
        sophisticated equipment, Sharda Hospital provides global comprehensive healthcare as preferred destination 
        of healthcare. It’s highly qualified and experienced medical professionals offer best in class expert care to the patients
        round-the-clock.

        Our endeavor is to provide modern medical care to our patients,
        encourage research activities, give extensive training to medical students and 
        continuously improve medical and healthcare facilities/practices, and extend.

        Sharda Hospital offers broad spectrum of medical services from tertiary care,
        superspecialities, general specialities, advanced diagnostic & radiology services to critical care.
        Pertaining to the growing demand and increasing popularity of Ayurveda, we have also established a ‘Panchakarma Centre’
        at Sharda Hospital to provide massage therapies of high and positive prognostic value to the diseases 
        that are considered to be medically unmanageable.

       At the onset where Sharda Group of Institutions 
       aspires to reach new benchmark of success the Group believes and continuously serves the humanity and the society.
       We are committed to upgrading the level and standard of medical facilities 
       to all sections of the society and emphasize the importance of helping the community with
       their need for medical emergency and treatment Sharda Hospital is a 900+ bedded hospital, It is a well-equipped,
       multispecialty hospital with modern facilities situated in pollution free environment and
       easily accessible from Delhi international airport and city of Delhi. it’s associated School of Medical Sciences and
       Research (Medical College) with 150 MBBS students intake provides rich opportunities for students to pursue
       collaborative and interdisciplinary education and independent study projects in the field of medical education.

       Hospital has 90+ beds in critical care in the fields of medicine,
       pulmonology, surgery, pediatric, neonatology, cardiology, cardiothoracic surgery and neurosciences.""")    
    print(aboutt)
    print("-"*40)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
    






    
    








    
    
    
    

    

     
    
    
    
    
























    
    