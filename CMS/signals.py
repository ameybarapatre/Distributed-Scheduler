from django.db.models.signals import pre_save,post_save,post_delete,pre_delete
from django.dispatch import receiver
from CMS.models import *

@receiver(post_save, sender=Timetable_9)
def model_post_change(sender,instance,**kwargs):
	if instance.Dep_id==1:
		q = Timetable_dep1_25(p_id =instance.p_id,s_id = instance.s_id ,Subject_name=instance.Subject_name,Time_slot_no=instance.Time_slot_no,Day=instance.Day)
		q.save()
		w = Timetable_dep1_stud_24(s_id = instance.s_id ,Subject_name=instance.Subject_name,Time_slot_no=instance.Time_slot_no,Day=instance.Day)
		w.save()
	if instance.Dep_id==2:
		q = Timetable_dep2_24(p_id =instance.p_id,s_id = instance.s_id ,Subject_name=instance.Subject_name,Time_slot_no=instance.Time_slot_no,Day=instance.Day)
		q.save()
		w = Timetable_dep2_stud_24(s_id = instance.s_id ,Subject_name=instance.Subject_name,Time_slot_no=instance.Time_slot_no,Day=instance.Day)
		w.save()
@receiver(post_delete, sender=Timetable_9)
def model_post_ch(sender,instance,**kwargs):
	if instance.Dep_id==1:
		q = Timetable_dep1_25.objects.filter(p_id =instance.p_id,s_id = instance.s_id ,Subject_name=instance.Subject_name,Time_slot_no=instance.Time_slot_no,Day=instance.Day)
		q.delete()
		w = Timetable_dep1_stud_24.objects.filter(s_id = instance.s_id ,Subject_name=instance.Subject_name,Time_slot_no=instance.Time_slot_no,Day=instance.Day)
		w.delete()
	if instance.Dep_id==2:
		q = Timetable_dep2_24.objects.filter(p_id =instance.p_id,s_id = instance.s_id ,Subject_name=instance.Subject_name,Time_slot_no=instance.Time_slot_no,Day=instance.Day)
		q.delete()
		w = Timetable_dep2_stud_24.objects.filter(s_id = instance.s_id ,Subject_name=instance.Subject_name,Time_slot_no=instance.Time_slot_no,Day=instance.Day)
		w.delete()
@receiver(post_delete, sender=Timetable_dep1_25)
@receiver(post_delete, sender=Timetable_dep2_24)
def model_post_delete(sender,instance,**kwargs):
	if sender==Timetable_dep1_25:
		q = Timetable_9.objects.filter(Dep_id=1,p_id =instance.p_id,s_id = instance.s_id ,Subject_name=instance.Subject_name,Time_slot_no=instance.Time_slot_no,Day=instance.Day)
		q.delete()
	if sender==Timetable_dep2_24:
		q = Timetable_9.objects.filter(Dep_id=2,p_id =instance.p_id,s_id = instance.s_id ,Subject_name=instance.Subject_name,Time_slot_no=instance.Time_slot_no,Day=instance.Day)
		q.delete()
@receiver(pre_delete, sender=Timetable_dep1_prof_25)
@receiver(pre_delete, sender=Timetable_dep2_prof_25)
def model_pos(sender,instance,**kwargs):
	if sender==Timetable_dep1_prof_25:
		q = Timetable_9.objects.filter(Dep_id=1,p_id =instance.p_id,Subject_name=instance.Subject_name,Time_slot_no=instance.Time_slot_no,Day=instance.Day)
		q.delete()
	if sender==Timetable_dep2_prof_25:
		q = Timetable_9.objects.filter(Dep_id=2,p_id =instance.p_id,Subject_name=instance.Subject_name,Time_slot_no=instance.Time_slot_no,Day=instance.Day)
		q.delete()


