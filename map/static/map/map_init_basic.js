function map_init_basic (map,options) {
  var json_points = '/data/points/';
  
  $.getJSON(json_points, function(data) {
    var geojson = L.geoJson(data, {
        onEachFeature: function (feature, layer) {

        var photo = '/media/'+feature.properties.photo
        var html = `
          <div class="card" style="width: 18rem;">
            <img class="card-img-top" src="`
            +photo+
            `" alt="カードの画像">
            <div class="card-body">
            <h5 class="card-title">`
            +feature.properties.name+
            `</h5><p class="card-text">登った日:`
            +feature.properties.date+
            `</p>
            </div>
          </div>`;
           
            var field = feature.properties.name+'<br>'+feature.properties.date;
            console.log(html);
            layer.bindPopup(html).openPopup(field);
        }
    });
    geojson.addTo(map);
});
}

