class radio:
    def __init__(self, model, quantity):
        self.model = model
        self.quantity = quantity

    def name(self):
        print("Radio Model is " + self.model)

    def howMany(self):
        print(str(self.quantity) + " Radios to rent")
        


rental = radio("XPR 3500", "2")

rental.name()
rental.howMany()