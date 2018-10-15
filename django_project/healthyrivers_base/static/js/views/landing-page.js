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
        url: '/api/fish-collections/',
        dataType: 'json',
        success: function (data) {
            $('#chart-fish').parent().empty().append('<canvas id="chart-fish" width="250px" height="250px"></canvas>');
            var total_sites = Object.keys(data).length;
            $('#fish-total-records').html(total_sites);
            var native = 0;
            var non_native = 0;
            var translocated = 0;
            $.each(data, function (index, key) {
                if(key['category'] === 'native' || key['category'] === 'indigenous'){
                    native += 1;
                }
                if(key['category'] === 'non-native' || key['category'] === 'alien'){
                    non_native += 1;
                }
                if(key['category'] === 'translocated'){
                    translocated += 1;
                }

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
            })
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