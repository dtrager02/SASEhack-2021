getScrapedData = (callback) => {
    console.log("got data");
    temp = {};
    $.ajax({
        async: false,
        type: 'GET',
        url: 'api/content/update',
        success: function(data) {
            callback(data['response']['post']['table']);
        }
    });
};

createTable = (columns) => {
    columns.forEach((row) => {$(".main_table > tbody").append(`<tr><td>${row[0]}</td><td>${row[1]}</td></tr>`)
    }); 
}

repeat = () =>{
    console.log("entered repeat")
    getScrapedData((columns) => {
        $(".main_table > tbody").html("");
        createTable(columns);
        $(".main_table tr").each(function(){
            let num = parseFloat($(this).find("td").eq(1).text());
            if(num > .6 || num <.4){
            $(this).find("td").eq(1).css("background-color",`rgb(${parseInt((num)*255)},${parseInt((1-num)*255)},0,.5)`);
            console.log(num);
        } else {
            $(this).find("td").eq(1).css("background-color",`rgb(150,150,150,.8)`);
        }
        });
    });
};
console.log("started");
repeat();
setInterval(repeat,30000);