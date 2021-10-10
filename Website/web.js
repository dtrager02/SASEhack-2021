$("table tr").each(function(){
    let num = parseFloat($(this).find("td").eq(1).text());
    if(num > .6 || num <.4){
    $(this).find("td").eq(1).css("background-color",`rgb(${parseInt((1-num)*255)},${parseInt(num*255)},0)`);
    console.log(num);
} else {
    $(this).find("td").eq(1).css("background-color",`rgb(150,150,150)`);
}
});