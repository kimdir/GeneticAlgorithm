import ast
"""Defines individual components and the Components class."""

# ---------- Generic Type Classes ---------- #

class GenericComponent(object):
    """Generic component class for defining common attributes. Modify this to
        change attributes common to all components."""

    def __init__(self,name):

        self.name = name

        # Evaluation
        self.mass = 0 # kg
        self.cost = 0 # $
        self.isViable = True

        # Genetics
        self.design_variables = DesVarManager()
        self.calculated_variables = CalcVarManager()
        self.stress_variables = StressVarManager()
        self.misc_variables = MiscVarManager()
        self.chromosome = []

        # Identifiers
        self.isCylinder = False
        self.isStructural = False
        self.isFastener = False

        self.isProximal = False
        self.isDistal = False
        self.isLateral = False
        self.isMedial = False
        self.isAnterior = False
        self.isPosterior = False

        self.hasAxial = False
        self.hasShear = False
        self.hasBending = False
        self.hasTorsion = False
        self.hasBuckling = False
        self.hasContact = False
        self.hasPressure = False

class GenericCylinder(GenericComponent):
    """Generic actuation component. Modify this to change attributes common to
        all actuation cylinder components"""

    def __init__(self):
        super.__init__()
        self.movementType = ""
        self.maxForce = 0 # N
        self.isCylinder = True

class GenericStructure(GenericComponent):
    """Generic structural component. Modify this to change attributes common to
        all structural components."""

    def __init__(self):
        super.__init__()
        self.maxStress = 0 # MPa
        self.maxDeflection = 0 # m
        self.FOS = 0
        self.isStructure = True

class GenericFastener(GenericComponent):
    """Generic fastener component. Currently inlcuded to help with
        categorization."""

    def __init__(self):
        super.__init__()
        self.isFastener = True

# ---------- Generic Location Components ---------- #

# Legacy code; Consider removal

class GenericLocation(object):
    """Generic Location object. Modify this to change all location objects."""

    def __init__(self):
        self.isAnterior = False
        self.isPosterior = False
        self.isLateral = False
        self.isMedial = False
        self.isProximal = False
        self.isDistal = False

class GenericAnterior(GenericLocation):
    """Generic anterior component. Modify this to change all anterior components."""

    def __init__(self):
        GenericLocation.__init__()
        self.isAnterior = True

class GenericPosterior(GenericLocation):
    """Generic anterior component. Modify this to change all anterior components."""

    def __init__(self):
        GenericLocation.__init__()
        self.isPosterior = True

class GenericLateral(GenericLocation):
    """Generic anterior component. Modify this to change all anterior components."""

    def __init__(self):
        GenericLocation.__init__()
        self.isLateral = True

class GenericMedial(GenericLocation):
    """Generic anterior component. Modify this to change all anterior components."""

    def __init__(self):
        GenericLocation.__init__()
        self.isMedial = True

class GenericProximal(GenericLocation):
    """Generic anterior component. Modify this to change all anterior components."""

    def __init__(self):
        GenericLocation.__init__()
        self.isProximal = True

class GenericDistal(GenericLocation):
    """Generic anterior component. Modify this to change all anterior components."""

    def __init__(self):
        GenericLocation.__init__()
        self.isDistal = True

# ---------- Assemblies ---------- #
class Assembly(self):
    """Generic assembly that holds references to the components that are a part of the
    assembly. Used for informational purposes primarily."""

    def __init__(self,name,ID):
        self.components = {}
        self.name = name
        self.ID = ID

    def addComponent(self,component):
        self.components[component.name]

# ---------- Manager Classes ---------- #

class ComponentManager(object):
    """Container class for all components regardless of assembly. Used for
        inheritance in member creation."""

    def __init__(self):
        self.components = {}
        self.componentID = 0

    def addComponent(self,component):
        if not component.name in self.components:
            assert(component.ID == self.componentID)
            self.components[component.name] = component
            componentID = componentID + 1

class AssemblyManager(object):
    """Container describing all assemblies of components. Gives overview of
        functional units."""

    def __init__(self):
        self.assemblies = {}
        self.assemblyID = 0

    def addAssembly(self,name):
        if not name in self.assemblies:
            self.assemblies[name] = Assembly(name,assemblyID)
            assemblyID = assemblyID + 1

class VarManager(object):
    """Defines the general variable manager for storing variables. Used for
        categorization."""

    def __init__(self):
        variables = {}

    def calculate(target,EqDict,DVM,CVM,SVM):
    """Sets calculated variables based on the equations given in the component file.
        Var should be a string name for the variable and eq should be the equation for
        the function written in Python notation and including class names in the
        variables. Takes the DesValManager, CalcVarManager, StressVarManager of the component to reduce character load
        in the component files."""

        for var,eq in EqDict.items():
            target.variables[var] = (eval(compile(ast.parse(str3,mode="eval"),'<ast>',mode='eval')))
        return

class DesVarManager(VarManager):
    """Manages design variables. These are the only ones that should be changed
        in the breeding process, then CalcVars should be calculated, then
        StressVars calculated."""

    def __init__(self):
        pass

class CalcVarManager(VarManager):
    """Manages calculated variables, including equations for calculations."""

    def __init__(self):
        CVEquations = {}

class StressVarManager(VarManager):
    """Manages stress variables, to be determined after calculated variables
        are evaluated."""

    def __init__(self):
        pass

class MiscVarManager(VarManager):
    """Manages miscellaneous variables, such as materials and manufacturing
        processes."""

    def __init__(self):
        pass

# ---------- Component Template Generator  ---------- #

class ComponentBuilder(object):
    """Builds components from user input."""

    def __init__(self):
        pass

    def refereshComponents(self):
        self.component_names = []
        with open(self.file_name) as comp_file:
            name_lines = [x for x in comp_file.readlines if x.startswith('target.component_name')]
            for n in name_lines:
                self.component_names.append(n.split()[2])
