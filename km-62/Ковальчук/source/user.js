$("button[name='btn_delete_user']").click(function() {

    var data = { email : $(this).data('email')}

    $.ajax({
      type: 'POST',
      url: "/delete_user",
      data: data,
      dataType: "text",
      success: function(resultData) {
          location.reload();
      }
});
});


$("button[name='btn_edit_user']").click(function() {

    window.location = "edit_user?email="+$(this).data('email');

});


$("button[name='btn_new_user']").click(function() {

    window.location = "new_user";

});

