$('#id_minus_log_task').on('click', function () {
  if($('#id_main_card_log_task').hasClass('collapsed-card')) {
    $('#id_main_card_log_task').removeClass('collapsed-card');
  }
  else {
    $('#id_main_card_log_task').addClass('collapsed-card');
  }
});
