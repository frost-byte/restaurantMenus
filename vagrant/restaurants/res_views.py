stylesheets ='''
        <link rel='stylesheet' href='https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css'>
        <link rel='stylesheet' href='https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css'>
        <link rel='stylesheet' href='style.css'>'''

scripts ='''
        <script src='http://code.jquery.com/jquery-1.10.1.min.js'></script>
        <script src='main.js' type='text/javascript' charset='utf-8'></script>
        <script src='https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js'>
        </script>'''

head ='''<head>{0}{1}
    </head>'''

head = head.format(stylesheets, scripts)
page ='''<html>
    {0}
    <body>{1}
    </body>
</html>'''


confirmDeleteTemplate ='''
        <div class="container" id="restaurant-confirm-delete-container">
            <div class="col-md-5">
                <div class="panel panel-primary">
                    <div class="panel-heading">Delete this Restaurant?</div>
                    <div class="input-group">
                        <span class="input-group-btn">
                            <button
                                class="btn btn-danger confirm-btn"
                                data-restaurant-id="{0}"
                                data-restaurant-name="{1}"
                                type="button">Delete
                            </button>
                        </span>
                        <span class="input-group-btn">
                            <button
                                class="btn btm-primary cancel-btn"
                                type="button">Cancel
                            </button>
                        </span>
                    </div><!-- /Input Group -->
                </div><!-- /Panel -->
            </div><!-- /Column -->
        </div><!-- /Restaurant Confirm Delete Container -->'''


def confirmDeleteView(restaurant_id, restaurant_name):
    output = confirmDeleteTemplate.format(restaurant_id, restaurant_name)
    print output
    return output


tableRow ='''
                        <tr class="restaurant-item">
                            <td>
                                {0}
                            </td>
                            <td>
                                <button class='btn btn-primary edit-btn'
                                    type='button'
                                    data-restaurant-id='{1}'
                                    data-restaurant-name='{0}'>
                                    Edit
                                </button>
                            </td>
                            <td>
                                <button class='btn btn-danger delete-btn'
                                    type='button'
                                    data-restaurant-id='{1}'
                                    data-restaurant-name='{0}'>
                                    Delete
                                </button>
                            </td>
                        </tr>'''

restaurantsListTemplate ='''
        <div class="container" id="restaurant-list-container">
            <div class="col-md-5">
                <div class="panel panel-primary">
                    <div class="panel-heading">Restaurants</div>
                    <table class="restaurant-table">{0}{1}
                    </table><!-- /Restaurant List Table -->
                </div><!-- /Panel -->
            </div><!-- /Column -->
        </div><!-- /Restaurant List Container -->'''

createRestaurantRow = '''
                        <tr class="restaurant-create">
                            <td colspan='3'>
                                <button class='btn btn-success create-btn'
                                    type='button'>
                                    Create a Restaurant
                                </button>
                            </td>
                        </tr>'''


def listView(restaurants):
    # Store the Rendered View
    output = ""

    # Contents of the Rendered Table listing each Restaurant
    tableContents = ""

    # Add a Table row for each Restaurant that includes an edit and delete button
    for r in restaurants:
        tableContents += tableRow.format(r.name, r.id)

    # Combine the page head, body and table contents to render the complete view.
    output = restaurantsListTemplate.format(
        tableContents,
        createRestaurantRow
    )
    output = page.format(head, output)
    #print output
    return output


newRestaurantTemplate = '''
        <div class="row">
            <div class="col-md-4">
                <form>
                    <div class="form-group">
                        <label for="makeNewRestaurant">Make a New Restaurant</label>
                        <div class="input-group">
                            <input
                                type="text"
                                class="form-control"
                                id="makeRestaurant"
                                placeholder="Restaurant Name">
                            <span class="input-group-btn">
                                <button
                                    class="btn btn-success"
                                    id="newRestaurant"
                                    type="button">
                                    Create
                                </button>
                            </span>
                        </div>
                    </div> <!-- /Form Group -->
                </form>
            </div><!-- /Column -->
        </div><!-- /Row -->'''


def newView():
    # print newRestaurantTemplate
    return newRestaurantTemplate


editRestaurantTemplate = '''
        <form class="form-inline" id="editForm">
            <div class="form-group">
                <label for="editRestaurantForm">Edit Restaurant</label>
                <input
                    type="text"
                    class="form-control"
                    id="editRestaurant"
                    data-restaurant-id="{0}"
                    value="{1}">
            </div><!-- /Form Group -->
            <input type="submit" class="btn btn-success" value="Update">
        </form><!-- /Form -->
'''


def editView(restaurant_id, restaurant_name):
    result = editRestaurantTemplate.format(restaurant_id, restaurant_name)
    #print result
    return result

