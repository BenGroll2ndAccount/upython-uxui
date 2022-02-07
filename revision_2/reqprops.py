class PROPMAP():
    def uPBOX_PROPS_CHECK(props):
        return True
    def uCARD_PROPS_CHECK(props):
        return True
    
def propcheck(classname, props):
    return getattr(PROPMAP, classname + "_PROPS_CHECK")(props)



