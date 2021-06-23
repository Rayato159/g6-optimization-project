import os

class Black_Box_Function:

    def __init__(self, f_input, f_output, execute):
        self.f_input = f_input
        self.f_output = f_output
        self.execute = execute

    def getFunction(self, x1, x2=None):
        self.x1 = x1
        self.x2 = x2

        with open("./" + self.f_input, "w") as w:
            if (self.x2 == None):
                w.write(f"{self.x1}")
            else:
                w.write(f"{self.x1} {self.x2}")
        
        os.system("wine " + self.execute + " > /dev/null 2>&1")
        # os.system("clear")

        with open("./" + self.f_output, "r") as f:
            self.value = f.readline()

        return float(self.value)
