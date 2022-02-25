
global L_weekday
L_weekday = []

global weekday
weekday = 0

global darkmode_enabled
darkmode_enabled = True

global L_darkmode_enabled
L_darkmode_enabled = [] 

global L_testvalue
L_testvalue = []

global testvalue
testvalue = False

global L_node_requests_redraw
L_node_requests_redraw = []

global node_requests_redraw
node_requests_redraw = False

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

    def edit_darkmode_enabled(value):
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

    def add_testvalue_listener(obj):
        global L_testvalue
        L_testvalue.append(obj)

    def remove_testvalue_listener(obj):
        global L_testvalue
        L_testvalue.remove(obj)

    def edit_testvalue():
        global testvalue
        global L_testvalue
        testvalue = not testvalue
        for listener in L_testvalue:
            listener.notify("testvalue", testvalue) 

    def add_node_requests_redraw_listener(obj):
        global L_node_requests_redraw
        L_node_requests_redraw.append(obj)

    def remove_node_requests_redraw_listener(obj):
        global L_node_requests_redraw
        L_node_requests_redraw.remove(obj)

    def edit_node_requests_redraw(value):
        global L_node_requests_redraw
        global node_requests_redraw
        node_requests_redraw = value
        for listener in L_node_requests_redraw:
            listener.notify("node_requests_redraw", node_requests_redraw)
        

def global_edit(name, value):
        func = getattr(nMAP, "edit_" + name)
        func(value)

def global_addL(name, obj):
    func = getattr(nMAP, "add_" + name + "_listener")
    func(obj)

def global_remL(name, obj):
    func = getattr(nMAP, "remove_" + name + "_listener")
    func(obj)


