$("button[name='btn_delete_worker']").click(function() {

    var data = { worker_id : $(this).data('worker_id')}

    $.ajax({
      type: 'POST',
      url: "/delete_worker",
      data: data,
      dataType: "text",
      success: function(resultData) {
          location.reload();
      }
});
});


$("button[name='btn_edit_worker']").click(function() {

    window.location = "edit_worker?worker_id="+$(this).data('worker_id');

});


$("button[name='btn_new_worker']").click(function() {

    window.location = "new_worker";

});

