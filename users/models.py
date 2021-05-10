from django.db import models
from django.contrib.auth.models import AbstractUser
from aboutPatient.models import Dossier, Consultation, Radio, Analyse, Chambre,Prescription

# Create your models here.
# def get_profile_iage_filepath(self, filename):
#     return f'profile_image/{self.pk}/{"profile_image.png}'

class Personne(models.Model):
    email = models.EmailField(blank=False, max_length=254, verbose_name="email address",unique=True)
    nom = models.CharField(max_length=30 )
    prenom = models.CharField(max_length=30)
    motDePasse = models.CharField(max_length=20)
    adresse = models.CharField(max_length=254)
    telephone = models.CharField(max_length=20)
    #profile_image = models.ImageField(max_length=255, upload_to= , null = True, blank = True, default=)
    dateDeNaissance = models.DateField() 
    class Meta:
        abstract =True
    
    
        



class Patient (Personne):
    idDossier = models.OneToOneField(Dossier,null=True,on_delete=models.SET_NULL)
    
    
    

class Docteur (Personne):
    specialite = models.CharField(max_length=100)

class Analyste (Personne):
    pass

class Radiologue (Personne):
    pass

class Pharmacien (Personne):
    pass
#----------------------------------------------------------------------------------------------------------------

""" class Consultation (models.Model):
    comptRendu = models.TextField()
    idPrescription = models.ForeignKey(Docteur, on_delete=models.CASCADE, related_name='idPrescription')
    idDossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='idDossierConsultation')
    idDocteur = models.ForeignKey(Docteur, on_delete=models.CASCADE, related_name='idDocteurConsultation')
    idChambre = models.IntegerField()
    idRadio = models.IntegerField()
    idAnalyse = models.IntegerField()

class Presciption (models.Model):
    medicament = models.TextField()
    dateDeCreation = models.DateField(auto_now_add=True)
    idDocteur = models.ForeignKey(Docteur, on_delete=models.CASCADE, related_name='idDocteurPresciption')
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='idPatientPresciption')

class Chambre (models.Model):
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='idPatientChambre')
    idDocteur = models.ForeignKey(Docteur, on_delete=models.CASCADE, related_name='idDocteurChambre')
    dateDeSejour = models.DateField()
    dateDeFinSejour =models.DateField()

class Radio (models.Model):
    description = models.TextField()
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='idPatientRadio')
    idDocteur = models.ForeignKey(Docteur, on_delete=models.CASCADE, related_name='idDocteurRadio')
    dateOperation = models.DateField()
    resultat = models.TextField()
    validation = models.BooleanField(default=False)

class Analyse (models.Model):
    description = models.TextField()
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='idPatientAnalyse')
    idDocteur = models.ForeignKey(Docteur, on_delete=models.CASCADE, related_name='idDocteurAnalyse')
    dateOperation = models.DateField()
    resultat = models.TextField()
    validation = models.BooleanField(default=False)

 """