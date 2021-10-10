getScrapedData = () => {
    console.log("got data");
    temp = {};
    $.ajax({
        async: false,
        type: 'GET',
        url: 'api/content/update',
        success: function(data) {
            temp = data['table'];
        }
    });
    console.log(temp)
    return temp;
};

createTable = (columns) => {
    results = `<table><tr>
    <th>4 chan message<\th>
    <th>predictions<\th>
    <\tr>`;
    resultsEnd = "</table>";
    columns.forEach((row) => { results += `<tr><td>${row[0]}</td><td>${row[1]}</td></tr>`
    }); //inserts div for each matching anime from database
    results += resultsEnd;
    $('.main_table').html(results);
}

repeat = () =>{
    console.log("entered repeat")
    columns = getScrapedData();
    createTable(columns);
};
console.log("started");
repeat();
setInterval(repeat,30000);