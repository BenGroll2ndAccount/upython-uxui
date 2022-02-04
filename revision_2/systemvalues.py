global L_weekday
L_weekday = []

global weekday
weekday = 0

class nMAP():
    def edit_weekday(value):
        global weekday
        global L_weekday
        weekday = value
        for listener in L_weekday:
            listener.notify("weekday", weekday)

    def add_weekday_listener(obj):
        global L_weekday
        L_weekday.append(obj)
    
    def remove_weekday_listener(obj):
        global L_weekday
        L_weekday.remove(obj)

def global_edit(name, value):
        func = getattr(nMAP, "edit_" + name)
        func(value)

def global_addL(name, obj):
    func = getattr(nMAP, "add_" + name + "_listener")
    func(obj)

def global_remL(name, obj):
    func = getattr(nMAP, "remove_" + name + "_listener")
    func(obj)


