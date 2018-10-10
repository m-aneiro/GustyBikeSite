$(document).ready(function() {
    $('#completeLogin').on('click', function() {
        $.post('authenticate', {'username': $("#loginUsername").val(), 'password': $("#loginPassword").val()}, function(response) {
            switch (response) {
                case 0:
                    //not found
                    alertify.error("The username and password do not match.");
                    break;
                case 1:
                    //found
                    sessionStorage.setItem('UserID', "#userID");
                    window.location.reload(true);
                    break;
            }
            console.log(response);
        })
    })
})