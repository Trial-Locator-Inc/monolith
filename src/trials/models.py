from django.db import models

class TrialStatus(models.TextChoices):
  ACTIVE_NOT_RECRUITING = "Active, not recruiting"
  COMPLETED = "Completed"
  ENROLLING_BY_INVITATION = "Enrolling by invitation"
  NOT_YET_RECRUITING = "Not yet recruiting"
  RECRUITING = "Recruiting"
  SUSPENDED = "Suspended"
  TERMINATED = "Terminated"
  WITHDRAWN = "Withdrawn"
  AVAILABLE = "Available"
  NO_LONGER_AVAILABLE = "No longer available"
  TEMPORARILY_NOT_AVAILABLE = "Temporarily not available"
  APPROVED_FOR_MARKETING = "Approved for marketing"
  WITHHELD = "Withheld"
  UNKNOWN = "Unknown status"

class ClinicalTrial(models.Model):
  class AgencyClass(models.TextChoices):
    NIH = "NIH"
    FED = "FED"
    OTHER_GOV = "Other Gov"
    INDIV = "Indiv"
    INDUSTRY = "Industry"
    NETWORK = "Network"
    AMBIG = "Ambiguous"
    OTHER = "Other"
    UNKNOWN = "Unknown"

  class Sex(models.TextChoices):
    FEMALE = "F"
    MALE = "M"
    ALL = "All"

  class ResponsibleParty(models.TextChoices):
    SPONSOR = "Sponsor"
    PRINCIPAL_INVESTIGATOR = "Principal Investigator"
    SPONSOR_INVESTIGATOR = "Sponsor-Investigator"

  class StudyType(models.TextChoices):
    EXPANDED_ACCESS = "Expanded Access"
    INTERVENTIONAL = "Interventional"
    OBSERVATIONAL = "Observational"

  class Phase(models.TextChoices):
    NOT_APPLICABLE = "NA"
    EARLY_PHASE_1 = "Early phase 1"
    PHASE_1 = "1"
    PHASE_2 = "2"
    PHASE_3 = "3"
    PHASE_4 = "4"

  # This first section is just data I can get from clinicaltrials.gov
  # protocolSection.identificationModule.nctId
  nct_id = models.CharField(max_length=11)

  # protocolSection.identificationModule.briefTitle
  brief_title = models.CharField()

  # protocolSection.identificationModule.officialTitle
  official_title = models.CharField()

  # protocolSection.identificationModule.organization.fullName
  organization_name = models.CharField()

  # protocolSection.identificationModule.organization.class
  organization_type = models.CharField(choices=AgencyClass)

  # protocolSection.statusModule.statusVerifiedDate
  record_verification_date = models.DateField()

  # protocolSection.statusModule.overallStatus
  overall_status = models.CharField(choices=TrialStatus)

  # protocolSection.statusModule.startDateStruct.date
  start_date = models.DateField()

  # protocolSection.statusModule.studyFirstPostDateStruct.date
  date_posted = models.DateField()

  # protocolSection.sponsorCollaboratorsModule.responsibleParty.type
  responsible_party = models.CharField(choices=ResponsibleParty)

  # protocolSection.eligibilityModule.eligibilityCriteria
  eligibility_criteria = models.TextField()

  # protocolSection.eligibilityModule.sex
  eligible_sex = models.CharField(choices=Sex)

  # protocolSection.eligibilityModule.minimumAge
  min_age = models.CharField()

  # protocolSection.eligibilityModule.maximumAge
  max_age = models.CharField()

  # protocolSection.eligibilityModule.studyPopulation
  study_population = models.TextField()


  # TODO: add description module
  # TODO: add conditions module
  # TODO: add design module
  # TODO: add arms intervention module

  def __str__(self):
    return f"{self.nct_id}: {self.brief_title}"

  class PrimaryPurpose(models.TextChoices):
    TREATMENT = "Treatment"
    PREVENTION = "Prevention"
    DIAGNOSTIC = "Diagnostic"
    ECT = "Educational/Counseling/Training"
    SUPPORTIVE_CARE = "Supportive care"
    SCREENING = "Screening"
    HEALTH_SERVICES_RESEARCH = "Health services research"
    BASIC_SCIENCE = "Basic science"
    DEVICE_FEASIBILITY = "Device feasibility"
    OTHER = "Other"

  class ArmGroupType(models.TextChoices):
    EXPERIMENTAL = "Experimental"
    ACTIVE_COMPARATOR = "Active comparator"
    PLACEBO_COMPARATOR = "Placebo comparator"
    SHAM_COMPARATOR = "Sham comparator"
    NO_INTERVENTION = "No intervention"
    OTHER = "Other"

  class InterventionType(models.TextChoices):
    BEHAVIORAL = "Behavioral"
    BIOLOGICAL = "Biological"
    COMBINATION_PRODUCT = "Combination Product"
    DEVICE = "Device"
    DIAGNOSTIC_TEST = "Diagnostic Test"
    DIETARY_SUPPLEMENT = "Dietary Supplement"
    DRUG = "Drug"
    GENETIC = "Genetic"
    PROCEDURE = "Procedure"
    RADIATION = "Radiation"
    OTHER = "Other"


# TODO: finish
class Location(models.Model):
  trials = models.ManyToManyField(ClinicalTrial)
  status = models.CharField(choices=TrialStatus)

# TODO: finish
class Contact(models.Model):
  trials = models.ManyToManyField(ClinicalTrial)

# TODO finish
class Collaborator(models.Model):
  trials = models.ManyToManyField(ClinicalTrial)

# TODO finish
# each trial has one or more targeted outcomes
class Outcome(models.Model):
  trials = models.ManyToManyField(ClinicalTrial)
