
define(['shared', 'collections/fish'], function(Shared, FishCollection) {
    return Backbone.View.extend({
        template: _.template($('#map-template').html()),
        className: 'map-wrapper',
        map: null,
        fishVectorSource: null,
        events: {
            'click .zoom-in': 'zoomInMap',
            'click .zoom-out': 'zoomOutMap',
            'click .layer-control': 'layerControlClicked'
        },
        initialize: function () {
            // Ensure methods keep the `this` references to the view itself
            _.bindAll(this, 'render');
        },
        zoomInMap: function (e) {
            var view = this.map.getView();
            var zoom = view.getZoom();
            view.animate({
                zoom: zoom-1,
                duration: 250
            })
        },
        zoomOutMap: function (e) {
            var view = this.map.getView();
            var zoom = view.getZoom();
            view.animate({
                zoom: zoom+1,
                duration: 250
            })
        },
        layerControlClicked: function (e) {
            Shared.Dispatcher.trigger('map:layerControlClicked', e);
        },
        renderCollection: function () {
            var self = this;

            for(var i=0; i < this.collection.length; i++) {
                var fish = this.collection.models[i];
                var geojsonObject = JSON.parse(fish.get('geometry'));
                var geojson = {
                    'type': 'FeatureCollection',
                    'features': [
                        geojsonObject
                    ]
                };
                var features = new ol.format.GeoJSON().readFeatures(geojson, {
                    featureProjection: 'EPSG:3857'
                });
                self.fishVectorSource.addFeatures(features);
            }
        },
        render: function() {
            var self = this;

            this.$el.html(this.template());
            $('#map-container').append(this.$el);
            this.map = this.loadMap();

            this.collection = new FishCollection();
            this.collection.fetch().done(function () {
                self.renderCollection();
            });

            return this;
        },
        loadMap: function() {
            var baseSourceLayer;
            var self = this;

            if(bingMapKey) {
                baseSourceLayer = new ol.source.BingMaps({
                    key: bingMapKey,
                    imagerySet: 'AerialWithLabels'
                })
            } else {
                baseSourceLayer = new ol.source.OSM();
            }

            self.fishVectorSource = new ol.source.Vector({});

            var fishVectorLayer = new ol.layer.Vector({
                source: self.fishVectorSource
            });

            return new ol.Map({
                target: 'map',
                layers: [
                    new ol.layer.Tile({
                        source: baseSourceLayer
                    }),
                    fishVectorLayer
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
