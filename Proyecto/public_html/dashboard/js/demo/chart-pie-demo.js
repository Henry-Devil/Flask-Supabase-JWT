

const counts = {
  'admin': 1012,
  'blue-collar': 884,
  'technician': 691,
  'services': 393,
  'management': 324,
  'retired': 166,
  'self-employed': 159,
  'entrepreneur': 148,
  'unemployed': 111,
  'housemaid': 110,
  'student': 82,
  'unknown': 39
};
var nub = document.getElementById("myPieChart");
var myPieChart = new Chart(nub, {
  type: 'pie',
  data: {
    labels: Object.keys(counts),
    datasets: [{
        label: 'Cantidad de trabajos por categoría',
        data: Object.values(counts),
        backgroundColor: ['#4e73df', '#1cc88a','#36b9cc','#FF8800', '#8800FF', '#00FFFF','#FF00FF', '#FFF00', '#00FF00','#FF66FF', '#1cc88a'],
        hoverBackgroundColor: ['#4e73df', '#1cc88a','#36b9cc','#4e73df', '#1cc88a', '#36b9cc','#4e73df', '#1cc88a', '#36b9cc','#4e73df', '#1cc88a'],
        hoverBorderColor: "rgba(234, 236, 244, 1)",
    }]
    
},
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 5,
  },
});
