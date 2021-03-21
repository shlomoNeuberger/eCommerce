$("form .login-form").one(function (e) {
    e.preventDefault();
    console.log(e.target)
    //TODO: Check if that was the best correctly

    $(this).submit();
});