$(document).ready(function() {
    $('#completeLogin').on('click', function() {
        $.post('authenticate', {'username': $("#loginUsername").val(), 'password': $("#loginPassword").val()}, function(response) {
           /* switch (response) {
                case 0:
                    //not found
                    break;
                case 1:
                    //found
                    break;
            } */
            console.log(response);
        })
    })
})