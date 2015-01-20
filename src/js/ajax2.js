$('#submitContext').click(function() {
  var button = $(this);
    button.attr('disabled', true);

  var hostUrl= './cgi_genPlan.cgi';
  var param1 = $('#userId').val();
  var param2 = $('#companion').val();
  var param3 = $('#budget').val();
  var param4 = $('#focus1').val();
  var param5 = $('#focus2').val();
  if (param4 != param5) {
    $.ajax({
      url: hostUrl,
      type:'POST',
      scriptCharset: 'utf-8',
      data: {userId:param1, companion:param2, budget:param3, focus1:param4, focus2:param5},
      dataType: 'HTML',
      timeout: 100000,
      success: function(res) {
        $('#planArea').html(res);
      },
      error: function(XMLHttpRequest, textStatus, errorThrown) {
        alert(errorThrown);
      },
      complete: function() {
        button.attr('disabled', false);
      }
    });
  } else {
    $('#requestResponse').html('<span id="alert">ジャンル1とジャンル2は異なる行動から選択してください.</span>');
    $('#alert').fadeOut(1500).queue(function() {
      this.remove();
    });
    button.attr("disabled", false);
  }
});

$('#genPattern').click(function() {
  var button = $(this);
    button.attr('disabled', true);

  var hostUrl= './cgi_genPattern.cgi';
  var param1 = $('#genre1').val();
  var param2 = $('#genre2').val();
  var param3 = $('#genre3').val();
  var param4 = $('#genre4').val();
  var param5 = $('#genre5').val();
  $.ajax({
    url: hostUrl,
    type:'POST',
    scriptCharset: 'utf-8',
    data: {genre1:param1, genre2:param2, genre3:param3, genre4:param4, genre5:param5},
    dataType: 'HTML',
    timeout: 100000,
    success: function(res) {
      $('#patternArea').html(res);
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      alert(errorThrown);
    },
    complete: function() {
      button.attr('disabled', false);
    }
  })
});

$('#saveRating').click(function() {
  var button = $(this);
    button.attr("disabled", true);

  var hostUrl= './cgi_writefile2.cgi';
  var param1 = $('#userId').val();
  var param2 = $('#date').val() || "None";
  var param3 = $('#companion').val() || "None";
  var param4 = $('#budget').val() || "None";
  var param5 = $('#pattern1').val();
  var param6 = $('#pattern2').val();
  var param7 = $('#pattern3').val();
  var param8 = $('#pattern4').val();
  var param9 = $('#pattern5').val();
  var param10 = $('#pattern6').val();
  var param11 = $('#pattern7').val();
  var param12 = $('#pattern8').val();
  var param13 = $('#pattern9').val();
  var param14 = $('#pattern10').val();
  var param15 = $('input:radio[name="rate1"]:checked').val() || "None";
  var param16 = $('input:radio[name="rate2"]:checked').val() || "None";
  var param17 = $('input:radio[name="rate3"]:checked').val() || "None";
  var param18 = $('input:radio[name="rate4"]:checked').val() || "None";
  var param19 = $('input:radio[name="rate5"]:checked').val() || "None";
  var param20 = $('input:radio[name="rate6"]:checked').val() || "None";
  var param21 = $('input:radio[name="rate7"]:checked').val() || "None";
  var param22 = $('input:radio[name="rate8"]:checked').val() || "None";
  var param23 = $('input:radio[name="rate9"]:checked').val() || "None";
  var param24 = $('input:radio[name="rate10"]:checked').val() || "None";
  if ((param15 != "None") && (param16 != "None") && (param17 != "None") && (param18 != "None") && (param19 != "None") && (param20 != "None") && (param21 != "None") && (param22 != "None") && (param23 != "None") && (param24 != "None")) {
    $.ajax({
      url: hostUrl,
      type:'POST',
      scriptCharset: 'utf-8',
      data: {userId:param1, date:param2, companion:param3, 
        budget:param4, pattern1:param5, pattern2:param6, 
        pattern3:param7, pattern4:param8, pattern5:param9, 
        pattern6:param10, pattern7:param11, pattern8:param12, 
        pattern9:param13, pattern10:param14, rate1:param15, 
        rate2:param16, rate3:param17, rate4:param18, 
        rate5:param19, rate6:param20, rate7:param21, 
        rate8:param22, rate9:param23, rate10:param24},
      dataType: 'HTML',
      timeout: 100000,
      success: function(res) {
        $('#response').html('<span id="alert">保存しました.</span>');
        $('#alert').fadeOut(1500).queue(function() {
          this.remove();
        });
      },
      error: function(XMLHttpRequest, textStatus, errorThrown) {
        $('#response').html('<span id="alert">予期しないエラーが発生しました.</span>');
        $('#alert').fadeOut(1500).queue(function() {
          this.remove();
        });
      },
      complete: function() {
        button.attr("disabled", false);
      }
    });
  } else {
    $('#response').html('<span id="alert">全てのプランに評価してください.</span>');
    $('#alert').fadeOut(1500).queue(function() {
      this.remove();
    });
    button.attr("disabled", false);
  }
});