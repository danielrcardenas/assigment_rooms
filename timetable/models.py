from django.db import models


# Create your models here.

class SubjectArea(models.Model):
    sa_id = models.AutoField(primary_key=True)
    sa_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.s_name


class Professor(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=200, unique=True)
    p_type = models.IntegerField(default=0)
    p_email = models.EmailField(max_length=254)
    p_hours_per_week = models.IntegerField(default=0)
    #Horas Contratadas
    p_signed_hours = models.IntegerField(default=0)
    p_subject_area = models.ForeignKey(SubjectArea, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.p_name


class Subject(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=200, unique=True)
    s_subject_area = models.ForeignKey(SubjectArea, on_delete=models.SET_NULL, null=True, blank=True)


class SubjectStudyPlan(models.Model):
    ssp_id = models.AutoField(primary_key=True)
    ssp_subjet = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    ssp_study_plan = models.ForeignKey(SubjectArea, on_delete=models.CASCADE, null=True, blank=True)
    ssp_semester = models.IntegerField()


class StudyPlan(models.Model):
    f_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=200, unique=True)


