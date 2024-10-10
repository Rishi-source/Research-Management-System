from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Department(models.Model):
    name = models.CharField(max_length=500, default='Unknown Department')

    def __str__(self):
        return self.name
    
class Organization(models.Model):
    name = models.CharField(max_length=500, default='Unknown Organization')

    def __str__(self):
        return self.name

class FinancialYear(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    
class PrincipleInvestigator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    PSRN = models.CharField(max_length=500, default='Not Provided')
    Name_PI = models.CharField(max_length=500, default='Not Provided')
    Designation_PI = models.CharField(max_length=500, default='Not Provided')
    organization = models.ForeignKey(Organization, related_name='principle_investigators', on_delete=models.CASCADE, default=None)
    department = models.ForeignKey(Department, related_name='principle_investigators', on_delete=models.CASCADE, default=None)
    superannuation_date = models.PositiveIntegerField(
        validators=[
            MinValueValidator(datetime.date.today().year - 10),  
            MaxValueValidator(datetime.date.today().year)
        ],
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.Name_PI} ({self.Designation_PI})"

    
CHOICES = [
    ('yes', 'Yes'),
    ('no', 'No'),
]

PROJECT_TYPE = [
    ("Government", "Government"),
    ("Industry Sponsored Project", "Industry Sponsored Project"),
    ("Consultancy Project", "Consultancy Project"),
    ("International Project", "International Project"),
    ("Alumni Project", "Alumni Project")
]

FUNDING_AGENCY_TYPE = [
    ("Government Project", "Government Project"),
    ("Non-Governmental Organization in India", "Non-Governmental Organization in India"),
    ("International", "International"),
    ("Industry", "Industry"),
]

SUBMISSION_TYPE = [
    ("Online (Email submission)", "Online (Email submission)"),
    ("Online (Portal submission)", "Online (Portal submission)"),
    ("Offline (postal submission)", "Offline (postal submission)"),
]

STATUS_CHOICES = (
    ('ongoing', 'Ongoing'),
    ('completed', 'Completed'),
)

class EndorsementForm(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Project_Title = models.CharField(max_length=500, null=True, blank=True)
    PSRN = models.CharField(max_length=500,null=True, blank=True)
    Name_PI = models.CharField(max_length=500, null=True, blank=True)
    Designation_PI = models.CharField(max_length=500, null=True, blank=True)
    organization = models.ForeignKey(Organization, related_name='endorsement_forms', on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, related_name='endorsement_forms', on_delete=models.CASCADE, null=True, blank=True)
    superannuation_date = models.PositiveIntegerField( null=True, blank=True)
    Co_PI1 = models.ForeignKey(PrincipleInvestigator, related_name='co_pi1_forms', on_delete=models.CASCADE, null=True, blank=True)
    Co_PI2 = models.ForeignKey(PrincipleInvestigator, related_name='co_pi2_forms', on_delete=models.CASCADE, null=True, blank=True)
    Co_PI3 = models.ForeignKey(PrincipleInvestigator, related_name='co_pi3_forms', on_delete=models.CASCADE, null=True, blank=True)
    Co_PI4 = models.ForeignKey(PrincipleInvestigator, related_name='co_pi4_forms', on_delete=models.CASCADE, null=True, blank=True)
    Co_PI5 = models.ForeignKey(PrincipleInvestigator, related_name='co_pi5_forms', on_delete=models.CASCADE, null=True, blank=True)
    Co_PI6 = models.ForeignKey(PrincipleInvestigator, related_name='co_pi6_forms', on_delete=models.CASCADE, null=True, blank=True)
    project_type = models.CharField(
        max_length=100,
        choices=PROJECT_TYPE,
        null=True, blank=True
    )
    funding_agency = models.CharField(max_length=500, null=True, blank=True)
    funding_scheme = models.CharField(max_length=500, null=True, blank=True)
    funding_agency_type = models.CharField(
        max_length=100,
        choices=FUNDING_AGENCY_TYPE,
        null=True, blank=True
    )
    CAPEX = models.PositiveIntegerField(null=True, blank=True)
    OPEX = models.PositiveIntegerField(null=True, blank=True)
    total_budget_requested = models.PositiveIntegerField(null=True, blank=True)
    budget_split = models.TextField(null=True, blank=True)
    submission_type = models.CharField(
        max_length=100,
        choices=SUBMISSION_TYPE,
        null=True, blank=True
    )
    project_duration = models.PositiveIntegerField(null=True, blank=True)
    last_date_for_submission = models.DateField(null=True, blank=True)
    commencement_date_of_project = models.DateField(null=True, blank=True)
    abstract = models.TextField(max_length=200, help_text="Abstract of the project (up to 200 words)",null=True, blank=True)
    keywords = models.CharField(max_length=255, help_text="Keywords (5-6, comma separated)",null=True, blank=True)
    informed_hod = models.CharField(max_length=3, choices=CHOICES, null=True, blank=True, help_text="Have you informed your HoD about this proposal?")
    upload_hod_consent = models.CharField(max_length=3, choices=CHOICES, null=True, blank=True, help_text="Would you like to upload the reviews and consent from departmental HoD?")
    hod_consent_pdf = models.FileField(upload_to='hod_consent/', blank=True, null=True, help_text="Upload PDF file. Max 10 MB.")
    proposal_file = models.FileField(upload_to='project_proposals/', help_text="Upload 1 supported file: PDF. Max 10 MB.",null=True, blank=True)
    endorsement_required = models.CharField(max_length=3, choices=CHOICES, null=True, blank=True, help_text="Is an Endorsement form required?")
    endorsement_template = models.FileField(upload_to='endorsement_templates/', blank=True, null=True, help_text="Upload 1 supported file: doc/docx/pdf. Max 10 MB.")
    additional_comments = models.TextField(blank=True, null=True, help_text="Any additional comments")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    year = models.ForeignKey(FinancialYear, related_name='Year', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Endorsement Form: {self.id}"

    class Meta:
        verbose_name = "Endorsement Form"
        verbose_name_plural = "Endorsement Forms"

class Budget(models.Model):
    project = models.OneToOneField(EndorsementForm, on_delete=models.CASCADE, default=None)
    sanctiondate = models.DateField(blank = True , null = True)
    sanctionorder = models.CharField(max_length=255,blank = True , null = True,default=None)
    Equipment = models.PositiveIntegerField()
    Consumables = models.PositiveIntegerField()
    Fellowship = models.PositiveIntegerField()
    Contingency = models.PositiveIntegerField()
    Travel = models.PositiveIntegerField()
    Field_Testing = models.PositiveIntegerField()
    Miscellaneous = models.PositiveIntegerField()

    def __str__(self):
        return f"Budget : {self.project.id}"
    
class RecievedAmount(models.Model):
    project = models.OneToOneField(EndorsementForm, on_delete=models.CASCADE, null=True, blank=True)
    Equipment = models.PositiveIntegerField()
    Consumables = models.PositiveIntegerField()
    Fellowship = models.PositiveIntegerField()
    Contingency = models.PositiveIntegerField()
    Travel = models.PositiveIntegerField()
    Field_Testing = models.PositiveIntegerField()
    Miscellaneous = models.PositiveIntegerField()

    def __str__(self):
        return f"Recieved Amount : {self.project.id}"

    
class Installment(models.Model):
    project = models.ForeignKey(EndorsementForm, on_delete=models.CASCADE)
    installment_year = models.ForeignKey(FinancialYear, related_name='Financial_Year', on_delete=models.CASCADE, default=None)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"Installment Amount : {self.project.id} {self.installment_year.name} Rs.{self.amount} "
    
EXPENDITURE_TYPE = [
    ('Equipment' ,'Equipment'),
    ('Consumables' ,'Consumables'),
    ('Fellowship' ,'Fellowship'),
    ('Contingency' ,'Contingency'),
    ('Travel' ,'Travel'),
    ('Field Testing' ,'Field Testing'),
    ('Miscellaneous' ,'Miscellaneous'),
]

TYPE = [
    ('Recurring' ,'Recurring'),
    ('Non-Recurring' ,'Non-Recurring'),
]

class Expenditure(models.Model):
    project = models.ForeignKey(EndorsementForm, on_delete=models.CASCADE)
    year = models.ForeignKey(FinancialYear, on_delete=models.CASCADE, null=True, blank=True)
    expenditure_type = models.CharField(
        max_length=100,
        choices=EXPENDITURE_TYPE,
    )
    Expenditure_date = models.DateField(blank = True , null = True)
    amount = models.PositiveIntegerField()
    type = models.CharField(
        max_length=100,
        choices=TYPE,
        blank = True , null = True
    )

    def __str__(self):
        return f"Expenditure Amount : {self.project.id} - Rs.{self.amount} - {self.expenditure_type} "
    
class FinYearBudget(models.Model):
    project = models.OneToOneField(EndorsementForm, on_delete=models.CASCADE, null=True, blank=True)
    year = models.ForeignKey(FinancialYear, on_delete=models.CASCADE, null=True, blank=True)
    Equipment = models.PositiveIntegerField(null=True, blank=True)
    Consumables = models.PositiveIntegerField(null=True, blank=True)
    Fellowship = models.PositiveIntegerField(null=True, blank=True)
    Contingency = models.PositiveIntegerField(null=True, blank=True)
    Travel = models.PositiveIntegerField(null=True, blank=True)
    Field_Testing = models.PositiveIntegerField(null=True, blank=True)
    Miscellaneous = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Financial Year Budget : {self.project.id}"
