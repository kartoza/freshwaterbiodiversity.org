define(['models/location_site'], function (LocationSite) {
   return Backbone.View.extend({
        initialize: function (options) {
            this.parent = options.parent;
            _.bindAll(this, 'render');
            this.model.fetch({
                success: this.render
            });
        },
        render: function () {
            var modelJson = this.model.toJSON();
            var geometry = JSON.parse(modelJson['geometry']);
            delete modelJson['geometry'];
            var geojson = {
                'type': 'FeatureCollection',
                'features': [
                    {
                        'type': 'Feature',
                        'geometry': geometry,
                        'properties': modelJson
                    }
                ]
            };
            var features = new ol.format.GeoJSON().readFeatures(geojson, {
                featureProjection: 'EPSG:3857'
            });

            this.parent.addLocationSiteFeatures(features);
        }
   })
});
