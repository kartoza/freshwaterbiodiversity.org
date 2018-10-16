$(document).ready(function () {
    $.ajax({
        url: '/api/location-site/',
        dataType: 'json',
        success: function (data) {
            var total_sites = Object.keys(data).length;
            $('#fish-total-sites').html(total_sites);
        }
    });
    $.ajax({
        url: '/api/fish-summary/',
        dataType: 'json',
        success: function (data) {
            $('#chart-fish').parent().empty().append('<canvas id="chart-fish" width="250px" height="250px"></canvas>');
            var native = 0;
            var non_native = 0;
            var translocated = 0;
            $.when($.each(data, function (index, value) {
                if(value.hasOwnProperty('total_fish')){
                    $('#fish-total-records').html(value['total_fish']);
                }

                if (value.hasOwnProperty('category')) {
                    if(value['category'] === 'indigenous') {
                        native += value['total'];
                    }
                    if(value['category'] === 'native') {
                        native += value['total'];
                    }
                    if(value['category'] === 'alien') {
                        non_native += value['total'];
                    }
                    if(value['category'] === 'non-native') {
                        non_native += value['total'];
                    }
                    if(value['category'] === 'translocated') {
                        translocated += value['total'];
                    }
                }
            })).then(function () {
                var fishContainer = document.getElementById("chart-fish");
                var fishData = {
                    labels: ["Native", "Non-Native", "Translocated"],
                    datasets: [{
                        data: [native, non_native, translocated],
                        backgroundColor: [
                            '#a13447',
                            '#00a99d',
                            '#e0d43f'
                        ],
                        borderWidth: 1
                    }]
                };
                createDonutGraph(fishContainer, fishData)
            });
        }
    })
});

function createDonutGraph(container, data) {
    var donutChart = new Chart(container, {
        type: 'doughnut',
        data: data,
        options: {
            cutoutPercentage: 60,
            legend: {
                display: false
            }
        }
    });
}