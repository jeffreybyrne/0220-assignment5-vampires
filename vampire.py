class Vampire:
    """Represents a coven of vampires
    """
    coven = []

    def __init__(self, name, age, in_coffin, drank_blood_today):
        self.name = name
        self.age = age
        self.in_coffin = in_coffin
        self.drank_blood_today = drank_blood_today

    @classmethod
    def create(cls, name, age, in_coffin, drank_blood_today):
        """Creates a new vampire instance and adds it to the list of vampires
        in the coven
        """
        new_vamp = Vampire(name, age, in_coffin, drank_blood_today)
        Vampire.coven.append(new_vamp)
        return new_vamp

    def drink_blood(self):
        # Set the instantiated vampire's blood drinking boolean to true
        self.drank_blood_today = True

    @classmethod
    def sunrise(cls):
        # For each vampire in the coven
        for num in range(0, len(Vampire.coven)):
            curr_vamp = Vampire.coven[num]
            # If they haven't drank blood or they aren't in their coffin
            if not curr_vamp.drank_blood_today or not curr_vamp.in_coffin:
                # Make 'em fry'
                Vampire.coven.remove(curr_vamp)

    @classmethod
    def sunset(cls):
        # For each vampire in the coven
        for num in range(0, len(Vampire.coven)):
            curr_vamp = Vampire.coven[num]
            # Kick them out of their coffin
            curr_vamp.in_coffin = False
            # Make them thirst once more
            curr_vamp.drank_blood_today = False

    def go_home(self):
        # Send the instantiated vampire back to it's coffin
        self.in_coffin = True


vlad = Vampire.create("Vlad", '243', True, True)
print(Vampire.coven)  # Just Vlad
Vampire.sunrise()  # no change
print(Vampire.coven)  # Still just Vlad
Vampire.sunset()  # no change
# kill off any vampire who isn't in their coffin and hasn't had blood today
Vampire.sunrise()
print(Vampire.coven)  # oh crap, Vlad's dead!
vlad = Vampire.create("Vlad", '243', True, True)  # let's create a new Vlad
print(Vampire.coven)  # just Vlad again
Vampire.sunset()  # let's send him out again
vlad.drink_blood()  # he's had some blood
vlad.go_home()  # let's send him home as well
Vampire.sunrise()  # and see what happened...
print(Vampire.coven)  # Vlad's still alive, yay!
