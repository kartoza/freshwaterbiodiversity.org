
define(['shared', 'models/location_site', 'views/location_site'], function(Shared, LocationSiteModel, LocationSiteView) {
    return Backbone.View.extend({
        template: _.template($('#map-template').html()),
        className: 'map-wrapper',
        map: null,
        locationSiteVectorSource: null,
        events: {
            'click .zoom-in': 'zoomInMap',
            'click .zoom-out': 'zoomOutMap',
            'click .layer-control': 'layerControlClicked'
        },
        initialize: function () {
            // Ensure methods keep the `this` references to the view itself
            _.bindAll(this, 'render');
            this.collection.fetch({
                success: this.render
            })
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
        mapClicked: function (e) {
            var self = this;
            var features = self.map.getFeaturesAtPixel(e.pixel);
            if (features) {
                self.featureClicked(features[0]);
            } else {
               Shared.Dispatcher.trigger('sidePanel:closeSidePanel');
            }
        },
        featureClicked: function (feature) {
            var self = this;
            var properties = feature.getProperties();
            delete properties['geometry'];
            if(properties.hasOwnProperty('location_type')) {
                properties = properties['location_type'];
            }
            Shared.Dispatcher.trigger('sidePanel:openSidePanel', properties);
        },
        layerControlClicked: function (e) {
        },
        renderCollection: function () {
            var self = this;

            for(var i=0; i < this.collection.length; i++) {
                var locationSiteModel = this.collection.models[i];
                var locationSiteView = new LocationSiteView({
                    model: locationSiteModel,
                    parent: this
                });
            }
        },
        render: function() {
            var self = this;

            this.$el.html(this.template());
            $('#map-container').append(this.$el);
            this.map = this.loadMap();

            self.renderCollection();

            this.map.on('click', function (e) {
               self.mapClicked(e);
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

            self.locationSiteVectorSource = new ol.source.Vector({});

            var locationSiteVectorLayer = new ol.layer.Vector({
                source: self.locationSiteVectorSource
            });

            return new ol.Map({
                target: 'map',
                layers: [
                    new ol.layer.Tile({
                        source: baseSourceLayer
                    }),
                    locationSiteVectorLayer
                ],
                view: new ol.View({
                    center: ol.proj.fromLonLat([22.937506, -30.559482]),
                    zoom: 7
                }),
                controls: ol.control.defaults({
                    zoom: false
                })
            });
        },
        addLocationSiteFeatures: function (features) {
            this.locationSiteVectorSource.addFeatures(features);
        }
    })
});
