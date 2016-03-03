function load_json(callback){
    var task_json = null;
    console.log("from jsonretriever.js");
    $.ajax({
        'type': "GET",
        'async': true,
        'global': false,
        'url': "get_task_json",
        'dataType': "json",
    })
    .done(callback);
}
