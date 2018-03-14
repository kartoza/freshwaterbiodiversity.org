
define([], function() {
    return Backbone.View.extend({
        template: _.template($('#map-template').html()),
        map: null,
        events: {
            'click .zoom-in': 'zoomInMap',
            'click .zoom-out': 'zoomOutMap'
        },
        zoomInMap: function (e) {
            var view = map.getView();
            var zoom = view.getZoom();
            view.animate({
                zoom: zoom-1,
                duration: 250
            })
        },
        zoomOutMap: function (e) {
            var view = map.getView();
            var zoom = view.getZoom();
            view.animate({
                zoom: zoom+1,
                duration: 250
            })
        },
        render: function() {
            this.$el.html(this.template());
            $('#map-wrapper').append(this.$el.children());
            this.map = this.loadMap();
            return this;
        },
        loadMap: function() {
            var baseSourceLayer;

            if(bingMapKey) {
                baseSourceLayer = new ol.source.BingMaps({
                    key: bingMapKey,
                    imagerySet: 'AerialWithLabels'
                })
            } else {
                baseSourceLayer = new ol.source.OSM();
            }

            this.map = new ol.Map({
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
        }
    })
});
