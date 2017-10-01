"""Defines the classes used in the genetic algorithm."""
import component_classes
import random

# ---------- Member Classes ---------- #

class Member(object):
    """Parent class for all Members. Defines common traits shared between
        Members."""

    def __init__(self,memID):
        # --- Member Attributes --- #
        self.age = 0
        self.fitness = 0
        self.memID = memID
        self.breed_chance = 0.0
        self.isViable = True
        self.isEvaluated = False

        # --- Managers --- #
        self.components = ComponentManager()
        self.assemblies = AssemblyManager()

        # --- Utility Variables --- #
        self.bin_place = 6 "Better way to do this?"

    def attributeList(target):
        attr_list = [x for x in target.__dict__() if not x.startswith('__')]
        return attr_list

class InitialMember(Member):
    """Member generated at initialization. These members should have randomized
        design component values."""

    def __init__():
        super.__init__()

    def binaryEncode(value):
    	"""Encodes a numerical value into a binary string"""
        #Values currently limited to integers, will consider decimals later
        bin_count = self.bin_place

        # Special Case:
        if value == 0:
    		bin_string = [0] * self.bin_place
    		return bin_string

        #Construct binary string
        # Hard-coded values: consider revising. Upper value limit of 63

        bit_max = bin_count
        bin_string =[0] * bin_count
        current_sum =  0
        while bin_count >= 1:
            bit_val = 2**(bin_place-1)
    		try:
    			val_test = int(value) - (bit_val)
    		except ValueError:
    			print(value)
    			print(type(value))
    			input("Value Error")
    		current_sum += bit_val

    		if current_sum > int(value):
    			current_sum -= bit_val
    			bin_string[bit_max-bin_place] = 0
    		elif val_test < 0:
    			bin_string[bit_max-bin_place] = 0
    		else:
    			bin_string[bit_max-bin_place] = 1
    		bin_count -= 1
    	return bin_string

    def writeGenome(self):
        """Iterates through components and writes each component's binary
            chromosome."""
        for x in self.attributeList(self.components):
            self.writeChromosome(x)

    def writeChromosome(target):
        """Writes the design values into the binary chromosome."""
        for des_var in self.attributeList(target.design_variables)
            binary = self.binaryEncode(des_var)
            for bit in binary:
                target.genome.append(bit)

class ChildMember(Member):
    """Member generated by the breeding process. No component value should be
        randomized for this type of member."""

    def __init__():
        super.__init__()

    def readGenome(self):
        """Iterates through member components and writes each component's binary
            chromosome."""
        for x,y in self.components.__dict__().items):
            self.readChromosome(y)

    def readChromosome(self,target):
        """Reads the binary genome into design variables."""

        chromosome = target.chromosome
        gene_list = target.design_variables.__dict__
        assert len(chromosome)/target.bin_place == len(gene_list)
        val_list = self.binaryDecode(chromosome)
        for des_var,val in target.components:
            setattr(target,des_val,val_list.pop(0))

    def binaryDecode(self,chromosome):
    	"""Converts a binary genome into a list of values"""

        val_list = []
        temp_gene = []*self.bin_place
        while len(chromosome)>0:
            for x in temp_gene:
                x = chromosome.pop(0)
            eval_gene = temp_gene[::-1]
            digit_ID = 0
            value = 0
            for bit_val in eval_gene:
                value += bit_val * 2**digit__ID
            val_list.append(value)
        return val_list

class Breeder(object):
    """Contains the commands for member breeding."""

    def __init__(self):
        # Population Requirement Modifiers
        self.base_mod = 0.2
        self.cycle_mod = 0
        self.pop_mod = 0
        self.growth_mod = self.base_mod * self.cycle_mod * self.pop_mod
        self.growth_rate = 1 + self.growth_mod

        # Breeding Thresholds
        self.crossover_thresh = 0.6
        self.mutate_thresh = 0.8

        # Factories
        self.MemberFactory = MemberFactory()

    def refreshMods(self,StatManager):
        self.cycle_mod = math.sinf(random.random*2*math.pi())
        self.pop_mod = random.random * 10 * StatManager.population_size/1000
        self.growth_rate = 1 + self.growth_mod
        self.growth_mod = self.base_mod * self.cycle_mod * self.pop_mod
        self.growth_rate = 1 + self.growth_mod
        self.goal_pop = self.growth_rate * StatManager.population_size

    def qualify(PopManager):
        """Defines the reproduction chance range for each member based on their
            fitness compared to the whole fitness."""
        roulette_list = []
        breed_range = [0,0]
        last_val = 0
        for mem in PopManager.pop_list:
            breed_span = mem.fitness/PopManager.StatManager.total_fitness)
            breed_range[0] = last_val
            last_val += breed_span
            breed_range[1] = last_val
            roulette_list.append([mem,breed_range])
        assert (last_val > 0.99) and (last_val < 1.01)
        return roulette_list

    def match(roulette_list):
        """Roulette selection of breeding pairs based on fitness values of
            individual members compared to total overall fitness."""
        # -Tune fitness equations to prevent single members from always being
        #   selected?
        # -Restrict number of offspring from single member?
        parent1 = None
        parent2 = None

        while parent1.memID == parent2.memID:
            parent1_check = random.random
            parent2_check = random.random
            for x in roulette_list
                if x[1][0] < parent1_check < x[1][1]:
                    parent1 = x[0]
                elif x[1][0] < parent2_check < x[1][1]:
                    parent2 = x[0]

        return parent1, parent2

    def mate(self,parent1,parent2):
        """Breeds two members matched by fitness values and roulette selection.
            Each breeding produces two new children members."""

        children = [self.MemberFactory.newMember("child"),self.MemberFactory.newMember("child")]

        for [x for x in parent1.components.__dict__ if not x.startswith("__")]:
            component1 = getattr(parent1.components,x)
            component2 = getattr(parent2.components,x)
            child_component1 = getattr(children[0].components,x)
            child_component2 = getattr(children[1].components,x)

            assert len(component1.chromosome) == len(component2.chromosome)

            isCrossed = False
            cross_index = 1

            while isCrossed == False:
                cross_check = random.random()
                if cross_check > self.cross_thresh:
                    child_component1.chromosome = component1.chromosome
                    child_component2.chromosome = component2.chromosome
                    child_component1.chromosome[cross_index:] = component2.chromosome[cross_index:]
                    child_component2.chromosome[cross_index:] = temp_list
                    assert len(child_component1.chromosome) == len(child_component2.chromosome)
                    isCrossed = True
                    continue
                cross_index += 1
                if cross_index == len(component1.chromosome):
                    cross_index = 1

            self.mutate(child_component1)
            self.mutate(child_component2)
            assert len(child_component1.chromosome) == len(child_component2.chromosome)

        for child in children: child.readGenome()

        return children

    def mutate(chromosome):
        """Mutates genomes to prevent settling in local minima. Based on the
            mutate chance defined by the member, which increases with age."""

        for x in chromosome:
            mutate_check = random.random()
            if mutate_check > self.mutate_thresh:
                if x == 0: x = 1
                else: x = 0

        return chromosome

    def breed(self,PopManager):
        self.refreshMods(PopManager.StatManger)
        roulette_list = self.qualify(PopManager)

        while PopManager.StatManager.population_size < self.goal_pop:
            parent1,parent2 = self.match(self,roulette_list)
            child1,child2 = self.mate(parent1,parent2)
            PopManager.pop_list.append(child1)
            PopManager.pop_list.append(child2)
            PopManager.StatManager.updateStats()

    def startup(self):
        return self.MemberFactory.newMember(InitialMember)

# ---------- Evaluator Classes ---------- #

class Evaluator(object):
    """Generic Evaluator object. Modify this to modify all Evaluators."""

    def __init__(self):
        self.evaluated_fitness = 0.0

class AgeEvaluator(Evaluator):
    """Evaluates age parameters, killing members that die of age and
        incrementing the age value of members that survive."""

    def __init__(self):
        super.__init__()
        self.age_threshold = 4
        self.death_mod = 0.1

    def evaluate(self,target):
        death_chance = (target.age-self.age_threshold)*death_mod
        if death_chance < 0:
            death_chance = 0
        death_check = random.random()
        if death_check < death_chance:
            target.isViable = False
        else: target.age += 1

class CostEvaluator(Evaluator):
    """Evaluates costs of components based on material and manufacturing
        processes. Assigns fitness values based on the included equation."""

    def __init__(self):
        super.__init__()

    def evaluate(self,target):
        pass

class DynamicsEvaluator(Evaluator):
    """Evaluates dynamics of the design based on determined criteria. Assigns
        fitness values based on the included equation and marks components as
        non-viable if the criteria are not achieved by the design."""

    def __init__(self):
        super.__init__()

    def evaluate(self,target):
        pass

class FitnessEvaluator(Evaluator):
    """Evaluates the fitness of members according to a minimum threshold that
        shifts as generations increase."""

        def __init__(self):
            super.__init__()
            self.threshold_mod = 0.02
            self.threshold_offset = 100

        def evaluate(self,PopManager):
            gen_mod = (PopManager.StatManager.generation-self.threshold_offset)
            fit_mod = self.threshold_mod*PopManager.StatManager.max_fitness
            fitness_threshold = gen_mod * fit_mod
            for mem in PopManager.pop_list:
                if mem.fitness < fitness_threshold:
                    mem.isViable = False

class FluidsEvaluator(Evaluator):
    """Evaluates the fluid characteristics of a design."""

    def __init__(self):
        super.__init__()

    def evaluate(self,target):
        pass

class MassEvaluator(Evaluator):
    """Evaluates mass of components based on material and dimensions. Assigns
        fitness values based on the included equation."""

    def __init__(self):
        super.__init__()

    def evaluate(self,target):
        pass

class StrainEvaluator(Evaluator):
    """Evaluates strain on members, comparing them to component-defined
        limits. Assigns fitness values based on the included equation and marks
        them as non-viable if limits are not achieved by the design."""

    def __init__(self):
        super.__init__()

    def evaluate(self,target):
        pass

class StressEvaluator(Evaluator):
    """Evaluates stresses on members. Assigns fitness values based on the
        included equation and marks them as non-viable if the Factor
        of Safety (FoS) is not achieved by the design."""

    def __init__(self):
        super.__init__()
        self.FoS = 2

    def evaluate(self,target):
        pass

    def axial(self,target):
        pass

    def shear(self,target):
        pass

    def bending(self,target):
        pass

    def torsion(self,target):
        pass

    def buckling(self,target):
        pass

    def pressure(self,target):
        pass

    def contact(self,target):
        pass

# ---------- Manager Classes ---------- #

class FileManager(object):
    """Manages file input/output functions."""

    def __init__(self,target):
        self.components_location = "component_list.txt"

    def inputComponents(taget):
        while open(components_location) as compFile:
            for [line for line in iter(compFile) if line.startswith('target.')]:
                eval(line)

    def outputGenStats():
        pass

class PopulationManager(object):
    """Manages the population including calculating relevant information.""""

    def __init__(self):
        #Population Variables
        self.pop_list = []
        self.initial_population = 400

        #Managers
        self.Breeder = Breeder()
        self.StatManager = StatisticsManager()
        self.EvalManager = EvaluatorManager()

    def refreshPopList(self):
        self.pre_pop = len(self.pop_list)
        self.pop_list = [x for x in self.pop_list if x.isValid]
        self.StatManager.death_count += (self.pre_pop - len(self.pop_list))

    def newGeneration(self):
        self.refreshPopList()
        self.Breeder.breed(self)
        self.StatManager.updateStats(self)

    def evaluateMember(self,target):
        self.AgeEval.evaluate(target)
        self.StressEval.evaluate(target)

    def startup(self):
        while len(self.pop_list) < self.initial_population:
            self.pop_list.append(self.Breeder.startup())
            print("Generated " + len(self.pop_list)) + " Members")

class EvaluatorManager(object):
    """Manages creation of singleton evaluators and contains the evaluate call
        which triggers each evaluator."""

    def __init__(self):
        self.Age = AgeEvaluator()
        self.Stress = StressEvaluator()
        self.Deflection = DeflectionEvaluator()
        self.Cost = CostEvaluator()
        self.Mass = MassEvaluator()
        self.Dynamics = DynamicsEvaluator()
        self.Fluids = FluidsEvaluator()

    def evaluate(self,target):
        for [x for x in dir(self) if not x.startswith("__")]:
            current_evaluator = getattr(self,x)
            current_evaluator.evaluate(target)
            if target.isValid == False:
                break

class PatientManager(object):
    """Manages patient data, such as limb length and height."""

    def __init__(self):
        pass
# ---------- Factory Classes ---------- #

class MemberFactory(object):
    """Factory that constructs new members and tracks generations. Constructs
        the proper members based on what phase of the algorithm is running."""

    memberID = 0

    def __init__(self):
        pass

    def newMember(memType):
        if memType == "initial":
            newMember = InitialMember(memberID)
            memberID += 1
        elif memType == "child"
            newMember = ChildMember(memberID)
            memberID += 1
        return newMember

class GeneticAlgorithm(object):
    """Wrapper for all genetic algorithm functions. Used to initialize the
        optimization process."""

    def __init__(self):
        self.Patient = PatientManager()
        self.Population = PopulationManager()
        self.Files = FileManager()

    def run(self):
        self.Population.startup()

# ---------- End of Classes ---------- #

if __name__ == '__main__':
    GenAlg = GeneticAlgorithm()
    GenAlg.run()
