$username = $('#username')
$password = $('#password')
$password_verify = $('#password_verify')
$firstName = $('#first_name')
$lastName = $('#last_name')
$email = $('#email')
$form = $("#register_btn");
$alert = $("#alert");
$alert.hide()

function valid(e, item, HelpTextElement, feild) {
    if (e.target.value === '') {
        item.addClass("is-invalid");
        item.removeClass("is-valid");
        if (HelpTextElement !== null) {
            HelpTextElement.old = HelpTextElement.html();
            HelpTextElement.html("Must be filled");
            HelpTextElement.addClass("text-danger");
        }
        item.valid = false;

    } else {
        item.removeClass("is-invalid");
        item.addClass("is-valid");
        if (HelpTextElement !== null) {
            HelpTextElement.html("Insert your " + feild);
            HelpTextElement.removeClass("text-danger");
        }
        item.valid = true;
    }
}

$('#username').on("change click", (e) => {
    valid(e, $username, $("#usernameHelp"), "username");
})

$('#password').on("change click", (e) => {
    valid(e, $password, null);
    $('#password_verify').val("")
    $('#password_verify').removeClass("is-valid");

})

$('#password_verify').on("change click", (e) => {
    console.log($('#password_verify').val());
    console.log($('#password').val());
    if ($('#password_verify').val() !== "" &&
        $('#password').val() === $('#password_verify').val()) {
        $('#password_verify').addClass("is-valid");
        $('#password_verify').removeClass("is-invalid");
        $password_verify.valid = true;
    }
    else {
        $('#password_verify').removeClass("is-valid");
        $('#password_verify').addClass("is-invalid");
        $password_verify.valid = false;
    }
})

$('#first_name').on("change click", (e) => {
    valid(e, $firstName, $("#firstHelpId"), "first name");
})
$('#last_name').on("change click", (e) => {
    valid(e, $lastName, $("#lastHelpId"), "last name");
})
$('#email').on("change click", (e) => {
    valid(e, $email, $("#emailHelpId"), "email adress");
})

