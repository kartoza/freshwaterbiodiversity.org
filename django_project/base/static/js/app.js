
define( ['views/olmap', 'views/side_panel', 'shared'], function(olmap, side_panel, Shared) {
    // Display the map
    var map = new olmap();
    map.render();

    var panel = new side_panel();
    panel.render();
});
