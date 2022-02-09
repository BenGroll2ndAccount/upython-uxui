global L_weekday
L_weekday = []

global weekday
weekday = 0

global darkmode_enabled
darkmode_enabled = True

global L_darkmode_enabled
L_darkmode_enabled = []


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

    def toggle_darkmode():
        global darkmode_enabled
        global L_darkmode_enabled
        darkmode_enabled = not darkmode_enabled
        for listener in L_darkmode_enabled:
            listener.notify("darkmode_enabled", darkmode_enabled)
    
    def add_darkmode_enabled_listener(obj):
        global L_darkmode_enabled
        L_darkmode_enabled.append(obj)
    
    def remove_darkmode_enabled_listener(obj):
        global L_darkmode_enabled
        L_darkmode_enabled.remove(obj)

def global_edit(name, value):
        func = getattr(nMAP, "edit_" + name)
        func(value)

def global_addL(name, obj):
    func = getattr(nMAP, "add_" + name + "_listener")
    func(obj)

def global_remL(name, obj):
    func = getattr(nMAP, "remove_" + name + "_listener")
    func(obj)


