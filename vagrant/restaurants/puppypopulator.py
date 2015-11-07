from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from puppy_db_setup import Base, Shelter, Puppy, Adopter, Profile
#from flask.ext.sqlalchemy import SQLAlchemy
from random import randint
import datetime
import random



engine = create_engine('sqlite:///puppies.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


#Add Shelters
shelter1 = Shelter(name = "Oakland Animal Services", address = "1101 29th Ave", city = "Oakland", state = "California", zipCode = "94601", website = "oaklandanimalservices.org")
session.add(shelter1)

shelter2 = Shelter(name = "San Francisco SPCA Mission Adoption Center", address="250 Florida St", city="San Francisco", state="California", zipCode = "94103", website = "sfspca.org")
session.add(shelter2)

shelter3 = Shelter(name = "Wonder Dog Rescue", address= "2926 16th Street", city = "San Francisco", state = "California" , zipCode = "94103", website = "http://wonderdogrescue.org")
session.add(shelter3)

shelter4 = Shelter(name = "Humane Society of Alameda", address = "PO Box 1571" ,city = "Alameda" ,state = "California", zipCode = "94501", website = "hsalameda.org")
session.add(shelter4)

shelter5 = Shelter(name = "Palo Alto Humane Society" ,address = "1149 Chestnut St." ,city = "Menlo Park", state = "California" ,zipCode = "94025", website = "paloaltohumane.org")
session.add(shelter5)

#Add Puppies

male_names = ["Bailey", "Max", "Charlie", "Buddy","Rocky","Jake", "Jack", "Toby", "Cody", "Buster", "Duke", "Cooper", "Riley", "Harley", "Bear", "Tucker", "Murphy", "Lucky", "Oliver", "Sam", "Oscar", "Teddy", "Winston", "Sammy", "Rusty", "Shadow", "Gizmo", "Bentley", "Zeus", "Jackson", "Baxter", "Bandit", "Gus", "Samson", "Milo", "Rudy", "Louie", "Hunter", "Casey", "Rocco", "Sparky", "Joey", "Bruno", "Beau", "Dakota", "Maximus", "Romeo", "Boomer", "Luke", "Henry"]

female_names = ['Bella', 'Lucy', 'Molly', 'Daisy', 'Maggie', 'Sophie', 'Sadie', 'Chloe', 'Bailey', 'Lola', 'Zoe', 'Abby', 'Ginger', 'Roxy', 'Gracie', 'Coco', 'Sasha', 'Lily', 'Angel', 'Princess','Emma', 'Annie', 'Rosie', 'Ruby', 'Lady', 'Missy', 'Lilly', 'Mia', 'Katie', 'Zoey', 'Madison', 'Stella', 'Penny', 'Belle', 'Casey', 'Samantha', 'Holly', 'Lexi', 'Lulu', 'Brandy', 'Jasmine', 'Shelby', 'Sandy', 'Roxie', 'Pepper', 'Heidi', 'Luna', 'Dixie', 'Honey', 'Dakota']

puppy_images = ["http://pixabay.com/get/da0c8c7e4aa09ba3a353/1433170694/dog-785193_1280.jpg?direct", "http://pixabay.com/get/6540c0052781e8d21783/1433170742/dog-280332_1280.jpg?direct","http://pixabay.com/get/8f62ce526ed56cd16e57/1433170768/pug-690566_1280.jpg?direct","http://pixabay.com/get/be6ebb661e44f929e04e/1433170798/pet-423398_1280.jpg?direct","http://pixabay.com/static/uploads/photo/2010/12/13/10/20/beagle-puppy-2681_640.jpg","http://pixabay.com/get/4b1799cb4e3f03684b69/1433170894/dog-589002_1280.jpg?direct","http://pixabay.com/get/3157a0395f9959b7a000/1433170921/puppy-384647_1280.jpg?direct","http://pixabay.com/get/2a11ff73f38324166ac6/1433170950/puppy-742620_1280.jpg?direct","http://pixabay.com/get/7dcd78e779f8110ca876/1433170979/dog-710013_1280.jpg?direct","http://pixabay.com/get/31d494632fa1c64a7225/1433171005/dog-668940_1280.jpg?direct"]

# Descriptions
puppy_descriptions = ["Frumpy little dumpy dump.","Cute as a button.","Hit by an ugly stick.","Jowls bigger than a 777.","Has feet in need of clown shoes.","If you build it, this puppy will eat it.","Thinks it's a cat.","Needs plenty of sleep, and food.","Will steal your heart, and bury it.","Given a bone by this old man.","You dislike yappy little dogs, well too bad.","The Jackson Pollack of dogs but uses slobber instead of paint.","Likes shiney things, yeah yeah yeah, chase the shiney.","Has ninety-nine problems, but you aren't one."]

puppy_needs = ["Love","Affection","Shock Collar","Cat food","Frisbee","Ball!","Scraps",
              "Bacon","The cat","Lots of Exercise","A towel for slobber collection",
              "A Ribbon for its hair","Lots of squeaky toys","Deworming medicine",
               "No squeaky toys, Death to squeaky!","A Pedicure","Flea Collar",
               "A breath mint","A lot of breath mints","For you to throw the stick."]


# Adopters
adopter_names = ["George Tanaka","Bill Witherspoon","Johnny Football","Johnny Utah",
                "John Wick","Meryl Streep","Jacob Dylan","Troy Armstong",
                 "Tennessee Williams","Billy Bob McNugget","Kim Bigassian",
                "Sarah Failin","Garet Jax","Gandalf the Grey","Saruman the White",
                "Nathan Barnes","Amy Adams","Keira Knightley","Jessica Chastain",
                "Jennifer Lawrence"]


def removeAdopterName(name):
    if name in adopter_names:
        adopter_names.remove(name)


a_name = random.choice(adopter_names)
adopter1 = Adopter(name = random.choice(adopter_names))
removeAdopterName(a_name)
session.add(adopter1)

a_name = random.choice(adopter_names)
adopter2 = Adopter(name = random.choice(adopter_names))
removeAdopterName(a_name)
session.add(adopter2)

a_name = random.choice(adopter_names)
adopter3 = Adopter(name = random.choice(adopter_names))
removeAdopterName(a_name)
session.add(adopter3)

a_name = random.choice(adopter_names)
adopter4 = Adopter(name = random.choice(adopter_names))
removeAdopterName(a_name)
session.add(adopter4)

a_name = random.choice(adopter_names)
adopter5 = Adopter(name = random.choice(adopter_names))
removeAdopterName(a_name)
session.add(adopter5)


#This method will make a random age for each puppy between 0-18 months(approx.) old from the day the algorithm was run.
def CreateRandomAge():
    today = datetime.date.today()
    days_old = randint(0,540)
    birthday = today - datetime.timedelta(days = days_old)
    return birthday


#This method will create a random weight between 1.0-40.0 pounds (or whatever unit of measure you prefer)
def CreateRandomWeight():
    return random.uniform(1.0, 40.0)


def CreateProfile(p_name, p_gender):
    new_profile = Profile(
        name = p_name,
        gender = p_gender,
        description = random.choice(puppy_descriptions),
        specialNeeds = random.choice(puppy_needs),
        dateOfBirth = CreateRandomAge(),
        picture= random.choice(puppy_images),
        weight= CreateRandomWeight())
    return new_profile


def ChooseAdopter():
    adopter_arr = [adopter1, adopter2, adopter3, adopter4, adopter5]
    ad = random.choice(adopter_arr)
    return ad


for i,x in enumerate(male_names):
    new_profile = CreateProfile(x,"male")
    session.add(new_profile)

    new_puppy = Puppy(
        shelter_id = randint(1,5),
        profile = new_profile)

    new_puppy.adopters.append(ChooseAdopter())

    session.add(new_puppy)
    session.commit()

for i,x in enumerate(female_names):
    new_profile = CreateProfile(x,"female")
    session.add(new_profile)

    new_puppy = Puppy(
        shelter_id = randint(1,5),
        profile = new_profile)

    new_puppy.adopters.append(ChooseAdopter())

    session.add(new_puppy)
    session.commit()
'''
# Ascending Name
pup = sess.query(Puppy).order_by(Puppy.name).all()
for p in pup:
    print p.name
    print "\n"

# Puppies younger than 6 months old, ordered by youngest first
cutoff = datetime.date.today() - datetime.timedelta(days = 180)
pup = sess.query(Puppy).filter(Puppy.dateOfBirth > cutoff).order_by(desc(Puppy.dateOfBirth)).all()

# Ascending Weight
pup = sess.query(Puppy).order_by(Puppy.weight).all()
for p in pup:
    print p.name
    print p.weight
    print "\n"
pup = sess.query(Puppy).order_by(Puppy.shelter_id).all()
for p in pup:
    print p.name
    print p.shelter.name
    print "\n"

'''
