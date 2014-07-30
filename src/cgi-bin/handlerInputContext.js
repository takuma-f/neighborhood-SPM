$('#submitContext').click(function() {
  var hostUrl= './cgi_inputContext.cgi';
  var param1 = $('userId').val();
  var param2 = $('companion').val();
  var param3 = $('budget').val();
  $.ajax({
    url: hostUrl,
    type:'POST',
    data : {parameter1 : param1, parameter2 : param2, parameter3 : param3},
    timeout:100000,
    success: function(transaction_list, patterns) {
      alert(transaction_list);
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      alert("error.")
    }
  });
});
