// from data.js
var tableData = data;

var tbody = d3.select('tbody');
// console.log(data);

// YOUR CODE HERE!

function newTable(data){
    tbody.html("");

 
data.forEach((UFOreport) => {
    var row = tbody.append('tr');
   
    Object.values(UFOreport).forEach((val) => {
      var cell = row.append('td');
      cell.text(val);
    });
  })
}



function handleClick(){ 
  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var date = d3.select('#datetime').property('value');
  var filteredData = tableData; 

  if(date) {
      filteredData = filteredData.filter((row) => row.datetime === date);
  }

  newTable(filteredData);

}

d3.selectAll('#filter-btn').on('click', handleClick);
  
newTable(tableData);
