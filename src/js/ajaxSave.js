$('[id^=savePlan]').click(function() {
  var btn = $(this);
    btn.attr('disabled', true);
    val = btn.attr('value');
  var hostUrl= './cgi_savePlan.cgi';
  var param1 = $('#userId').val();
  var param2 = $('#date').val();
  var param3 = $('input:radio[name="companion"]:checked').val();
  var param4 = $('#budget').val();
  var param5 = $('#pattern1').val() || "None";
  var param6 = $('#pattern2').val() || "None";
  var param7 = $('#pattern3').val() || "None";
  var param8 = $('#pattern4').val() || "None";
  var param9 = $('#pattern5').val() || "None";
  var param10 = $('#pattern6').val() || "None";
  var param11 = $('#ordPlan'+val).val() || "None";
  var param12 = $('#amtItem'+val).val() || "None";
  var param13 = $('#which'+val).val() || "None";
  var param14 = $('#venue'+val+'1').val() || "None";
  var param15 = $('#venue'+val+'2').val() || "None";
  var param16 = $('#venue'+val+'3').val() || "None";
  var param17 = $('#venue'+val+'4').val() || "None";
  var param18 = $('#venue'+val+'5').val() || "None";
  if (param14 != "None") {
    $.ajax({
      url: hostUrl,
      type:'POST',
      scriptCharset: 'utf-8',
      data: {userId:param1, date:param2, companion:param3, 
        budget:param4, pattern1:param5, pattern2:param6, 
        pattern3:param7, pattern4:param8, pattern5:param9, 
        pattern6:param10, order:param11, amount:param12, 
        which:param13, venue1:param14, venue2:param15, 
        venue3:param16, venue4:param17, venue5:param18},
        // 最後のカンマ忘れやすいので注意すること
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