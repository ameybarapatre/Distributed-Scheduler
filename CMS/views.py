from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect
from .models import *
from django.utils import timezone
from django.utils import formats
import datetime

def index(request):
	return render(request,'login.html')

def login(request):
	if request.method == 'POST':
		if User.objects.filter(username=request.POST.get('login_username'),password=request.POST.get('login_password')).count()!=0:
			request.session['username']=request.POST.get('login_username')
			k=User.objects.filter(username=request.POST.get('login_username'),password=request.POST.get('login_password'))
			if k[0].user_type==1:
				request.session['user_type']=1
				return redirect(show)
			else:
				request.session['user_type']=0	
				return redirect(find)
		else :
			return render(request,'login.html')
	else :
		if 'username' in  request.session :
			if request.session['user_type']==0:
				return redirect(find)
			else:
				return redirect(show)
		else :
			return render(request,'login.html')


def find(request):
	if 'username'  in  request.session :
		if request.session['user_type']==0:
			q = User.objects.filter(username=request.session['username'])
			day=['Monday','Tuesday','Wednesday','Thursday','Friday']
			x=[]
			if q[0].user_dep==1:
				x = Timetable_dep1_prof_25.objects.filter(p_id=q[0].user_id)
				print(x,day)
			else :	
				x= Timetable_dep2_prof_25.objects.filter(p_id=q[0].user_id)
				print(x,day)
			context={'Lects': x ,'Days' : day ,'id' :q[0].user_id }
			return render(request,'find.html',context)
		else:
			return redirect(show)
	else :
		return redirect(index)	


def lectures(request):
	if 'username'  in  request.session :
		if request.session['user_type']==0:
			return redirect(find)
		else:
			return redirect(find)

	else :
		return redirect(index)	


def logout(request):
	del request.session['username']
	return redirect(login)


def remove(request):
	if 'username'  in  request.session :
		if request.method == 'POST':
			q = User.objects.filter(username=request.session['username'])
			if q[0].user_dep == 1:
					w = Timetable_dep1_prof_25.objects.filter(p_id =q[0].user_id,Subject_name=request.POST.get('Subject'),Time_slot_no=request.POST.get('Time'),Day=request.POST.get('Day')).delete()
			else :
					w = Timetable_dep2_prof_25.objects.filter(p_id =q[0].user_id,Subject_name=request.POST.get('Subject'),Time_slot_no=request.POST.get('Time'),Day=request.POST.get('Day')).delete()
					
			return HttpResponseRedirect('/CMS/find/')
		else :
			return HttpResponseRedirect('/CMS/find/')
	else :
		return HttpResponseRedirect('/CMS/home/')

def submit(request):
	if 'username'  in  request.session :
		if request.method == 'POST':
			if request.POST.get('Subject')!=None or request.POST.get('Time')!=None or request.POST.get('Day')!=None :
				q = User.objects.filter(username=request.session['username'])
				if q[0].user_dep == 1:
					w = Timetable_dep1_prof_25(p_id =q[0].user_id,Subject_name=request.POST.get('Subject'),Time_slot_no=request.POST.get('Time'),Day=request.POST.get('Day'))
					w.save()
				else :
					w = Timetable_dep2_prof_25(p_id =q[0].user_id,Subject_name=request.POST.get('Subject'),Time_slot_no=request.POST.get('Time'),Day=request.POST.get('Day'))
					w.save()
				return HttpResponseRedirect('/CMS/find/')
			else:
				return HttpResponseRedirect('/CMS/find/')
		else:
			return HttpResponseRedirect('/CMS/find/')
	else :
		return HttpResponseRedirect('/CMS/home/')	

def show(request):
	if 'username'  in  request.session :
		if  request.method == 'GET' :
			q = User.objects.filter(username=request.session['username'])
			x=[]
			z = User.objects.filter(user_type=0,user_dep=q[0].user_dep)
			prof=[]
			for each in z :
				prof.append(each.username)	
			print(prof)	
			context={'Lects': x ,'id' :q[0].user_id ,'prof' :prof}
			return render(request,'lectures.html',context)
		else:	
			if request.session['user_type']==1:
				q = User.objects.filter(username=request.session['username'])
				z = User.objects.filter(user_type=0,user_dep=q[0].user_dep)
				prof=[]
				for each in z :
					prof.append(each.username)	
				print(prof)	
				 
				x=[]
				if q[0].user_dep==1:
					if request.POST.get('Professor')!=None:
						w = User.objects.filter(username=request.POST.get('Professor'))
						your_values = { 'Subject_name' : request.POST.get('Subject') , 'Day' : request.POST.get('Day'), 'p_id' :w[0].user_id, 'Time_slot_no' :request.POST.get('Time')}
						arguments = {}
						for k, v in your_values.items():
							if v:
								arguments[k] = v

						x = Timetable_dep1_prof_25.objects.filter(**arguments)
					elif  request.POST.get('Professor')==None:
						
						your_values = { 'Subject_name' : request.POST.get('Subject') , 'Day' : request.POST.get('Day'), 'Time_slot_no' :request.POST.get('Time')}
						arguments = {}
						for k, v in your_values.items():
							if v:
								arguments[k] = v

						x = Timetable_dep1_prof_25.objects.filter(**arguments)
					
					else:
						HttpResponseRedirect('/CMS/show/')
					
					context={'Lects' : x,'id' : q[0].user_id ,'prof' : prof}
					return render(request,'lectures.html',context)
				elif q[0].user_dep==2:
					if request.POST.get('Professor')!=None:
						w = User.objects.filter(username=request.POST.get('Professor'))
						your_values = { 'Subject_name' : request.POST.get('Subject') , 'Day' : request.POST.get('Day'), 'p_id' :w[0].user_id, 'Time_slot_no' :request.POST.get('Time')}
						arguments = {}
						for k, v in your_values.items():
							if v:
								arguments[k] = v

						x = Timetable_dep2_prof_25.objects.filter(**arguments)
					elif  request.POST.get('Professor')==None:
						
						your_values = { 'Subject_name' : request.POST.get('Subject') , 'Day' : request.POST.get('Day'), 'Time_slot_no' :request.POST.get('Time')}
						arguments = {}
						for k, v in your_values.items():
							if v:
								arguments[k] = v
						x = Timetable_dep2_prof_25.objects.filter(**arguments)
						
					else:
						HttpResponseRedirect('/CMS/show/')
					context={'Lects' : x,'id' : q[0].user_id ,'prof' : prof}
					return render(request,'lectures.html',context)
				
				else :	
					return redirect(index)	
				
			else:
				return redirect(index)
	else :
		return redirect(index)	

def add(request):
	if 'username'  in  request.session :
		if request.method == 'POST':
			q = User.objects.filter(username=request.session['username'])
			k = User.objects.filter(user_id=request.POST.get('Professor'))
			if Timetable_9.objects.filter(s_id=q[0].user_id,Time_slot_no=request.POST.get('Time'),Day=request.POST.get('Day')).count()==0:
			
				if q[0].user_dep == 1:
						w = Timetable_9(p_id=k[0].user_id,s_id =q[0].user_id,Subject_name=request.POST.get('Subject'),Time_slot_no=request.POST.get('Time'),Day=request.POST.get('Day'))
						w.save()
				else :
						w = Timetable_9(p_id=k[0].user_id,s_id =q[0].user_id,Subject_name=request.POST.get('Subject'),Time_slot_no=request.POST.get('Time'),Day=request.POST.get('Day'))
						w.save()
				return HttpResponseRedirect('/CMS/show/')
			else:
				return HttpResponseRedirect('/CMS/show/')
		else :
			return HttpResponseRedirect('/CMS/show/')
	else :
		return HttpResponseRedirect('/CMS/home/')

# Create your views here.

def display(request):
	if 'username'  in  request.session :
		if request.session['user_type']==1:
			q = User.objects.filter(username=request.session['username'])
			day=['Monday','Tuesday','Wednesday','Thursday','Friday']
			x=[]
			if q[0].user_dep==1:
				x = Timetable_dep1_25.objects.filter(s_id=q[0].user_id)
				
			else :	
				x= Timetable_dep2_25.objects.filter(s_id=q[0].user_id)
				
			context={'Lects': x ,'Days' : day ,'id' :q[0].user_id }
			return render(request,'display.html',context)
		else:
			return redirect(index)
	else :
		return redirect(index)	

def removeitem(request):
	if 'username'  in  request.session :
		if request.method == 'POST':
			q = User.objects.filter(username=request.session['username'])
			if q[0].user_dep == 1:
					w = Timetable_dep1_25.objects.filter(p_id=request.POST.get('Professor'),s_id =q[0].user_id,Subject_name=request.POST.get('Subject'),Time_slot_no=request.POST.get('Time'),Day=request.POST.get('Day')).delete()
			else :
					w = Timetable_dep2_25.objects.filter(p_id=request.POST.get('Professor'),s_id =q[0].user_id,Subject_name=request.POST.get('Subject'),Time_slot_no=request.POST.get('Time'),Day=request.POST.get('Day')).delete()
					
			return HttpResponseRedirect('/CMS/display/')
		else :
			return HttpResponseRedirect('/CMS/display/')
	else :
		return HttpResponseRedirect('/CMS/home/')