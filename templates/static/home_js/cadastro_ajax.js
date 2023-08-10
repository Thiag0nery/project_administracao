const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;
$('#form-cadastro').submit(function(event) {
    event.preventDefault();

    const form = $(this);

    $.ajax({
        url: $('#btn-cadastro').data('url'),
        type: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
        },
        data: form.serialize(),

        success: function(response) {

        },
        error: function(error) {

        }
    });
});