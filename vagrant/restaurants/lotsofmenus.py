from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

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


# Menu for Panda Garden
restaurant1 = session.query(Restaurant).filter(Restaurant.name == "Panda Garden").first()

menuItem3 = MenuItem(name="Gyoza", description="Japanese-style gyoza, in comparison with the Chinese-style jiaozi, features a rich garlic flavor,  light seasoning with salt and soy sauce, and a much thinner wrapper.",
                     price="$9.95", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     price="$6.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Thyme for that
restaurant1 = Restaurant(name="Thyme for That Vegetarian Cuisine ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     price="$2.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                     price="$5.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Honey Boba Shaved Snow", description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
                     price="$4.50", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     price="$6.95", course="Appetizer", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     price="$7.95", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$6.80", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Tony's Bistro
restaurant1 = Restaurant(name="Tony\'s Bistro ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     price="$13.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken and Rice", description="Chicken... and rice",
                     price="$4.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                     price="$6.95", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", course="Dessert", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     price="$7.95", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()


# Menu for Andala's
restaurant1 = Restaurant(name="Andala\'s")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     price="$9.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                     price="$7.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     price="$6.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     price="$6.75", course="Appetizer", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$7.00", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Auntie Ann's
restaurant1 = Restaurant(name="Auntie Ann\'s Diner' ")

session.add(restaurant1)
session.commit()

menuItem9 = MenuItem(name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy",
                     price="$8.99", course="Entree", restaurant=restaurant1)

session.add(menuItem9)
session.commit()


menuItem1 = MenuItem(name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     price="$2.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     price="$10.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Morels on toast (seasonal)", description="Wild morel mushrooms fried in butter, served on herbed toast slices",
                     price="$7.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     price="$8.95", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem10 = MenuItem(name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                      price="$1.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem10)
session.commit()


# Menu for Cocina Y Amor
restaurant1 = Restaurant(name="Cocina Y Amor ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
                     price="$5.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     price="$7.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


restaurant1 = Restaurant(name="State Bird Provisions")
session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                     price="$5.95", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit

menuItem1 = MenuItem(name="Guanciale Chawanmushi", description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",
                     price="$6.95", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem1 = MenuItem(name="Lemon Curd Ice Cream Sandwich", description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",
                     price="$4.25", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


print "added menu items!"
