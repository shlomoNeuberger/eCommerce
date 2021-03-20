$logout = $('#logout');
$userbadge = $('#user_badge');
$logout.hide();
$logout.hovering = false;
$userbadge.hovering = false;

$(document).on({
    mouseenter: function (e) {
        const itemId = e.target.id
        switch (itemId) {
            case 'user_badge':
                $logout.show();
                $logout.hovering = true
                $userbadge.hovering = true
                break;
            case 'logout':
                $logout.hovering = true
                console.log('logout enter', $logout.hovering);
                $logout.show()
                break;
            default:
                console.log(e);
                break;
        }
    },

    mouseleave: function (e) {
        const itemId = e.target.id
        switch (itemId) {
            case 'user_badge':
                $userbadge.hovering = false
                $logout.hovering = false
                setTimeout(() => {
                    console.log('timeout 500', $logout.hovering);
                    if (!$userbadge.hovering && !$logout.hovering) {
                        $logout.hide()
                    }
                }, 100)
                break;
            case 'logout':
                console.log('logout leave', $logout.hovering);
                $logout.hide()
                $logout.hovering = false
                break;
            default:
                console.log(e);
                break;
        }

    }
}, '.hovers');



