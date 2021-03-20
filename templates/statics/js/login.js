$username = $('#username')
$password = $('#password')
$form = $("#login_from");
$username.valid = false
$password.valid = false

function valid(e, item, HelpTextElement) {
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
            HelpTextElement.html("Insert your username");
            HelpTextElement.removeClass("text-danger");
        }
        item.valid = true;
    }
}

$('#username').change((e) => {
    valid(e, $username, $("#usernameHelp"));
})
$('#password').change((e) => {
    valid(e, $password, null);
})

$("#login_btn").on('submit', (e) => {
    e.preventDefault();
    const items_count = $form[0].length

    if (!$username.valid) {
        return false;
    }

    if (!$password.valid) {
        return false;
    }

    e.currentTarget.submit();
})