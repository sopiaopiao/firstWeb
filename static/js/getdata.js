function gethsdata(){
//$(document).ready(function() {  
   var chart = {
       plotBackgroundColor: null,
       plotBorderWidth: null,
       plotShadow: false
   };
   var title = {
      text: 'HeartStone'   
   };      
   var tooltip = {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
   };
   var plotOptions = {
      pie: {
         allowPointSelect: true,
         cursor: 'pointer',
         dataLabels: {
            enabled: true,
            format: '<b>{point.name}%</b>: {point.percentage:.1f} %',
            style: {
               color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
            }
         }
      }
   };
   var series= [{
      type: 'pie',
      name: 'Role share',
      data: [
         ['牧师',   45.0],
         ['法师',       26.8],
//         {
//            name: '术士',
//            y: 12.8,
//            sliced: true,
//            selected: true
//         },
          ['术士', 12.8],
         ['德鲁伊',    8.5],
         ['战士',     6.2],
         ['其他',   0.7]
      ]
   }];     
      
   var json = {};   
   json.chart = chart; 
   json.title = title;     
   json.tooltip = tooltip;  
   json.series = series;
   json.plotOptions = plotOptions;
   $('#container1').highcharts(json);  
//});
}

