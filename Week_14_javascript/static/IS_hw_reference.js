// Assign the data from `data.js` to a descriptive variable
var ufodata = data;

// Select the submit button
var submit = d3.select("#filter");

//creating filteredData in the main scope so that it can be used by all the functions
var filteredData


submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#ufo-form-input");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);
  console.log(ufodata);

  filteredData = ufodata.filter(columntype => columntype.datetime === inputValue);

  console.log(filteredData);

  // render the tables
  tabulate(filteredData, ['datetime', 'city', 'state', 'country', 'shape', 'durationMinutes', 'comments']); // 2 column table
 
});


    
function tabulate(data, columns) {
//reference from: "https://gist.github.com/jfreels/6733593"

  var body = d3.select("body");
  var table = d3.select("table");
  var thead = d3.select("thead")
  var tbody = d3.select("tbody");


  // create a row for each object in the data
  var rows = tbody.selectAll('tr')
    .data(filteredData)
    .enter()
    .append('tr');

  // create a cell in each row for each column
  var cells = rows.selectAll('td')
    .data(function (row) {
      return columns.map(function (column) {
        return {column: column, value: row[column]};
      });
    })
    .enter()
    .append('td')
      .text(function (d) { return d.value; });

  return table;
}

============
