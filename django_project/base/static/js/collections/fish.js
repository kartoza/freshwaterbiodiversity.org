define(['models/fish'], function (Fish) {
   return Backbone.Collection.extend({
       model: Fish,
       url: "/api/fish-collections/"
   })
});
