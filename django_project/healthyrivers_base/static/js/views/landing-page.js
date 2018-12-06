$(document).ready(function () {
    $.ajax({
        url: '/api/module-summary/',
        dataType: 'json',
        success: function (data) {
            var fishData = null;
            if (data.hasOwnProperty('Fish')) {
                fishData = data['Fish'];
            } else if (data.hasOwnProperty('fish')) {
                fishData = data['Fish'];
            }
            if (!fishData) {
                return;
            }

            $('#chart-fish').parent().empty().append('<canvas id="chart-fish" width="210px" height="210px"></canvas>');
            var native = 0;
            var non_native = 0;
            var translocated = 0;
            var totalFish = 0;
            var totalSite = 0;

            $.each(fishData, function (fishClassName, fishClassData) {
                if (fishClassData.hasOwnProperty('total')) {
                    totalFish += fishClassData['total'];
                }
                if (fishClassData.hasOwnProperty('alien')) {
                    non_native += fishClassData['alien'];
                }
                if (fishClassData.hasOwnProperty('indigenous')) {
                    native += fishClassData['indigenous'];
                }
                if (fishClassData.hasOwnProperty('translocated')) {
                    translocated += fishClassData['translocated'];
                }
                if (fishClassData.hasOwnProperty('total_site')) {
                    totalSite += fishClassData['total_site'];
                }
            });

            $('#fish-total-records').html(totalFish);
            $('#fish-total-sites').html(totalSite);

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
        }
    })
});

function createDonutGraph(container, data) {
    var donutChart = new Chart(container, {
        type: 'doughnut',
        data: data,
        options: {
            cutoutPercentage: 70,
            legend: {
                display: false
            }
        }
    });
}