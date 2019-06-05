$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
	let actions = $("table td:last-child").html();
	// Append table with add row form on add new button click
    $(".add-new").click(function(){
		$(this).attr("disabled", "disabled");
		let index = $("table tbody tr:last-child").index(),
            row = '<tr>' +
            '<td><input type="text" class="form-control" name="user_email" id="name"></td>' +
            '<td><input type="text" class="form-control" name="user_name" id="department"></td>' +
            '<td><input type="text" class="form-control" name="user_first_name" id="user_first_name"></td>' +
            '<td><input type="text" class="form-control" name="user_last_name" id="user_last_name"></td>' +
			'<td>' + actions + '</td>' +
        '</tr>';
    	$("table").append(row);
		$("table tbody tr").eq(index + 1).find(".add, .edit").toggle();
        $('[data-toggle="tooltip"]').tooltip();
    });
	// Add row on add button click
	$(document).on("click", ".add", function(){
		var empty = false;
		var input = $(this).parents("tr").find('input[type="text"]');
        input.each(function(){
			if(!$(this).val()){
				$(this).addClass("error");
				empty = true;
			} else{
                $(this).removeClass("error");
            }
		});
		$(this).parents("tr").find(".error").first().focus();
		if(!empty){
            let obj = {};
			input.each(function(){
			    obj[$(this).attr('name')] = $(this).val();
				//$(this).parent("td").html($(this).val());
			});
			$.ajax({
				type: 'POST',
				url: '/user_edit',
				data: obj,
				beforeSend: function(xhr){xhr.setRequestHeader('X-CSRFToken', csrf_token);},
				dataType: 'text',
				success: function (result) {
					var data = JSON.parse(result)
					if ($("input").next('p').length) $("input").nextAll('p').empty();
					for (var name in data.errors) {
						// object message error django
						var $input = $("input[name='"+ name +"']");
						$input.after("<p style='color: red'>" + data['errors'][name] + "</p>");
				  }
					if (data.successed === true) {
						input.each(function(){
							$(this).parent("td").html($(this).val());
						});
						window.location.reload();
					}
                }
			});
		}
    });
	// Edit row on edit button click
	$(document).on("click", ".edit", function(){
        $(this).parents("tr").find("td:not(:last-child)").each(function(){
			$(this).html('<input name="' + $(this).attr('data-model-name') + '" type="text" class="form-control" value="' + $(this).text() + '">');
		});
		$(this).parents("tr").find(".add, .edit").toggle();
		$(".add-new").attr("disabled", "disabled");
    });
	// Delete row on delete button click
	$(document).on("click", ".delete", function(){
		let obj = {};
		obj['user_id'] = $(this)[0].id;
		$.ajax({
			type: 'POST',
			url: '/del_user',
			data: obj,
			beforeSend: function(xhr){xhr.setRequestHeader('X-CSRFToken', csrf_token);},
			dataType: 'text',
			success: function (result) {
				window.location.reload();
			}
		});
        $(this).parents("tr").remove();
		$(".add-new").removeAttr("disabled");
    });
});