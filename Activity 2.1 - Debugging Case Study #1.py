class Cat:
    # Made double underscores and changed spelling from bread to breed.
    def __init__(self, name, age, breed):
        self.name = name
        self.age = 1
        self.breed = "Devon Rex"

    # Included "self" in the bracket here.
    def walk(self):
        print("*Evasiveley strolling*")


# Included age and breed here.
Cat = Cat("Kora", 2, "Ragdoll")
Cat.walk()
