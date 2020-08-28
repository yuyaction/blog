function map_init_basic (map,options) {
  var json_points = '/data/points/';
  
  $.getJSON(json_points, function(data) {
    var geojson = L.geoJson(data, {
        onEachFeature: function (feature, layer) {
        var count = 0;
        for (let i =1;i<6;i++){
          s = String(i);
          if ((eval('feature.properties.photo'+s))){
            count++;
          }
        }
        var photo1 = '/media/'+feature.properties.photo1
        var html = `
          <div class="card" style="width: 18rem;">
            <a href="`
            +photo1+
            `" class="luminous">
            <img class="card-img-top" src="`
            +photo1+
            `" alt="カードの画像">
            </a>
            <div class="card-body">
            <h5 class="card-title">`
            +feature.properties.name+
            `</h5><p class="card-text">登った日:`
            +feature.properties.date+
            `</p>
            </div>
          </div>`;
        for (let i =2;i<count+1;i++){
         s = String(i);
         add_photo = '/media/'+eval('feature.properties.photo'+s);
         var hidden_html = `
            <a href="`
            +add_photo+
            `" class="luminous">
            </a>
            `;
         html = html + hidden_html;
        }
            layer.bindPopup(html).on( 'popupopen', function ( popup ) {
            new LuminousGallery(document.querySelectorAll('.luminous'));
            });
        }
        , pointToLayer: function( feature, latlng ) {
            var icn = L.icon({
                iconUrl: '/media/yama.png', 
                //iconRetinaUrl: 'sample2.png',
                iconSize: [30, 30],
                iconAnchor: [12, 25],
                popupAnchor: [0, -25],
            });
            return L.marker( latlng, { icon: icn });
          }
    });
    geojson.addTo(map);
});
}

