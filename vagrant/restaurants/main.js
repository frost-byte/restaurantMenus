$(document).ready(function () {

    function updateRestaurant(restaurant_name, restaurant_id){
        console.log("PUT /edit")
        var data = {
            name: restaurant_name,
            id: restaurant_id
        };

        $.ajax({
            url: '/edit',
            type: 'PUT',
            data: JSON.stringify(data),
            datatype: 'json',
            contentType: 'application/json',
            success: function(response){
                console.log("PUT /edit");
                console.log(response)
                window.location.href = "/restaurants";
            }
        });
    }

    // An Edit Button for a restaurant was clicked.
    $(document).on('click', '.edit-btn', function (event) {
        // Retrieve the Restaurant's id
        var data = {
            id: $(this).attr('data-restaurant-id'),
            name: $(this).attr('data-restaurant-name')
        };

        // Send a GET request to the Server to see the Restaurant's Edit Page
        $.ajax({
            url: '/edit',
            data: data,
            datatype: 'html',
            success: function (result, status, xhr) {
                //console.log(result)
                $(document.body).html(result);
                $('#editForm').submit( function (event){
                    var restaurant_name = $('#editRestaurant').val();
                    var restaurant_id = 
                        $('#editRestaurant').attr('data-restaurant-id');

                    updateRestaurant(restaurant_name, restaurant_id);
                });
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    // A Delete Button for a restaurant was clicked.
    $(document).on('click', '.delete-btn', function (event) {
        // Retrieve the Restaurant's id
        var data = {
            id: $(this).attr('data-restaurant-id'),
            name: $(this).attr('data-restaurant-name')
        };

        // Send a GET request to ask for delete confirmation
        $.ajax({
            url: '/confirm',
            type: 'GET',
            data: data,
            datatype: 'html',
            contentType: "application/json",
            success: function(result, status, xhr){
                console.log("confirm deletion GET /confirm");
                console.log(status)
                $(document.body).html(result)
            }
        });
    });

    // Send a DELETE request when a delete operation for a restaurant is confirmed.
    $(document).on('click', '.confirm-btn', function (event) {
        var data = {
            id: $(this).attr('data-restaurant-id'),
            name: $(this).attr('data-restaurant-name')
        };

        // Send a DELETE request to remove a restaurant
        $.ajax({
            url: '/delete',
            data: JSON.stringify(data),
            datatype: 'json',
            contentType: "application/json",
            type: 'DELETE',
            success: function (response) {
                console.log("DELETE /delete");
                console.log(response)
                window.location = "/restaurants";
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    // Return to the main page when a Delete operation is canceled.
    $(document).on('click', '.cancel-btn', function (event) {
        console.log("Redirecting to /restaurants");
        window.location.href = "/restaurants";
    });



    // The Create Button to add a new restaurant was clicked.
    // This Redirects to the \new url
    $(document).on('click', '.create-btn', function (event) {
        // Send a GET request to the Server to see the New Restaurant Page
        console.log("GET /new")
        $.ajax({
            url: '/new',
            type: 'GET',
            datatype:'html',
            success: function(response, status, xhr){
                console.log(response)
                $(document.body).html(response);
            }
        });
    });

    // Send a POST request to add a new Restaurant with the specified name.
    function newRestaurant(){
        console.log("POST /new")
        var restaurant_name = $('#makeRestaurant').val();

        var data = {
            name: restaurant_name
        };

        $.ajax({
            url: '/new',
            type: 'POST',
            data: JSON.stringify(data),
            datatype: 'json',
            contentType: "application/json",
            success: function(result, status, xhr){
                console.log("Redirecting to /restaurants");
                console.log(status)
                window.location = "/restaurants";
            }
        });
    }

    // Submit the Restaurant name in the makeRestaurant input.
    $(document).on('click', '#newRestaurant', newRestaurant);

    // Submit the name when the enter key is pressed and the makeRestaurant element
    // has focus.
/*    $(document).on('keypress', "#makeRestaurant", function (event) {
        var keycode = (event.keyCode ? event.keyCode : event.which);

        // If the enter key was pressed
        if (keycode == '13') {
            $('#newRestaurant').trigger('click')
        }
    });
*/
});