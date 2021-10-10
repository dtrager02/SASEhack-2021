getScrapedData = () => {
    console.log("got data");
    $.ajax({
        async: false,
        type: 'GET',
        url: '/content/update',
        success: function(data) {
            temp = data['table'];
        }
    });
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
    columns = getScrapedData;
    createTable(columns);
};
setInterval(repeat,30000);