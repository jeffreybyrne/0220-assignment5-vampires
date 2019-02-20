class Vampire:
    """Represents a coven of vampires
    """
    coven = []

    def __init__(self,name,age,in_coffin,drank_blood_today):
        self.name = name
        self.age = age
        self.in_coffin = in_coffin
        self.drank_blood_today = drank_blood_today

    @classmethod
    def create(cls,name,age,in_coffin,drank_blood_today):
        """Creates a new vampire instance and adds it to the list of vampires
        in the coven
        """
        new_vamp = Vampire(name,age,in_coffin,drank_blood_today)
        Vampire.coven.append(new_vamp)
        return new_vamp
