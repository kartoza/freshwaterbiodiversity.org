
var baseSourceLayer;

if(bingMapKey) {
    baseSourceLayer = new ol.source.BingMaps({
        key: bingMapKey,
        imagerySet: 'AerialWithLabels'
    })
} else {
    baseSourceLayer = new ol.source.OSM();
}


var map = new ol.Map({
    target: 'map',
    layers: [
        new ol.layer.Tile({
            source: baseSourceLayer
        })
    ],
    view: new ol.View({
        center: ol.proj.fromLonLat([22.937506, -30.559482]),
        zoom: 7
    }),
    controls: ol.control.defaults({
        zoom: false
    })
});


$('.close-panel').click(function () {
    $( ".right-panel" ).toggle( "slide", {
        direction: 'right'
    });
});

$('.zoom-in').click(function () {
    var view = map.getView();
    var zoom = view.getZoom();
    view.animate({
        zoom: zoom-1,
        duration: 250
    })
});

$('.zoom-out').click(function () {
    var view = map.getView();
    var zoom = view.getZoom();
    view.animate({
        zoom: zoom+1,
        duration: 250
    })
});