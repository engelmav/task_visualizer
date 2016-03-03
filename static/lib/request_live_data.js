function make_human(item){
    var d = null;
    d = moment.utc(item);
    return d;
}
/**
 * Request data from the server, add it to the graph and set a timeout 
 * to request again
 */
function requestData() {
    $.ajax({
        url: 'live_json',
    success: function(points) {

        data = chart.series[0];

        shift = data.length < points.length; // shift if the series is 

        points_cnt = points.length;
        for (var i = 0; i<points_cnt; i++){
            point = points[i];
            timestamp = point[0]*1000;
            taskCnt = point[1];
            point = new Array( timestamp, taskCnt);
            data.addPoint(point, true, false);
            //chart.redraw();
        }
        
        // call it again after one second
        setTimeout(requestData, 1000);
    },
    cache: false
    });
}


