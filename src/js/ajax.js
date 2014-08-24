$('#submitContext').click(function() {
  var button = $(this);
    button.attr('disabled', true);

  var hostUrl= './cgi_genPlan.cgi';
  var param1 = $('#userId').val();
  var param2 = $('input:radio[name="companion"]:checked').val();
  var param3 = $('#budget').val();
  $.ajax({
    url: hostUrl,
    type:'POST',
    scriptCharset: 'utf-8',
    data: {userId:param1, companion:param2, budget:param3},
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
});


// $('#viewPlan').click(function() {
//   var button = $(this);
//     button.attr('disabled', true);

//   var hostUrl= './cgi_ref.cgi';
//   var param1 = $('#userId').val();
//   $.ajax({
//     url: hostUrl,
//     type:'POST',
//     scriptCharset: 'utf-8',
//     data: {userId:param1},
//     dataType: 'HTML',
//     timeout: 100000,
//     success: function(res) {
//       $('#planArea').html(res);
//     },
//     error: function(XMLHttpRequest, textStatus, errorThrown) {
//       alert(errorThrown);
//     },
//     complete: function() {
//       button.attr('disabled', false);
//     }
//   });
// });


$('#submitHistory').click(function() {
  var button = $(this);
    button.attr("disabled", true);

  var hostUrl= './cgi_writefile.cgi';
  var param1 = $('#userId').val();
  var param2 = $('#date').val();
  var param3 = $('input:radio[name="companion"]:checked').val();
  var param4 = $('#budget').val();
  var param5 = $('#venue1').val();
  var param6 = $('#venue2').val();
  var param7 = $('#venue3').val();
  var param8 = $('#venue4').val();
  var param9 = $('#venue5').val();
  var param10 = $('#genre1').val();
  var param11 = $('#genre2').val();
  var param12 = $('#genre3').val();
  var param13 = $('#genre4').val();
  var param14 = $('#genre5').val();
  var param15 = $('#action1').val();
  var param16 = $('#action2').val();
  var param17 = $('#action3').val();
  var param18 = $('#action4').val();
  var param19 = $('#action5').val();
  var param20 = $('#rate1').val();
  var param21 = $('#rate2').val();
  var param22 = $('#rate3').val();
  var param23 = $('#rate4').val();
  var param24 = $('#rate5').val();
  $.ajax({
    url: hostUrl,
    type:'POST',
    scriptCharset: 'utf-8',
    data: {userId:param1, date:param2, companion:param3, 
      budget:param4, venue1:param5, venue2:param6, 
      venue3:param7, venue4:param8, venue5:param9, 
      genre1:param10, genre2:param11, genre3:param12, 
      genre4:param13, genre5:param14, action1:param15, 
      action2:param16, action3:param17, action4:param18, 
      action5:param19, rate1:param20, rate2:param21, 
      rate3:param22, rate4:param23, rate5:param24},
    dataType: 'HTML',
    timeout: 100000,
    success: function(res) {
      alert(res)
      $('#response').html(res);
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
      button.attr("disabled", false);
    }
  });
});


// $('#addPlace').click(function() {
//   var button = $(this);
//     button.attr('disabled', true);

//   var hostUrl= '';
//   var param1 = ;
//   $.ajax({
//     url: hostUrl,
//     type:'POST',
//     scriptCharset: 'utf-8',
//     data: {currentAmount:param1},
//     dataType: 'HTML',
//     timeout: 100000,
//     success: function(res) {
//       $('#ItemBox').html(res);
//     },
//     error: function(XMLHttpRequest, textStatus, errorThrown) {
//       alert(errorThrown);
//     },
//     complete: function() {
//       button.attr('disabled', false);
//     }
//   });
// });
