from django.db import models


class User(models.Model):
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
	user_dep=models.IntegerField(default=1)
	user_type=models.IntegerField(default=0)
	user_id=models.IntegerField(primary_key=True)
	class Meta:
		db_table = "CMS_USER"

class Timetable_9(models.Model):
	Days=(('Friday','Friday'),('Wednesday','Wednesday'),('Tuesday','Tuesday'),('Monday','Monday'),('Thurday','Thurday'))
	s_id = models.IntegerField(primary_key=True)
	p_id = models.IntegerField(default=0)
	Subject_name = models.CharField(max_length=30)
	Day  = models.CharField(max_length=30,choices=Days)
	Time_slot_no  = models.CharField(max_length=30)
	Dep_id = models.IntegerField(default=1)
	class Meta:
		db_table = "CMS_TIMETABLE_9"

# Create your models here.

class  Timetable_dep1_25(models.Model):
	Days=(('Friday','Friday'),('Wednesday','Wednesday'),('Tuesday','Tuesday'),('Monday','Monday'),('Thurday','Thurday'))
	
	p_id = models.IntegerField(default=0)
	s_id = models.IntegerField(default=0)
	Subject_name = models.CharField(max_length=30)
	Day  = models.CharField(max_length=30 ,choices = Days)
	Time_slot_no  = models.CharField(max_length=30)
	class Meta:
		db_table = "CMS_TIMETABLE_DEP1_25"

class Timetable_dep1_prof_25(models.Model):
	Days=(('Friday','Friday'),('Wednesday','Wednesday'),('Tuesday','Tuesday'),('Monday','Monday'),('Thurday','Thurday'))
	
	p_id = models.IntegerField(default=0)
	Subject_name = models.CharField(max_length=30)
	Day  = models.CharField(max_length=30,choices=Days)
	Time_slot_no  = models.CharField(max_length=30)
	class Meta:
		db_table = "CMS_TIMETABLE_DEP1_PROF_25"



class Timetable_dep2_prof_25(models.Model):
	Days=(('Friday','Friday'),('Wednesday','Wednesday'),('Tuesday','Tuesday'),('Monday','Monday'),('Thurday','Thurday'))
	
	p_id = models.IntegerField(default=0)
	Subject_name = models.CharField(max_length=30)
	Day  = models.CharField(max_length=30,choices=Days)
	Time_slot_no  = models.CharField(max_length=30)
	class Meta:
		db_table = "CMS_TIMETABLE_DEP2_PROF_25"


class Timetable_dep2_24(models.Model):
	Days=(('Friday','Friday'),('Wednesday','Wednesday'),('Tuesday','Tuesday'),('Monday','Monday'),('Thurday','Thurday'))
	
	p_id = models.IntegerField(default=0)
	s_id = models.IntegerField(default=0)
	Subject_name = models.CharField(max_length=30)
	Day  = models.CharField(max_length=30,choices=Days)
	Time_slot_no  = models.CharField(max_length=30)
	class Meta:
		db_table = "CMS_TIMETABLE_DEP2_24"


class  Timetable_dep1_stud_24(models.Model):
	Days=(('Friday','Friday'),('Wednesday','Wednesday'),('Tuesday','Tuesday'),('Monday','Monday'),('Thurday','Thurday'))
	
	s_id = models.IntegerField(default=0)
	Subject_name = models.CharField(max_length=30)
	Day  = models.CharField(max_length=30,choices=Days)
	Time_slot_no  = models.CharField(max_length=30)
	class Meta:
		db_table = "CMS_TIMETABLE_DEP1_STUD_24"

class Timetable_dep2_stud_24(models.Model):
	Days=(('Friday','Friday'),('Wednesday','Wednesday'),('Tuesday','Tuesday'),('Monday','Monday'),('Thurday','Thurday'))
	
	s_id = models.IntegerField(default=0)
	Subject_name = models.CharField(max_length=30)
	Day  = models.CharField(max_length=30,choices=Days)
	Time_slot_no  = models.CharField(max_length=30)
	class Meta:
		db_table = "CMS_TIMETABLE_DEP2_STUD_24"





# Create your models here.
