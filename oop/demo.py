
class Computer:
    #  class variable --belong to class
    brand="Wandola Ai"
    #instances variables  -- belongs to object
    def __init__(self,cpu,ram,ssd): 
       print("Init called")
       self.cpu=cpu
       self.ram=ram
       self.ssd=ssd
    def config(self):
          print("config",self.cpu ,self.ram ,self.ssd)
    @classmethod
    def info(cls):
        return cls.brand
    @staticmethod
    def gb_to_bytes(gb):
        return gb *(1024**3)

comp1=Computer("I5","16GB","512")
comp2=Computer("I9","96GB","2TB")

comp2.config()
# Computer.config(comp1)
# Computer.config(comp2)

comp1.config()

print(Computer.gb_to_bytes(16))
