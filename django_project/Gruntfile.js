module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('/package.json'),

        requirejs: {
            compile: {
                options: {
                    baseUrl: 'base/static/js',
                    mainConfigFile: 'base/static/js/app.js',
                    name: 'libs/almond/almond',
                    include: ['app.js'],
                    out: 'base/static/js/optimized.js'
                }
            }
        }

    });

    // Load plugins here.
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-requirejs');

    // Register tasks here.
    grunt.registerTask('default', ['requirejs']);
};
