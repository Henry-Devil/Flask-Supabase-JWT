//// Call the dataTables jQuery plugin
//$(document).ready(function() {
//  $('#dataTable').DataTable();
//});
//

const dat = document.getElementById('mypruebaChart');
const myChart = new Chart(dat, {
  type: 'polarArea',
  data: {
    labels: ['No', 'Yes', 'Unknown'],
    datasets: [{
      label: 'Respuestas',
      data: [3349, 665, 105],
      backgroundColor: [
        'rgba(255, 99, 132)',
        'rgba(75, 192, 192)',
        'rgba(255, 226, 86)'
      ]
    }]
  }
});