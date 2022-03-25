$(document).ready(function () {
    $('form').on('submit', function (event) {
        event.preventDefault();
        $.ajax({
            // Get the question
            data: {
                userQuestion: $('#userQuestion').val(),
            },
            type: 'GET',
            url: '/content'
            })
            // Display answer
            .done(function (data) {
                result = $("<section></section>");
                result.addClass("col-12 dialogue");
                result.html(data);
                result.appendTo("#all-responses");
            });
    });
});