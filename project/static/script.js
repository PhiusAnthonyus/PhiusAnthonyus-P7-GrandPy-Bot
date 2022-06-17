$(document).ready(function () {
    // Script pour les boîtes de dialogue (content.html)
    $('form').on('submit', function (event) {
        event.preventDefault();
        $.ajax({
            // boîte question
            data: {
                userQuestion: $('#userQuestion').val(),
            },
            type: 'GET',
            url: '/content'
            })
            // boîte réponse
            .done(function (data) {
                result = $("<section></section>");
                result.addClass("col-12 dialogue");
                result.html(data);
                result.appendTo("#all-responses");
            });
    });
});