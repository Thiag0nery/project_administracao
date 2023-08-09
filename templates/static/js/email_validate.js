$('#button-email').on('click', function(event) {
    event.preventDefault();

    email = $('#email-usuario').val()



    $.ajax({
        url: $('#button-email').data('url'),
        type: 'GET',
        data: {'email':email},
        success: function(response) {
            // Handle response here
        },
        error: function(error) {
            // Handle error here
        }
    });
});