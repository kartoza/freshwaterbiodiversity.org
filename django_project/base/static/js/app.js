
define( ['views/olmap', 'views/side_panel', 'collections/location_site', 'shared'], function(olmap, side_panel, LocationSiteCollection, Shared) {
    // Display the map
    var locationSiteCollection = new LocationSiteCollection();
    var map = new olmap({
        collection: locationSiteCollection
    });

    var panel = new side_panel();
    panel.render();
});
