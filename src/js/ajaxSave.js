$('[id^=savePlan]').click(function() {
  var btn = $(this);
    btn.attr('disabled', true);
    val = btn.attr('value');
  var hostUrl= './cgi_savePlan.cgi';
  var param1 = $('#userId').val();
  var param2 = $('#date').val();
  var param3 = $('#companion').val();
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
  var param19 = $('#which1').val() || "None";
  var param20 = $('#which2').val() || "None";
  var param21 = $('#which3').val() || "None";
  var param22 = $('#which4').val() || "None";
  var param23 = $('#which5').val() || "None";
  var param24 = $('#which6').val() || "None";
  var param25 = $('#amtItem1').val() || "None";
  var param26 = $('#amtItem2').val() || "None";
  var param27 = $('#amtItem3').val() || "None";
  var param28 = $('#amtItem4').val() || "None";
  var param29 = $('#amtItem5').val() || "None";
  var param30 = $('#amtItem6').val() || "None";
  var param31 = $('#seed').val() || "None";
  var param32 = $('#score1').val() || "None";
  var param33 = $('#score2').val() || "None";
  var param34 = $('#score3').val() || "None";
  var param35 = $('#score4').val() || "None";
  var param36 = $('#score5').val() || "None";
  var param37 = $('#score6').val() || "None";
  var param38 = $('#data_iter').val() || "None";
  var param39 = $('#sim_iter').val() || "None";
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
        venue3:param16, venue4:param17, venue5:param18, 
        type1:param19, type2:param20, type3:param21, 
        type4:param22, type5:param23, type6:param24, 
        amount1:param25, amount2:param26, amount3:param27, 
        amount4:param28, amount5:param29, amount6:param30, 
        seed:param31, score1:param32, score2:param33, 
        score3:param34, score4:param35, score5:param36, 
        score6:param37, data_iter:param38, sim_iter:param39},
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