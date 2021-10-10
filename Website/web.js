// adds color based on confidence 
$("table tr").each(function(){
    let num = parseFloat($(this).find("td").eq(1).text());
    if(num > .6 || num <.4){
    $(this).find("td").eq(1).css("background-color",`rgb(${parseInt((num/10.0)*255)},${parseInt((1-num/10.0)*255)},0)`);
    console.log(num);
} else {
    $(this).find("td").eq(1).css("background-color",`rgb(150,150,150)`);
}
});

//Comment button inputs
function clickfun()
{
   var input = document.getElementById("val1").value;
   document.getElementById("val1").value = "Response Recorded!";
   console.log(input);
   return input;
}