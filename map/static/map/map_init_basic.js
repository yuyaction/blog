function map_init_basic (map,options) {
  var json_points = '/data/points/';
  $.getJSON(json_points, function(data) {
    var geojson = L.geoJson(data, {
        onEachFeature: function (feature, layer) {
            var field = feature.properties.name+'<br>'+feature.properties.date;
            console.log(field);
            layer.bindPopup(field);
        }
    });
    geojson.addTo(map);
});
}

