from django.db import models

# Create your models here.

class Dossier (models.Model):
   pass 

class Prescription (models.Model):
    idDocteur = models.ForeignKey("users.Docteur", on_delete=models.CASCADE, related_name='idDocteurPrescription')
    idPatient = models.ForeignKey("users.Patient", on_delete=models.CASCADE, related_name='idPatientPrescription')
    medicament = models.TextField()
    dateDeCreation = models.DateField(auto_now_add=True)

class Chambre (models.Model):
    idPatient = models.ForeignKey("users.Patient", on_delete=models.CASCADE, related_name='idPatientChambre')
    idDocteur = models.ForeignKey("users.Docteur", on_delete=models.CASCADE, related_name='idDocteurChambre')
    dateDeSejour = models.DateField()
    dateDeFinSejour =models.DateField()

class Consultation (models.Model):
    idPrescription = models.OneToOneField(Prescription, on_delete=models.SET_NULL, related_name='idPrescription',null=True)
    idDossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='idDossierConsultation')
    idDocteur = models.ForeignKey("users.Docteur", on_delete=models.SET_NULL, related_name='idDocteurConsultation',null=True)
    idChambre = models.OneToOneField(Chambre, on_delete=models.SET_NULL,null=True)
    comptRendu = models.TextField()


class Radio (models.Model):
    
    idPatient = models.ForeignKey("users.Patient", on_delete=models.CASCADE, related_name='idPatientRadio')
    idDocteur = models.ForeignKey("users.Docteur", on_delete=models.CASCADE, related_name='idDocteurRadio',null=True)
    idConsultation = models.ForeignKey("Consultation",on_delete=models.SET_NULL, null=True)
    idRadiologue = models.ForeignKey("users.Radiologue", on_delete= models.SET_NULL, null=True)
    dateOperation = models.DateField()
    description = models.TextField()
    resultat = models.TextField()
    validation = models.BooleanField(default=False)

class Analyse (models.Model):
    idPatient = models.ForeignKey("users.Patient", on_delete=models.CASCADE, related_name='idPatientAnalyse')
    idDocteur = models.ForeignKey("users.Docteur", on_delete=models.CASCADE, related_name='idDocteurAnalyse')
    idConsultation = models.ForeignKey(Consultation,on_delete=models.SET_NULL, null=True)
    idAnalyste = models.ForeignKey("users.Analyste", on_delete= models.SET_NULL, null=True)
    dateOperation = models.DateField()
    description = models.TextField()
    resultat = models.TextField()
    validation = models.BooleanField(default=False)