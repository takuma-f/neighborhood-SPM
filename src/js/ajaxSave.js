$('#saveRating').click(function() {
  var btn = $(this);
    btn.attr('disabled', true);
  var hostUrl= './cgi_savePlan.cgi';
  var param1 = $('#userId').val();
  var param2 = $('#date').val();
  var param3 = $('#companion').val();
  var param4 = $('#budget').val();
  var param5 = $('#seed').val() || "None";
  var param6 = $('#type1').val() || "None";
  var param7 = $('#type2').val() || "None";
  var param8 = $('#type3').val() || "None";
  var param9 = $('#type4').val() || "None";
  var param10 = $('#type5').val() || "None";
  var param11 = $('#type6').val() || "None";
  var param12 = $('#amount1').val() || "None";
  var param13 = $('#amount2').val() || "None";
  var param14 = $('#amount3').val() || "None";
  var param15 = $('#amount4').val() || "None";
  var param16 = $('#amount5').val() || "None";
  var param17 = $('#amount6').val() || "None";
  var param18 = $('#score1').val() || "None";
  var param19 = $('#score2').val() || "None";
  var param20 = $('#score3').val() || "None";
  var param21 = $('#score4').val() || "None";
  var param22 = $('#score5').val() || "None";
  var param23 = $('#score6').val() || "None";
  var param24 = $('#pattern1').val() || "None";
  var param25 = $('#pattern2').val() || "None";
  var param26 = $('#pattern3').val() || "None";
  var param27 = $('#pattern4').val() || "None";
  var param28 = $('#pattern5').val() || "None";
  var param29 = $('#pattern6').val() || "None";
  var param30 = $('input:radio[name="rate1"]:checked').val() || "None";
  var param31 = $('input:radio[name="rate2"]:checked').val() || "None";
  var param32 = $('input:radio[name="rate3"]:checked').val() || "None";
  var param33 = $('input:radio[name="rate4"]:checked').val() || "None";
  var param34 = $('input:radio[name="rate5"]:checked').val() || "None";
  var param35 = $('input:radio[name="rate6"]:checked').val() || "None";
  if ((param18 != "None") && (param19 != "None") && (param20 != "None") && (param21 != "None") && (param22 != "None")) {
    $.ajax({
      url: hostUrl,
      type:'POST',
      scriptCharset: 'utf-8',
      data: {userId:param1, date:param2, companion:param3, budget:param4, seed:param5, type1:param6, type2:param7, type3:param8, type4:param9, type5:param10, type6:param11, amount1:param12, amount2:param13, amount3:param14, amount4:param15, amount5:param16, amount6:param17, score1:param18, score2:param19, score3:param20, score4:param21, score5:param22, score6:param23, pattern1:param24, pattern2:param25, pattern3:param26, pattern4:param27, pattern5:param28, pattern6:param29, rate1:param30, rate2:param31, rate3:param32, rate4:param33, rate5:param34, rate6:param35},
        // 最後のカンマ忘れやすいので注意すること
      dataType: 'HTML',
      timeout: 100000,
      success: function(res) {
        $('#response').html('<span id="alert">保存完了.</span>');
        $('#alert').fadeOut(1500).queue(function() {
          this.remove();
        });
      },
      error: function(XMLHttpRequest, textStatus, errorThrown) {
        $('#response').html('<span id="alert">予期せぬエラーが発生しました.</span>');
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