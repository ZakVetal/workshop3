$('#attendance_form').submit(function (e) {
    e.preventDefault();
    $.ajax({
        type: $(this).attr('method'),
        url: $(this).attr('action'),
        data: $(this).serialize(),
        success: function (result) {
            if (result.error) {
                alert(result.error);
                window.location.reload();
            }
            if (result.success) {
                alert('User is added!');
            }
        }
    })
});

function del_user_from_event(user_id, event_id) {
    $.ajax({
        type: 'POST',
        url: '/del_user_from_event',
        data: {'user_id': user_id, 'event_id': event_id},
        success: function (result) {
            window.location.reload();
        }
    })
}