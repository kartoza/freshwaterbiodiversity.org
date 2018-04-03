define(['models/location_site'], function (LocationSite) {
   return Backbone.Collection.extend({
       model: LocationSite,
       url: "/api/location-site/"
   })
});
