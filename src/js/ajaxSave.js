$('[id^=savePlan]').click(function() {
  var btn = $(this);
    btn.attr('disabled', true);
    val = btn.attr('value');
  var hostUrl= './cgi_savePlan.cgi';
  var param1 = $('#userId').val();
  var param2 = $('#date').val();
  var param3 = $('input:radio[name="companion"]:checked').val();
  var param4 = $('#budget').val();
  var param5 = $('#venue'+val+'1').val() || "None";
  var param6 = $('#venue'+val+'2').val() || "None";
  var param7 = $('#venue'+val+'3').val() || "None";
  var param8 = $('#venue'+val+'4').val() || "None";
  var param9 = $('#venue'+val+'5').val() || "None";
  if (param5 != "None") {
    $.ajax({
      url: hostUrl,
      type:'POST',
      scriptCharset: 'utf-8',
      data: {userId:param1, date:param2, companion:param3, budget:param4, venue1:param5, venue2:param6, venue3:param7, venue4:param8, venue5:param9, order:val},
      dataType: 'HTML',
      timeout: 100000,
      success: function(res) {
        $('#response'+val).html('<span id="alert">保存完了.</span>');
        $('#alert').fadeOut(1500).queue(function() {
          this.remove();
        });
      },
      error: function(XMLHttpRequest, textStatus, errorThrown) {
        $('#response'+val).html('<span id="alert">予期せぬエラーが発生しました.</span>');
        $('#alert').fadeOut(1500).queue(function() {
          this.remove();
        });
      },
      complete: function() {
        btn.attr("disabled", false);
      }
    });
  } else {
    btn.attr("disabled", false);
  }
});