from peewee import SqliteDatabase, Model, CharField, IntegerField, BooleanField

db = SqliteDatabase('vampires.sqlite3')


class Vampire(Model):
    name = CharField()
    age = IntegerField()
    in_coffin = BooleanField()
    drank_blood_today = BooleanField()

    """Represents a coven of vampires
    """
    # coven = []

    class Meta:
        database = db

    def list_all_vampires(self):
        for vamp in Vampire.select():
            if vamp.drank_blood_today:
                blood_string = ''
            elif vamp.drank_blood_today is False:
                blood_string = 'not '
            if vamp.in_coffin:
                coffin_string = ''
            elif vamp.in_coffin is False:
                coffin_string = 'not '
            print("This vampire is {} years old and their name is {}. They have {}drank blood today, and is {}in their coffin.".format(vamp.age, vamp.name, blood_string, coffin_string))

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


db.connect()
db.create_tables([Vampire])
vlad = Vampire()
# ******************************
# vlad.create(name='Vlad', age=243, in_coffin=False, drank_blood_today=False)
# delete from vampire where name = 'Vlad';
# ******************************
vlad.list_all_vampires()

# print(Vampire.coven)  # Just Vlad
# Vampire.sunrise()  # no change
# print(Vampire.coven)  # Still just Vlad
# Vampire.sunset()  # no change
# # kill off any vampire who isn't in their coffin and hasn't had blood today
# Vampire.sunrise()
# print(Vampire.coven)  # oh crap, Vlad's dead!
# vlad = Vampire.create("Vlad", '243', True, True)  # let's create a new Vlad
# print(Vampire.coven)  # just Vlad again
# Vampire.sunset()  # let's send him out again
# vlad.drink_blood()  # he's had some blood
# vlad.go_home()  # let's send him home as well
# Vampire.sunrise()  # and see what happened...
# print(Vampire.coven)  # Vlad's still alive, yay!
