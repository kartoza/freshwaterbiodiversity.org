define(['shared'], function(Shared) {
    return Backbone.View.extend({
        template: _.template($('#side-panel-template').html()),
        className: 'panel-wrapper',
        rightPanel: null,
        events: {
        },
        initialize: function () {
            // Events
            Shared.Dispatcher.on('map:layerControlClicked', this.openSidePanel, this);
        },
        render: function() {
            this.$el.html(this.template());
            $('#map-container').append(this.$el);

            // Hide the side panel
            this.rightPanel = this.$el.find('.right-panel');
            this.rightPanel.css('display', 'none');

            return this;
        },
        openSidePanel: function (e) {
            this.rightPanel.show('slide', { direction: 'right'}, 200);
        }
    })
});
