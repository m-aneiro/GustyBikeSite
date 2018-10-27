$(document).ready(function() {
    $('#newSliderImage').change(function(event) {
        $("#sliderPreview").fadeOut('slow', function() {
            $(this).fadeIn('slow').attr('src', URL.createObjectURL(event.target.files[0]));
        })
    });

    $('#addNewSlider').on('click', function() {
        var form = $('#sliderForm');
        var data = new FormData();
        data.append('file', form[0]);

        $.ajax({
            url: '/admin/api/sliders/new',
            type: 'POST',
            data: data,
            cache: false,
            processData: false,
            contentType: false,
            success: function(response) {
                switch (response) {
                    case '0': //fail
                        alertify.error("Error uploading file, please make sure you are upload a valid image");
                        break;
                    case '1': //success
                        alertify.success("Image successfully added to the Homepage Slider!");
                        break;
                    case '2': //order not a number
                        alertify.error("Order submitted is not a number!");
                        break;

                }
            }
        });

        /*
        $.post('/admin/api/sliders/new', {'form': fileData, 'order': $('#newSliderOrder').val(), 'type': 'new_slider'}, function(response) {
            switch (response) {
                case '0': //fail
                    alertify.error("Error uploading file, please make sure you are upload a valid image");
                    break;
                case '1': //success
                    alertify.success("Image successfully added to the Homepage Slider!");
                    break;
                case '2': //order not a number
                    alertify.error("Order submitted is not a number!");
                    break;

            }
        }); */
    });
});