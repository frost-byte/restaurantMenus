import cgi
import os
import simplejson
from urlparse import urlparse, parse_qs
from mimetypes import types_map
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem
import res_views

curdir = os.curdir
sep = os.sep

engine = create_engine("postgresql+psycopg2:///restaurantmenus")
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



def listRestaurants():
    restaurants = session.query(Restaurant).all()
    return res_views.listView(restaurants)


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Render the Restaurant List View
            if "/restaurants" in self.path:
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                self.wfile.write(listRestaurants())
                return

            if "/edit" in self.path and '?' in self.path:
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                result = urlparse(self.path).query
                data = parse_qs(result)

                if 'id' in data and 'name' in data:
                    restaurant_id = data['id'][0]
                    restaurant_name = data['name'][0]

                    self.wfile.write(
                        res_views.editView(restaurant_id, restaurant_name))
                    return


            if "/delete" in self.path:
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                result = urlparse(self.path).query
                data = parse_qs(result)

                if 'id' in data and 'name' in data:
                    restaurant_id = data['id'][0]
                    restaurant_name = data['name'][0]

                    self.wfile.write(
                        res_views.confirmDeleteView(restaurant_id, restaurant_name))
                    return


            # Confrim that the user wants to DELETE a restaurant
            if "/confirm" in self.path:
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                result = urlparse(self.path).query
                data = parse_qs(result)

                if 'id' in data and 'name' in data:
                    restaurant_id = data['id'][0]
                    restaurant_name = data['name'][0]

                    self.wfile.write(
                        res_views.confirmDeleteView(restaurant_id, restaurant_name))
                    return

            # Render the New Restaurant View
            if self.path.endswith("/new"):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                self.wfile.write(res_views.newView())
                return

            fname,ext = os.path.splitext(self.path)
            if ext in (".js",".html", ".css"):
#                with open(os.path.join(curdir,self.path)) as f:
                f = open(curdir+os.sep+self.path)
                self.send_response(200)
                self.send_header('Content-type', types_map[ext])
                self.end_headers()
                self.wfile.write(f.read())
                return

            if self.path.endswith("/favicon.ico"):
                return

        except IOError:
            self.send_error(404, "File not found %s" % self.path)

    def do_POST(self):
        try:
            # Render the Restaurant Edit View, given it's name and id.
            '''if self.path.endswith("/edit"):
                self.send_response(200)
                self.end_headers()

                length = int(self.headers['content-length'])
                data = self.rfile.read(length)

                if self.headers['Content-type'] == 'application/json':
                    data = simplejson.loads(data)
                    restaurant_id = data['id']
                    restaurant_name = data['name']


                self.wfile.write(
                    res_views.editView(restaurant_id, restaurant_name))

                return'''
            if self.path.endswith("/new"):
                self.send_response(200)
                self.end_headers()

                length = int(self.headers['content-length'])
                data = self.rfile.read(length)

                if self.headers['Content-type'] == 'application/json':
                    data = simplejson.loads(data)
                    print "do_Post: name = " + data['name']

                    restaurant = Restaurant(name=data['name'])
                    session.add(restaurant)
                    session.commit()
                    self.wfile.write(restaurant.name)

                return
        except:
            pass


    def do_DELETE(self):
        try:
            if self.path.endswith("/delete"):
                self.send_response(200)
                self.end_headers()

                length = int(self.headers['content-length'])
                data = self.rfile.read(length)

                if self.headers['Content-type'] == 'application/json':
                    data = simplejson.loads(data)
                    id = data['id']

                    menu_items = session.query(MenuItem).filter(
                        MenuItem.restaurant_id == id).all()

                    for m in menu_items:
                        print m.name
                        session.delete(m)
                        session.commit()

                    restaurant = session.query(Restaurant).filter(
                        Restaurant.id == id).one()

                    session.delete(restaurant)
                    session.commit()
                    self.wfile.write(restaurant.name)

                return
        except:
            pass


    def do_PUT(self):
        try:
            if self.path.endswith("/edit"):
                self.send_response(200)
                self.end_headers()

                length = int(self.headers['content-length'])
                data = self.rfile.read(length)

                if self.headers['Content-type'] == 'application/json':
                    data = simplejson.loads(data)
                    id = data['id']
                    name = data['name']
                    restaurant = session.query(Restaurant).filter(
                        Restaurant.id == id).one()
                    restaurant.name = name
                    session.add(restaurant)
                    session.commit()
                    self.wfile.write(restaurant.name)

                return
        except:
            pass

def main():
    try:

        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "Web server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()

if __name__ == '__main__':
    main()
