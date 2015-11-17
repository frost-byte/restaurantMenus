from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric, Table
from sqlalchemy.orm import relationship

from trait import Trait
from database import Base


# Many to Many relationship between Puppy and Adopter
association_table = Table('association', Base.metadata,
                         Column('puppy_id', Integer, ForeignKey('puppy.id')),
                         Column('adopter_id', Integer, ForeignKey('adopter.id'))
                         )


class Shelter(Base):
    __tablename__ = "shelter"

    name = Column(String(80), nullable = False)
    address = Column(String(250), nullable = False)
    city = Column(String(250), nullable = False)
    state = Column(String(50), nullable = False)
    zipCode = Column(String(5), nullable = False)
    website = Column(String(250), nullable = False)
    current_occupancy = Column(Integer, nullable = False, default=0)
    maximum_capacity = Column(Integer, nullable = False, default=5)
    id = Column(Integer, primary_key = True)


    @staticmethod
    def defaultTraits():
        return [
            Trait("name"),
            Trait("address"),
            Trait("city"),
            Trait("state"),
            Trait("zipcode"),
            Trait("website"),
            Trait("occupancy"),
            Trait("capacity")
        ]

    @property
    def traits(self):
        return [
            Trait( "name", self.name ),
            Trait( "address", self.address ),
            Trait( "city", self.city ),
            Trait( "state", self.state ),
            Trait( "zipcode", self.zipCode ),
            Trait( "website", self.website ),
            Trait( "occupancy", self.current_occupancy ),
            Trait( "capacity", self.maximum_capacity )
        ]


    @property
    def serialize(self):

        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zipCode': self.zipCode,
            'website': self.website,
            'current_occupancy': self.current_occupancy,
            'maximum_capacity': self.maximum_capacity
        }


class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key = True)
    puppy_id = Column(Integer, ForeignKey('puppy.id'))
    picture = Column(String)
    description = Column(String)
    specialNeeds = Column(String)
    name = Column(String(250), nullable = False)
    gender = Column(String(6))
    dateOfBirth = Column(Date)
    weight = Column(String(6))


    @staticmethod
    def defaultTraits():
        return [
            Trait( "picture"),
            Trait( "name"),
            Trait( "weight"),
            Trait( "gender", 'male', "select", ['male','female'] ),
            Trait( "birthday", '2015-11-17', "date" ),
            Trait( "description", "", "textarea" ),
            Trait( "needs", "", "textarea" )
        ]


    @property
    def traits(self):
        return [
            Trait( "picture", self.picture, "image"),
            Trait( "name", self.name ),
            Trait( "weight", self.weight ),
            Trait( "gender", self.gender, "select", ['male','female'] ),
            Trait( "birthday", self.dateOfBirth, "date" ),
            Trait( "description", self.description, "textarea" ),
            Trait( "needs", self.specialNeeds, "textarea" )
        ]


    @property
    def serialize(self):
        return {
            'id': self.id,
            'puppy_id': self.puppy_id,
            'name': self.name,
            'picture': self.picture,
            'description': self.description,
            'specialNeeds': self.specialNeeds,
            'gender': self.gender,
            'dateOfBirth': str(self.dateOfBirth),
            'weight': self.weight
        }


class Puppy(Base):
    __tablename__ = "puppy"
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    profile = relationship("Profile", backref="puppy", uselist=False)
    id = Column(Integer, primary_key = True)
    adopters = relationship("Adopter",
                            secondary = association_table,
                            backref = "puppies")

    @staticmethod
    def defaultTraits():
        return [
            Trait( "id"),
            Trait( "shelter_id")
        ]


    @property
    def serialize(self):
        profileInfo = self.profile.serialize
        adoptersInfo = [a.serialize for a in self.adopters]

        # Returns object data in form that's easy to serialize.
        return {
            'id': self.id,
            'shelter_id': self.shelter_id,
            'profile': profileInfo,
            'adopters': adoptersInfo
        }

    @property
    def traits(self):
        profileTraits = self.profile.traits
        adoptersTraits = [a.traits for a in self.adopters]

        return [
            Trait( "id", self.id ),
            Trait( "shelter_id", self.shelter_id ),
        ]


class Adopter(Base):
    __tablename__ = "adopter"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)


    @staticmethod
    def defaultTraits():
        return [
            Trait( "name")
        ]

    @property
    def traits(self):
        return [
            Trait( "name", self.name )
        ]


    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
