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
$('#btn-empresa-validade').on('click', function(event) {
    event.preventDefault();

    email = $('#email_empresa').val()



    $.ajax({
        url: $('#btn-empresa-validade').data('url'),
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