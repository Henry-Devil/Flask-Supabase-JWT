// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function(n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
}

// bar Chart Example

const ctx = document.getElementById('myAreaChart');
    const myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Yes', 'No', 'Unknown'],
        datasets: [{
          label: 'Respuestas',
          data: [2175, 1839, 105],
          backgroundColor: [
            'rgba(75, 192, 192)',
            'rgba(255, 99, 132)',
            'rgba(255, 206, 86)'
          ],
          borderColor: [
            'rgba(75, 192, 192, 1)',
            'rgba(255, 99, 132, 1)',
            'rgba(255, 206, 86, 1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });

const dat = document.getElementById('mypruebaChart');
const prueba = new Chart(dat, {
  type: 'polarArea',
  data: {
    labels: ['No', 'Yes', 'Unknown'],
    datasets: [{
      label: 'Respuestas',
      data: [3349, 665, 105],
      backgroundColor: [
        'rgba(255, 99, 132,0.7)',
        'rgba(75, 192, 192)',
        'rgba(255, 206, 86)'
      ]
    }]
  }
});