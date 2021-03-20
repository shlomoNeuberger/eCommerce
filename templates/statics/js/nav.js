$logout = $('#logout');
$userbadge = $('#user_badge');
$badge_zone = $('#badge_zone');
$logout.hide();

$badge_zone.hover(
    () => {
        setTimeout(() => { $userbadge.hide(); $logout.show(); }, 150)
    },
    () => {
        setTimeout(() => { $userbadge.show(); $logout.hide(); }, 150)
    }

)

