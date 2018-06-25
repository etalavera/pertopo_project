$('#id_save_form_add_task').on('click', function () {
  debugger;
  var data = $('#id_form_add_task').find('input').serialize();
  data = data + '&project=' + PROJECT_ID;
  console.log("data serilize from save add task button");
  console.log(data);

  $.ajax({
    method: 'POST',
    url: '/apiFormularios/save_add_task',
    data: data,
    success: function (response) {
      console.log("Respuesta de save_add_task");
      console.log(response);
      if (response.status == "true" || response.status == true) {
        fillLogbookTable();
        $('#id_close_add_task').click();
      }
    },
    error: function (x, t, m) {
      console.log("Error: save_add_task");
      console.log(x);
    }
  })
});
