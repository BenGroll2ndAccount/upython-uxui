from uexceptions import uPROPERTYEXCEPTION



def check(props, wanted, defaults):
    checkedprops = {}
    properties = props.keys()
    for property in wanted:
        if property in properties:
            checkedprops[property] = props[property]
        else:
            checkedprops[property] = defaults[property]
    return checkedprops

class __PROPERTIES__():
    uHEAD = {
    }
    
    uPBOX = {
        "modX" : False,
        "modY": False,
        "modXvalue" : 100,
        "modYvalue" : 100,
        "alignX" : "align.center",
        "alignY" : "align.center"    
    }
    uPBOX_req = []
    #################################
    uCARD = {
        "rounded" : False,
        "rounding" : 0,
        "filled" : False,
        "fill_border" : False,
        "highlight" : False
    }
    uCARD_req = []


        
    
def propcheck(props, classname):
    if props == None:
        return {}
    defaults = getattr(__PROPERTIES__, classname)
    req = getattr(__PROPERTIES__, classname +"_req")
    checked_props = {}
    for default in defaults.keys():
        if default in props.keys():
            checked_props[default] = props[default]
        else:
            if default in req:
                raise uPROPERTYEXCEPTION("Required Property " + default + " not implemented.", widget = classname) 
            checked_props[default] = defaults[default]
    return checked_props


