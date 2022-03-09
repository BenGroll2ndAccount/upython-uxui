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
    ################################# uHEAD 
    uHEAD = {
        "width" : 128,
        "height" : 214
    }

    uHEAD_req = ["width", "height"]
    ################################# uPBOX
    
    uPBOX = {
        "modXvalue" : 100,
        "modYvalue" : 100,
        "alignX" : "align.center",
        "alignY" : "align.center"    
    }
    uPBOX_req = []
    ################################# uCARD
    uCARD = {
        "thickness" : 1,
        "rounded" : False,
        "rounding" : 0,
        "filled" : False,
        "fill_border" : False,
        "highlight" : False
    }
    uCARD_req = []
    ################################ uROW
    uROW = {
        "seperator" : 0,
        "spacing" : "spacing.equal",
        "container" : None,
        "include_edges": False
    }

    uROW_req = []
    ################################ uCOLUMN
    uCOLUMN = {
        "seperator" : 0,
        "spacing" : "spacing.equal",
        "container" : None,
        "include_edges": False
    }

    uCOLUMN_req = []



        
    
def propcheck(props, classname):
    defaults = getattr(__PROPERTIES__, classname)
    req = getattr(__PROPERTIES__, classname +"_req")
    checked_props = {}
    for default in defaults.keys():
        if props == None:
            if default in req:
                raise uPROPERTYEXCEPTION("Required Property " + default + " not implemented.", widget = classname) 
            else:
                checked_props[default] = defaults[default]
        elif default in props.keys():
            checked_props[default] = props[default]
        else:
            if default in req:
                raise uPROPERTYEXCEPTION("Required Property " + default + " not implemented.", widget = classname) 
            checked_props[default] = defaults[default]
    return checked_props


