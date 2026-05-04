
class Computer:
    #  class variable --accessed by all objects
    #  cpu="15"
    def __init__(self):
       print("Init called")
     def config(self):
          print("i7,16GB,1TB")

comp1=Computer()
comp2=Computer()

print(comp1.cpu)

# Computer.config(comp1)
# Computer.config(comp2)

comp1.config()
