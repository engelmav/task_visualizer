var chart;
$(document).ready(function() {
    console.log("Drawing chart.");
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'container',
            defaultSeriesType: 'line',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Tasks per second'
        },
        xAxis: {
            type: 'datetime',
            //tickPixelInterval: 500,
            //maxZoom: 20 * 1000,
            //min: ) 
            //type: 'logarithmic'
        },
        yAxis: {
            max: 1500,
            min: 0,
            //minPadding: 0.2,
            //maxPadding: 0.2,
            title: {
                text: 'Task qty',
                margin: 80,
            }
        },
        //animation: false,
        series: [{
            name: 'task count',
            data: [  ],
        }]
    });
});
