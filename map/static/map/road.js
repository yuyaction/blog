function road (map,options) {
  var route = '/data/gpx/';
  
  $.getJSON(route, function(data) {
    var item_num = Object.keys(data.features).length;
  for(let i = 0; i < item_num; i++) {
    new L.GPX('/media/'+data.features[i].properties.gpx_file, {
        async: true,
        marker_options: {
        startIconUrl: false,
        endIconUrl: false,
        shadowUrl: false
        },
        polyline_options: {
        color: '#ff3200',
        opacity: 0.75,
        weight: 3,
        lineCap: 'round'
        }
      }).on('loaded', function(e) {
      }).addTo(map);
    }
  }); 
}

