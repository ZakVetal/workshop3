$("button[name='btn_delete_assignment']").click(function() {

    var data = { assignment_id : $(this).data('assignment_id')}

    $.ajax({
      type: 'POST',
      url: "/delete_assignment",
      data: data,
      dataType: "text",
      success: function(resultData) {
          location.reload();
      }
});
});


$("button[name='btn_edit_assignment']").click(function() {

    window.location = "edit_assignment?assignment_id="+$(this).data('assignment_id');

});


$("button[name='btn_new_assignment']").click(function() {

    window.location = "new_assignment";

});

