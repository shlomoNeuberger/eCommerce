$username = $('#username')
$password = $('#password')
$firstName = $('#first_name')
$lastName = $('#last_name')
$email = $('#email')
$form = $("#login_from");
$username.valid = false
$password.valid = false

function valid(e, item, HelpTextElement, feild) {
    console.log(`e`, e)
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

$('#username').change((e) => {
    valid(e, $username, $("#usernameHelp"), "username");
})

$('#password').change((e) => {
    valid(e, $password, null);
})

$('#first_name').change((e) => {
    valid(e, $firstName, $("#firstHelpId"), "first name");
})
$('#last_name').change((e) => {
    valid(e, $lastName, $("#lastHelpId"), "last name");
})
$('#email').change((e) => {
    valid(e, $email, $("#emailHelpId"), "email adress");
})


$("#login_from").on('submit', (e) => {
    e.preventDefault();
    const items_count = $form[0].length

    if (!$username.valid) {
        return false;
    }

    if (!$password.valid) {
        return false;
    }

    $form.submit()
})