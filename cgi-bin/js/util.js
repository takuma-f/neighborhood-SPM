var date = new Date(); 

var yyyy = date.getFullYear();
var mm = date.getMonth()+1;
var dd = date.getDate();

// document.write(yyyy+"-"+mm+"-"+dd);
$('#row_date').append('<input type="date" id="date" name="date" value="'+ yyyy + "-" + mm + "-" + dd + '">');