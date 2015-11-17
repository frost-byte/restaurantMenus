import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import random

from puppy_db_setup import Base, Puppy, Profile, Shelter, Adopter
from trait import Trait

engine = create_engine('sqlite:///puppies.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def setCapacity():
    shelters = session.query(Shelter).order_by(Shelter.name).all()
    for s in shelters:
        s.maximum_capacity = 50
        s.current_occupancy = random.randint(46,50)
        session.add(s)

    session.commit()


def checkInPuppy():
    # Add a Puppy to a shelter
    print "Check in a new Puppy\n"
    print "++++++++++++++++++++\n"
    name = raw_input("Name: ")
    picture = raw_input("Picture URL: ")
    description = raw_input("Description: ")
    gender = raw_input("Gender: ")
    weight = raw_input("Weight: ")
    needs = raw_input("Needs: ")
    birthDate = raw_input("Birthdate: (yyyy-mmm-dd)")
    shelter = chooseShelter()
    prof = Profile(
        name=name,
        picture=picture,
        description=description,
        gender=gender,
        specialNeeds=needs,
        weight=weight,
        dateOfBirth=datetime.strptime(birthDate, "%Y-%b-%d"))

    session.add(prof)
    pup = Puppy(shelter=shelter,profile=prof)
    session.add(pup)
    session.commit()


def listShelters(shelters):
    for i in range(len(shelters)):
        print str(i+1) + ". " + shelters[i].name + "(" + str(shelters[i].current_occupancy) + ")"

        if i % 8 == 0 and i > 0:
            raw_input("Press Any Key to Continue")


def chooseShelter():
    shelters = session.query(Shelter).order_by(Shelter.name).all()

    while True:
        listShelters(shelters)
        shelterNumber = int(raw_input("Select a shelter: "))
        shelterNumber = shelterNumber - 1
        if( shelterNumber < 0 or shelterNumber >= len(shelters)):
            print "Invalid choice, choose a number between 1 and " + str(len(shelters))
            continue
        else:
            shelter = shelters[shelterNumber]
            if shelter.current_occupancy >= shelter.maximum_capacity:
                print "That shelter is full, please choose another."
                continue
            else:
                return shelter

    return None


def adoptPuppy(puppy_id, adopters):
    puppy = session.query(Puppy).filter(Puppy.id == puppy_id).one()

    if puppy is not Null:
        for a in adopters:
            puppy.adopters.append(a)
        session.add(puppy)
        session.commit()


'''
def balancePuppyLoad():
    # Equally balance the number of puppies across shelters.
'''


def testTextTrait():
    profile = session.query(Profile).filter_by(id = 1).one()

    trait = Trait(
        "name",
        profile.name
    )

    print trait.asInputElement("editPuppyForm")
    print trait.asOutputElement()


def testSelectTrait():
    profile = session.query(Profile).filter_by(id = 1).one()

    sexes = ['male','female']

    trait = Trait(
        "gender",
        profile.gender,
        "select",
        sexes
    )

    print trait.asInputElement("editPuppyForm")
    print trait.asOutputElement()


def testDateTrait():
    profile = session.query(Profile).filter_by(id = 1).one()

    trait = Trait(
        "birthday",
        profile.dateOfBirth,
        "date"
    )

    print trait.asInputElement("editPuppyForm")
    print trait.asOutputElement()


def testTextAreaTrait():
    profile = session.query(Profile).filter_by(id = 1).one()

    trait = Trait(
        "description",
        profile.description,
        "textarea"
    )

    print trait.asInputElement("editPuppyForm")
    print trait.asOutputElement()


def testTraits():

    testTextTrait()
    testSelectTrait()
    testDateTrait()
    testTextAreaTrait()
