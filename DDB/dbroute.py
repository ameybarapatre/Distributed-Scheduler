class router25(object):
    def db_for_read(self, model, **hints):
       
        l25 = ['Timetable_dep1_25','Timetable_dep1_prof_25','Timetable_dep2_prof_25']
        if model._meta.object_name in l25 :
            return 'user25a'
        return None

    def db_for_write(self, model, **hints):
        
        l25 = ['Timetable_dep1_25','Timetable_dep1_prof_25','Timetable_dep2_prof_25']
        if model._meta.object_name in l25 :
            return 'user25a'
        return None

    def allow_relation(self, obj1, obj2, **hints):
    
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
    
        l25 = ['timetable_dep1_25','timetable_dep1_prof_25','timetable_dep2_prof_25']
        if model_name in l25 :
            return db=='user25a'
        return None

class router24(object):
    def db_for_read(self, model, **hints):
       
        l24 = ['Timetable_dep2_24','Timetable_dep1_stud_24','Timetable_dep2_stud_24']
        if model._meta.object_name in l24 :
            return 'user24a'
        return None

    def db_for_write(self, model, **hints):
        
        l24 = ['Timetable_dep2_24','Timetable_dep1_stud_24','Timetable_dep2_stud_24']
        if model._meta.object_name in l24 :
            return 'user24a'
        return None


    def allow_relation(self, obj1, obj2, **hints):
    
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
    
        l24 = ['timetable_dep2_24','timetable_dep1_stud_24','timetable_dep2_stud_24']
        if model_name in l24 :
            return db=='user24a'
        return None

class router9(object):
    def db_for_read(self, model, **hints):
       
        l24 = ['Timetable_9','User']
        if model._meta.object_name in l24 :
            return 'user9'
        return None

    def db_for_write(self, model, **hints):
        
        l24 = ['Timetable_9','User']
        if model._meta.object_name in l24 :
            return 'user9'
        return None


    def allow_relation(self, obj1, obj2, **hints):
    
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        l24 = ['timetable_9','user']
        if model_name in l24 :
            return db=='user9'
        return None


class routerdef(object):
    def db_for_read(self, model, **hints):
       
        return None
    def db_for_write(self, model, **hints):
        
        return None
        
    def allow_relation(self, obj1, obj2, **hints):
    
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db=='default'
        
