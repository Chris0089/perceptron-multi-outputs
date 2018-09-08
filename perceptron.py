import random

INPUTFILE = 'input-values.txt'
DESIREDFILE = 'desired-values.txt'
ETA = 0.4
BOTTOM_LIMIT = -1
TOP_LIMIT = 1


class DataAccessObject:
    inputData = []
    desiredOutput = []

    def __init__(self):
        self.get_data()

    def get_data(self):
        file = open(FILENAME, "r")
        next(file)
        for line in file:
            fields = line.split(" ")
            size = len(fields)
            self.desiredOutput.append(float(fields[0]))
            if not self.inputData:
                for value in range(1, size):
                    self.inputData.append([])
            for value in range(1, size):
                self.inputData[value-1].append(float(fields[value]))


class Perceptron(DataAccessObject):
    inputData = []
    inputQuantity = None
    inputSize = None
    weightData = []
    threshold = []  # bias
    output = []
    desiredOutput = []
    v = []
    summation = []
    iteration = 0

    def __init__(self):
        self.inputData = DataAccessObject.inputData.copy()
        self.desiredOutput = DataAccessObject.desiredOutput.copy()
        self.inputQuantity = len(self.inputData)
        self.inputSize = len(self.desiredOutput)
        self.generate_random_values()
        self.main_algorithm()

    def generate_random_values(self):
        for value in range(0, self.inputQuantity):
            self.weightData.append([])
        for value in range(0, self.inputQuantity):
            for inputSize in range(0, self.inputSize):
                self.weightData[value].append(random.uniform(BOTTOM_LIMIT, TOP_LIMIT))
        for size in range(0, self.inputSize):
            self.threshold.append(random.uniform(BOTTOM_LIMIT, TOP_LIMIT))

    def calculate_output(self):
        self.output = []
        self.summation = []
        self.v = []
        for row in range(0, self.inputSize):
            self.summation.append(0)
            self.v.append(0)
            for column in range(0,self.inputQuantity):
                self.summation[row] += self.inputData[column][row] * self.weightData[column][row]
            self.v[row] = self.summation[row] + self.threshold[row] #changed, summed bias
            self.output.append(self.activation_function(self.v[row]))
        self.iteration += 1

    def activation_function(self, value):
        if value <= 0:
            return 0.0
        else:
            return 1.0

    def is_the_desired_output(self):
        if self.output == self.desiredOutput:
            return True
        else:
            return False

    def training(self):
        for row in range(0,self.inputSize):
            if self.desiredOutput[row] != self.output[row]:
                error = self.desiredOutput[row] - self.output[row]
                self.threshold[row] = self.threshold[row] + (ETA * error)
                for column in range(0, self.inputQuantity):
                    self.weightData[column][row] = self.weightData[column][row] +\
                                                   (ETA * error * self.inputData[column][row])

    def main_algorithm(self):
        self.calculate_output()
        self.print_data()
        while not self.is_the_desired_output():
            print(self.iteration)
            self.training()
            self.calculate_output()
            self.print_data()
        print("Finished")

    def print_data(self):
        print("Iteraciones = " + str(self.iteration))
        print("ETA = " + str(ETA))
        print("y   | d   | x1  | x2  | w1       | w2     | umbral    |")
        for row in range (0, self.inputSize):
            print( str(self.output[row]) + " | "
                   + str(self.desiredOutput[row]) + " | "
                   + str(self.inputData[0][row]) + " | "
                   + str(self.inputData[1][row]) + " | "
                   + str(round(self.weightData[0][row],5)) + " | "
                   + str(round(self.weightData[1][row],5)) + " | "
                   + str(round(self.threshold[row],5)) + " | "
                   )

dao = DataAccessObject()
perceptron = Perceptron()

