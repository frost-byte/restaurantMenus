from flask import (
    Flask,
    render_template,
    url_for,
    request,
    redirect,
    flash,
    jsonify
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem


engine = create_engine("postgresql+psycopg2:///restaurantmenus")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET','POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(
            name = request.form['name'],
            restaurant_id = restaurant_id
        )
        session.add(newItem)
        session.commit()
        flash("New menu item created!")
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))

    else:
        return render_template('newmenuitem.html', restaurant_id = restaurant_id)


@app.route(
    '/restaurants/<int:restaurant_id>/<int:menu_id>/edit/',
    methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):

    editItem = session.query(MenuItem).filter_by(id = menu_id).one()

    if request.method == 'POST':
        editItem.name = request.form['name']
        session.add(editItem)
        session.commit()

        flash("Item edited!")
        return redirect(
            url_for(
                'restaurantMenu',
                restaurant_id = restaurant_id
            )
        )

    else:
        return render_template(
            'editmenuitem.html',
            restaurant_id = restaurant_id,
            item = editItem
        )


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/',
           methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    deleteItem = session.query(MenuItem).filter_by(id = menu_id).one()

    if request.method == 'POST':
        session.delete(deleteItem)
        session.commit()

        flash("Item deleted!")
        return redirect(
            url_for(
                'restaurantMenu',
                restaurant_id = restaurant_id
            )
        )

    else:
        return render_template(
            'deletemenuitem.html',
            i = deleteItem
        )


@app.route('/')
@app.route('/restaurants')
def restaurantsList():
    restaurants = session.query(Restaurant).all()

    return render_template('restaurants.html', restaurants = restaurants)


@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):

    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)

    return render_template('menu.html', restaurant = restaurant, items = items)


# An API endpoint to retrieve all Menu Item objects for a restaurant in JSON format
@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id).all()

    return jsonify(MenuItems=[i.serialize for i in items])


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def restaurantMenuItemJSON(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(id = menu_id).one()

    return jsonify(MenuItem=item.serialize)

if __name__ == "__main__":
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = "0.0.0.0", port = 5000)