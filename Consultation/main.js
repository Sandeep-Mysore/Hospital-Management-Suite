/*var table = '';
var rows = 2;
var cols = 3;
for(var i=0; i<rows; i++){
  table += '<tr>';
    for(var j=0; j<cols; j++){
      table += '<td>' + j + '</td>';
    }
  table += '</tr>';
}
document.write('<table border="1">' + table + '</table>');
*/
window.onload = function(){
  var body = document.getElementsByTagName('body')[0];
  var table = document.createElement('table');
  var tbody = document.createElement('tbody');
  table.appendChild(tbody);
  for(var i=0; i<6; i++){
    var tr = document.createElement('tr');
    tbody.appendChild(tr);
    for(var j=0; j<6; j++){
      var td = document.createElement('td');
      tr.appendChild(td);
      }
    }
  body.appendChild(table);
}
