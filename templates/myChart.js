var ctx = document.getElementById('myChart');
const data = '{{data_list}}';
var z = /&\#39;/gi
var y = /[\[\]]/gi

n_data = data.replace(z, "");
nn_data = n_data.replace(y, "");

var data_list = nn_data.split(', ')  // 2021-07-23 00:00:00, 10, 34, 2021-07-23 00:00:15, 40, 13, 2021-07-23 00:00:30, 11, 7, 2021-07-23 00:00:45, 24, 24, 2021-07-23 00:01:00, 13, 8

var my_label = [];
var my_data = [];
var my_data2 = [];

for (let i = 0; i < data_list.length; i++) {
  if (i % 3 == 0) { // 날짜 
    if (data_list[i].slice(11, 19) == '00:00:00') {  // 시작날이면 
      my_label.push(data_list[i]);
    }
    else {
      my_label.push(data_list[i].slice(11, 19));
    }
  }
  else if (i % 3 == 1) { // cpu 
    my_data.push(data_list[i]);
  }
  else {
    my_data2.push(data_list[i])
  }
}

var visitorsChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: my_label,
    datasets: [{
      label: 'max data',
      data: my_data,
      borderColor: 'rgb(75, 192, 192)',
      borderColor: '#007bff',
      pointBorderColor: '#007bff',
      pointBackgroundColor: '#007bff',
      fill: false
    },
    {
      label: 'min data',
      data: my_data2,
      borderColor: 'rgb(75, 192, 192)',
      backgroundColor: '#ced4da',
      // borderColor: '#ced4da',
      pointBorderColor: '#ced4da',
      pointBackgroundColor: '#ced4da',
      fill: false
    }]
  },
  options: {
    legend: {
      display: false
    }
  }
});