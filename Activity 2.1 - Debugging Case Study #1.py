class Cat:
    # Made double underscores and changed spelling from bread to breed.
    def __init__(self, name, age, breed):
        self.name = name

        # Refer these attributes to parameters to make the code more practical.
        self.age = age
        self.breed = breed

    # Included "self" in the bracket here.
    def walk(self):
        print("*Evasiveley strolling*")


# Included age and breed here instead of in the class construction.
Cat = Cat("Kora", 1, "Devon Rex")
Cat.walk()
