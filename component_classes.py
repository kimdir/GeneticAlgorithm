import ast
"""Defines individual components and the Components class."""


# ---------- Variable Type Classes ---------- #

# ---------- Generic Type Classes ---------- #

class GenericComponent(object):
    """Generic component class for defining common attributes. Modify this to
        change attributes common to all components."""

    def __init__(self):
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


# ---------- Assembly Components ---------- #
class Assembly(self):
    """Generic assembly that holds references to the components that are a part of the
    assembly. Used for informational purposes primarily."""

    def __init__(self):
        self.components = {}

# ---------- Manager Classes ---------- #

class ComponentManager(object):
    """Container class for all components regardless of assembly. Used for
        inheritance in member creation."""

    def __init__(self):
        # Femur Location Components #

        # Tibia Location Components #

        # Foot Location Components #

class AssemblyManager(object):
    """Container describing all assemblies of components. Gives overview of
        functional units."""

    def __init__(self):
        self.assemblyList = []

    def addAssembly(self,name):
        self.assemblyList.append

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
        self.file_name = 'component_list.txt'
        self.component_names = []

        self.name_label = 'target.component_name = '
        self.desig_label = 'target.designation = '
        self.tgt = 'target.'
        self.des_var_header = '#design variables:'
        self.calc_var_header = '#calculated variables:'
        self.stress_var_header = '#stress variables:'

    def addComponent(self):
        """Prompts the user for information needed to create a new component,
            then formats and saves the component to the component_list file."""

        # Collect new component information
        self.comp_name = input("Component Name: ")
        self.comp_desig = input("Designation: ")

        self.des_var_count = input("How many design variables? ")
        self.des_vars = self.defineVariables(self.des_var_count,"design")

        self.calc_var_count = input("How many calculated variables? ")
        self.calc_vars = self.defineVariables(self.calc_var_count,"calculated")

        self.stress_func_count = input("How many stress functions? ")
        self.stress_funcs = self.defineVariables(self.stress_func_count,"stress")

        self.misc_var_count = input("How many misc vars? ")
        self.misc_vars = self.defineVariables(self.misc_var_count,"misc")

        # Write information to component_list file in correct format


        self.refereshComponents()

    def refereshComponents(self):
        self.component_names = []
        with open(self.file_name) as comp_file:
            name_lines = [x for x in comp_file.readlines if x.startswith('target.component_name')]
            for n in name_lines:
                self.component_names.append(n.split()[2])

    def defineVariables(self,count,var_type):
        x = 0
        holder = []
        while x < count:
            if var_type == "design":
                var_name = input("Variable Name: ")
                holder.append(str(self.target_label + var_name))
            elif var_type == "calculated":
                var_name = str(input("Variable Name: "))
                var_eq = str(input("Variable Equation:"))
                holder.append(str(var_name + " = " + var_eq))
            elif var_type == "stress":
                stress_type = str(input("Stress Type: "))
                stress_params = str(input("Enter parameters separated by commas:"))
                holder.append(str(var_name + " = " + var_eq))
            elif var_type == "misc":
                holder.append(input("Variable Name: "))
            else: input("Bad variable classification")
            x += 1
        return holder
