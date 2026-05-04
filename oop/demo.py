
class Computer:
    #  class variable --accessed by all objects
    #  cpu="15"
    def __init__(self,cpu,ram,ssd): 
       print("Init called")
       self.cpu=cpu
       self.ram=ram
       self.ssd=ssd
    def config(self):
          print("config",self.cpu ,self.ram ,self.ssd)

comp1=Computer("I5","16GB","512")
comp2=Computer("I9","96GB","2TB")

comp2.config()



# Computer.config(comp1)
# Computer.config(comp2)

comp1.config()
