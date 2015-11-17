from flask import (
    render_template,
    url_for,
    request,
    redirect,
    flash,
    jsonify
)

from datetime import datetime
from random import randint
import random

from database import session, Base
from models import (
    Puppy,
    Profile,
    Shelter,
    Adopter
)

from populator import puppy_images
from urls import Urls
from . import app


@app.context_processor
def makeurls_processor():
    def makeUrls(suffix, key=0):
        return Urls(suffix, key)
    return dict(makeUrls=makeUrls)


@app.context_processor
def hasattr_processor():
    return dict(hasattr=hasattr)


# Adopter Routes
@app.route('/adopter/<int:key>/')
def viewAdopter(key):

    vAdopter = session.query(Adopter).filter_by(id = key).one()

    return render_template(
        'view.html',
        viewType="adopter",
        key = key,
        traits = vAdopter.traits,
        name = vAdopter.name
    )


@app.route('/adopter/new', methods=['GET','POST'])
@app.route('/adopter/new/', methods=['GET','POST'])
def newAdopter():
    if request.method == 'POST':
        newAdopter = Adopter(
            name = request.form['name']
        )

        session.add(newAdopter)
        session.commit()

        flash("New Adopter created!")
        return redirect( url_for("viewAdopter", key = newAdopter.id) )

    else:
        return render_template(
            'new.html',
            viewType = "adopter",
            traits = Adopter.defaultTraits()
        )


@app.route('/adopter/<int:key>/edit/', methods=['GET','POST'])
def editAdopter(key):
    print "editAdopter: id = %s" % key
    edAdopter = session.query(Adopter).filter_by(id = key).one()

    if request.method == 'POST':
        edAdopter.name = request.form['name']

        session.add(edAdopter)
        session.commit()

        return redirect( url_for('viewAdopter', key = edAdopter.id) )

    else:
        return render_template(
            'edit.html',
            viewType = "adopter",
            key = key,
            traits = edAdopter.traits
        )


@app.route('/adopter/<int:key>/delete/', methods=['GET','POST'])
def deleteAdopter(key):
    delAdopter = session.query(Adopter).filter_by(id = key).one()

    if request.method == 'POST':
        session.delete(delAdopter)
        session.commit()

        return redirect( url_for('listAdopter') )

    else:
        return render_template(
            'delete.html',
            viewType = "adopter",
            key = key,
            name = delAdopter.name
        )


@app.route('/adopter/')
@app.route('/adopter')
def listAdopter():
    adopters = session.query(Adopter).all()
    return render_template(
        'list.html',
        viewType = "adopter",
        otherViews = ['shelter','puppy','profile'],
        objects = adopters)


# Shelter Routes
@app.route('/shelter/<int:key>/')
def viewShelter(key):
    shelter = session.query(Shelter).filter_by(id = key).one()

    return render_template(
        'view.html',
        viewType = "shelter",
        key = key,
        name = shelter.name,
        traits = shelter.traits
    )


@app.route('/shelter/new',  methods=['GET','POST'])
@app.route('/shelter/new/', methods=['GET','POST'])
def newShelter():
    if request.method == 'POST':
        newShelter = Shelter(
            name = request.form['name'],
            address = request.form['address'],
            city = request.form['city'],
            state = request.form['state'],
            zipCode = request.form['zipcode'],
            website = request.form['website'],
            current_occupancy = request.form['occupancy'],
            maximum_capacity = request.form['capacity']
        )

        session.add(newShelter)
        session.commit()

        flash("New Shelter created!")
        return redirect(url_for('viewShelter', key = newShelter.id))

    else:
        return render_template(
            'new.html',
            viewType = "shelter",
            traits = Shelter.defaultTraits()
        )


# Edit a Shelter
@app.route('/shelter/<int:key>/edit/',
          methods=['GET','POST'])
def editShelter(key):
    editShelter = session.query(Shelter).filter_by(id = key).one()

    if request.method == 'POST':

        editShelter.name = request.form['name']
        editShelter.address = request.form['address']
        editShelter.city = request.form['city']
        editShelter.state = request.form['state']
        editShelter.zipCode = request.form['zipcode']
        editShelter.website = request.form['website']
        editShelter.current_occupancy = request.form['occupancy']
        editShelter.maximum_capacity = request.form['capacity']
        print editShelter.serialize
        session.add(editShelter)
        session.commit()

        flash("Shelter edited!")
        return redirect(url_for('viewShelter', key = key))

    else:
        return render_template(
            'edit.html',
            viewType = 'shelter',
            key = key,
            traits = editShelter.traits
        )


@app.route('/shelter/<int:key>/delete/',
           methods=['GET','POST'])
def deleteShelter(key):
    deleteShelter = session.query(Shelter).filter_by(id = key).one()

    if request.method == 'POST':
        session.delete(deleteShelter)
        session.commit()

        flash("Shelter deleted!")
        return redirect(url_for('listShelter'))
    else:
        return render_template(
            'delete.html',
            viewType = "shelter",
            key = key,
            name = deleteShelter.name
        )


# List all Shelters
@app.route('/shelter/')
@app.route('/shelter')
def listShelter():
    shelters = session.query(Shelter).all()
    return render_template(
        'list.html',
        viewType = "shelter",
        otherViews = ['adopter','profile','puppy'],
        objects = shelters
    )


# Profile Routes
# View a Profile
@app.route('/profile/<int:key>/')
def viewProfile(key):

    profile = session.query(Profile).filter_by(puppy_id = key).one()

    return render_template(
        'view.html',
        viewType = "profile",
        key = key,
        name = profile.name,
        traits = profile.traits
    )


# Create a Profile
@app.route('/profile/new',  methods=['GET','POST'])
@app.route('/profile/new/', methods=['GET','POST'])
def newProfile():
    if request.method == 'POST':
        newProfile = Profile(
            name = request.form['name'],
            weight = request.form['weight'],
            gender = request.form['gender'],
            picture = random.choice(puppy_images),
            dateOfBirth = datetime.strptime(request.form['birthday'], "%Y-%m-%d"),
            description = request.form['description'],
            specialNeeds = request.form['needs']
        )

        session.add(newProfile)

        new_puppy = Puppy(
            shelter_id = randint(1,5),
            profile = newProfile)

        session.add(new_puppy)
        session.commit()

        flash("New puppy and profile created!")
        return redirect(url_for('viewProfile', key = newProfile.id))

    else:
        return render_template(
            'new.html',
            viewType = "profile",
            traits = Profile.defaultTraits()
        )


# Edit a Profile
@app.route(
    '/profile/<int:key>/edit/',
    methods=['GET','POST'])
def editProfile(key):

    editProfile = session.query(Profile).filter_by(id = key).one()

    if request.method == 'POST':
        editProfile.name = request.form['name']
        editProfile.weight = request.form['weight']
        editProfile.gender = request.form['gender']
        editProfile.dateOfBirth = datetime.strptime(request.form['birthday'], "%Y-%m-%d")
        editProfile.description = request.form['description']
        editProfile.specialNeeds = request.form['needs']

        session.add(editProfile)
        session.commit()

        flash("Profile edited!")
        return redirect( url_for('viewProfile', key = key) )

    else:
        return render_template(
            'edit.html',
            viewType = 'profile',
            key = key,
            traits = editProfile.traits
        )

# Delete a Profile
@app.route('/profile/<int:key>/delete/',
           methods=['GET','POST'])
def deleteProfile(key):
    deleteProfile = session.query(Profile).filter_by(puppy_id = key).one()
    deletePuppy = session.query(Puppy).filter_by(id = deleteProfile.puppy_id).one()

    if request.method == 'POST':
        session.delete(deleteProfile)
        session.commit()

        session.delete(deletePuppy)
        session.commit()
        flash("Profile deleted!")
        return redirect( url_for('listProfile') )

    else:
        return render_template(
            'delete.html',
            viewType = "profile",
            key = key,
            name = deleteProfile.name
        )


# List all Profiles
@app.route('/profile/')
@app.route('/profile')
def listProfile():
    profiles = session.query(Profile).all()

    return render_template(
        'list.html',
        viewType = 'profile',
        otherViews = ['shelter','adopter','puppy'],
        objects = profiles
    )


# An API endpoint to a Profile in JSON format
@app.route('/profile/<int:key>/JSON')
def profileJSON(key):
    profile = session.query(Profile).filter_by(puppy_id = key).one()

    return jsonify(Profile=profile.serialize)



# Puppy Routes
# View a Puppy
@app.route('/puppy/<int:key>/')
def viewPuppy(key):

    puppy = session.query(Puppy).filter_by(id = key).one()
    print "viewPuppy: key = {0} puppy = {1}".format(key, puppy)

    return render_template(
        'view.html',
        viewType = "puppy",
        key = key,
        name = puppy.id,
        traits = puppy.traits
    )


# Edit a Puppy
@app.route('/puppy/<int:key>/edit/', methods=['GET','POST'])
def editPuppy(key):

    puppy = session.query(Puppy).filter_by(id = key).one()

    if request.method == 'POST':
        print "editPuppy.POST"
    else:
        return render_template(
            'edit.html',
            key = key,
            viewType = "puppy",
            traits = puppy.traits
        )


    # Delete a Profile
@app.route('/puppy/<int:key>/delete/',
           methods=['GET','POST'])
def deletePuppy(key):
    deleteProfile = session.query(Profile).filter_by(puppy_id = key).one()
    deletePuppy = session.query(Puppy).filter_by(id = key).one()

    if request.method == 'POST':
        session.delete(deleteProfile)
        session.commit()

        session.delete(deletePuppy)
        session.commit()
        flash("Puppy and Profile deleted!")
        return redirect( url_for('listPuppy') )

    else:
        return render_template(
            'delete.html',
            viewType = "profile",
            key = key,
            name = deleteProfile.name
        )


# Create a Puppy
@app.route('/puppy/new', methods=['GET','POST'])
@app.route('/puppy/new/', methods=['GET','POST'])
def newPuppy():

    if request.method == 'POST':
        newProfile = Profile(
            name = request.form['pupname'],
            weight = request.form['weight'],
            gender = request.form['gender'],
            picture = random.choice(puppy_images),
            dateOfBirth = datetime.strptime(request.form['birthday'], "%Y-%m-%d"),
            description = request.form['description'],
            specialNeeds = request.form['needs']
        )

        session.add(newProfile)

        new_puppy = Puppy(
            shelter_id = randint(1,5),
            profile = newProfile)

        session.add(new_puppy)
        session.commit()

        flash("New puppy created!")
        return redirect(url_for('viewPuppy', key = newPuppy.id))

    else:
        return render_template(
            'new.html',
            viewType = "puppy",
            traits = Puppy.defaultTraits()
        )


# List all Puppies
@app.route('/')
@app.route('/puppies')
def listPuppy():
    puppies = session.query(Puppy).all()

    return render_template(
        'list.html',
        viewType = "puppy",
        otherViews = ['shelter','profile','adopter'],
        objects = puppies)


# Endpoint to retrieve a puppy and it's components in JSON format.
@app.route('/puppies/<int:key>/JSON ')
def puppyJSON(key):
    puppy = session.query(Puppy).filter_by(id = key).one()

    return jsonify(Puppy=puppy.serialize)