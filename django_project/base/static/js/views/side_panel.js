define(['shared'], function(Shared) {
    return Backbone.View.extend({
        template: _.template($('#side-panel-template').html()),
        className: 'panel-wrapper',
        rightPanel: null,
        events: {
            'click .close-panel': 'closeSidePanel'
        },
        initialize: function () {
            // Events
            Shared.Dispatcher.on('sidePanel:openSidePanel', this.openSidePanel, this);
            Shared.Dispatcher.on('sidePanel:closeSidePanel', this.closeSidePanel, this);
        },
        render: function() {
            this.$el.html(this.template());
            $('#map-container').append(this.$el);

            // Hide the side panel
            this.rightPanel = this.$el.find('.right-panel');
            this.rightPanel.css('display', 'none');

            return this;
        },
        openSidePanel: function (properties) {
            this.rightPanel.show('slide', { direction: 'right'}, 200);
            if(properties) {
                this.clearSidePanel();
                this.fillSidePanel(properties);
            }
        },
        closeSidePanel: function (e) {
            var self = this;
            this.rightPanel.hide('slide', { direction: 'right'}, 200, function () {
                self.clearSidePanel();
            });
        },
        fillSidePanel: function (contents) {
            for (var key in contents) {
                if (contents.hasOwnProperty(key)) {
                    $('#content-panel').append('<p>'+ key +' : '+ contents[key] +'</p>');
                }
            }
        },
        clearSidePanel: function () {
            $('#content-panel').html('');
        }
    })
});
