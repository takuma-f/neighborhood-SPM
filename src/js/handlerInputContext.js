$('#submitContext').click(function() {
  var hostUrl= './cgi_inputContext.cgi';
  var param1 = $('#userId').val();
  var param2 = $('input:radio[name="companion"]:checked').val();
  var param3 = $('#budget').val();
  $.ajax({
    url: hostUrl,
    type:'POST',
    data: {userId : param1, companion : param2, budget : param3},
    // dataType: ???,
    timeout: 100000,
    success: function(returnData) {
      document.write(returnData);
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      alert("error.")
    }
  });
});
