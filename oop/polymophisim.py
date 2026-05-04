
## Duck typing
class Laptop:  ## duck
    def build(self):
        print("Laptop build")
class Desktop: ## craw
    def build(self):
        print("Desktop is build")

class Programmer:
    def code(self,machine:Laptop):
        print("Programmer is building")
        machine.build()



lenovo_yoga=Laptop()
beast=Desktop()
 


Wandola=Programmer()
Wandola.code(lenovo_yoga)
Wandola.code(beast)