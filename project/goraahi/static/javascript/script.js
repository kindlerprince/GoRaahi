$(document).ready(function(){
	$('#datepicker').datepicker({
	    format: 'dd-MM-yyyy',
	    startDate: new Date()
	});
});

/*  verify search form */

function verify()
{
	var date=document.myform.j_date.value;
	if(document.myform.source.value=="")
	{
		document.myform.source.focus();
		alert("Please enter a source of journey");
		return false;
	}
	else if(document.myform.destination.value=="")
	{
		document.myform.source.focus();
		alert("Please enter a destination of journey");
		return false;
	}
	else if(date=="")
	{
		alert("enter a valid journey date");
		return false;
	}
	else
	{
		return true;
	}
}
