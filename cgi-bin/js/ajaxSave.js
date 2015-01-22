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
  var param12 = $('#type7').val() || "None";
  var param13 = $('#type8').val() || "None";
  var param14 = $('#type9').val() || "None";
  var param15 = $('#type10').val() || "None";

  var param16 = $('#amount1').val() || "None";
  var param17 = $('#amount2').val() || "None";
  var param18 = $('#amount3').val() || "None";
  var param19 = $('#amount4').val() || "None";
  var param20 = $('#amount5').val() || "None";
  var param21 = $('#amount6').val() || "None";
  var param22 = $('#amount7').val() || "None";
  var param23 = $('#amount8').val() || "None";
  var param24 = $('#amount9').val() || "None";
  var param25 = $('#amount10').val() || "None";

  var param26 = $('#score1').val() || "None";
  var param27 = $('#score2').val() || "None";
  var param28 = $('#score3').val() || "None";
  var param29 = $('#score4').val() || "None";
  var param30 = $('#score5').val() || "None";
  var param31 = $('#score6').val() || "None";
  var param32 = $('#score7').val() || "None";
  var param33 = $('#score8').val() || "None";
  var param34 = $('#score9').val() || "None";
  var param35 = $('#score10').val() || "None";

  var param36 = $('#pattern1').val() || "None";
  var param37 = $('#pattern2').val() || "None";
  var param38 = $('#pattern3').val() || "None";
  var param39 = $('#pattern4').val() || "None";
  var param40 = $('#pattern5').val() || "None";
  var param41 = $('#pattern6').val() || "None";
  var param42 = $('#pattern7').val() || "None";
  var param43 = $('#pattern8').val() || "None";
  var param44 = $('#pattern9').val() || "None";
  var param45 = $('#pattern10').val() || "None";

  var param46 = $('input:radio[name="rate1"]:checked').val() || "None";
  var param47 = $('input:radio[name="rate2"]:checked').val() || "None";
  var param48 = $('input:radio[name="rate3"]:checked').val() || "None";
  var param49 = $('input:radio[name="rate4"]:checked').val() || "None";
  var param50 = $('input:radio[name="rate5"]:checked').val() || "None";
  var param51 = $('input:radio[name="rate6"]:checked').val() || "None";
  var param52 = $('input:radio[name="rate7"]:checked').val() || "None";
  var param53 = $('input:radio[name="rate8"]:checked').val() || "None";
  var param54 = $('input:radio[name="rate9"]:checked').val() || "None";
  var param55 = $('input:radio[name="rate10"]:checked').val() || "None";

  var param56 = $('#intpattern1').val() || "None";
  var param57 = $('#intpattern2').val() || "None";
  var param58 = $('#intpattern3').val() || "None";
  var param59 = $('#intpattern4').val() || "None";
  var param60 = $('#intpattern5').val() || "None";
  var param61 = $('#intpattern6').val() || "None";
  var param62 = $('#intpattern7').val() || "None";
  var param63 = $('#intpattern8').val() || "None";
  var param64 = $('#intpattern9').val() || "None";
  var param65 = $('#intpattern10').val() || "None";
  if ((param46 != "None") && (param47 != "None") && (param48 != "None") && (param49 != "None") && (param50 != "None") && (param51 != "None") && (param52 != "None") && (param53 != "None") && (param54 != "None") && (param55 != "None")) {
    $.ajax({
      url: hostUrl,
      type:'POST',
      scriptCharset: 'utf-8',
      data: {userId:param1, date:param2, companion:param3, budget:param4, seed:param5, 
        type1:param6, type2:param7, type3:param8, type4:param9, type5:param10, 
        type6:param11, type7:param12, type8:param13, type9:param14, type10:param15, 
        amount1:param16, amount2:param17, amount3:param18, amount4:param19, amount5:param20, 
        amount6:param21, amount7:param22, amount8:param23, amount9:param24, amount10:param25, 
        score1:param26, score2:param27, score3:param28, score4:param29, score5:param30, 
        score6:param31, score7:param32, score8:param33, score9:param34, score10:param35, 
        pattern1:param36, pattern2:param37, pattern3:param38, pattern4:param39, pattern5:param40, 
        pattern6:param41, pattern7:param42, pattern8:param43, pattern9:param44, pattern10:param45, 
        rate1:param46, rate2:param47, rate3:param48, rate4:param49, rate5:param50, 
        rate6:param51, rate7:param52, rate8:param53, rate9:param54, rate10:param55, intpattern1:param56, 
        intpattern2:param57, intpattern3:param58, intpattern4:param59, intpattern5:param60, intpattern6:param61, 
        intpattern7:param62, intpattern8:param63, intpattern9:param64, intpattern10:param65},
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
    $('#response').html('<span id="alert">全てのプランに評価してください.</span>');
    $('#alert').fadeOut(1500).queue(function() {
      this.remove();
    });
    btn.attr("disabled", false);
  }
});