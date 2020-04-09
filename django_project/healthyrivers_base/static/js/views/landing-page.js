$(document).ready(function () {
    $.ajax({
        url: '/api/module-summary/',
        dataType: 'json',
        success: function (data) {
            var fishData = null;
            if (data.hasOwnProperty('fish')) {
                fishData = data['fish'];
            }
            createFishCharts(fishData);
            if (data.hasOwnProperty('invert')) {
                createInvertCharts(data['invert']);
            }
            if (data.hasOwnProperty('algae')) {
                createAlgaeChart(data['algae']);
            }
        }
    });
    $('[data-toggle="tooltip"]').tooltip()
});

function createFishCharts(fishData) {
    if (!fishData) {
        return;
    }
    $('#chart-fish').parent().empty().append('<canvas id="chart-fish" width="150px" height="150px"></canvas>');
    var native = 0;
    var non_native = 0;
    var translocated = 0;
    var totalFish = 0;
    var totalSite = 0;

    if (fishData.hasOwnProperty('total')) {
        totalFish += fishData['total'];
    }
    if (fishData.hasOwnProperty('alien')) {
        non_native += fishData['alien'];
    }
    if (fishData.hasOwnProperty('indigenous')) {
        native += fishData['indigenous'];
    }
    if (fishData.hasOwnProperty('translocated')) {
        translocated += fishData['translocated'];
    }
    if (fishData.hasOwnProperty('total_site')) {
        totalSite += fishData['total_site'];
    }

    $('#fish-total-records').html(totalFish);
    $('#fish-total-sites').html(totalSite);

    var fishContainer = document.getElementById("chart-fish");
    var fishChartDataset = {
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
    createDonutGraph(fishContainer, fishChartDataset)
}

function createInvertCharts(invertData) {
     $('#chart-invert').parent().empty().append('<canvas id="chart-invert" width="150px" height="150px"></canvas>');
    let invertContainer = document.getElementById("chart-invert");
    let totalInvert = 0;
    let totalSite = 0;
    let totalSass = 0;
    if (invertData.hasOwnProperty('total')) {
        totalInvert += invertData['total'];
    }
    if (invertData.hasOwnProperty('total_site')) {
        totalSite += invertData['total_site'];
    }
    if (invertData.hasOwnProperty('total_sass')) {
        totalSass += invertData['total_sass'];
    }
    $('#invert-total-records').html(totalInvert);
    $('#invert-total-sites').html(totalSite);
    $('#invert-total-sass').html(totalSass);
    let labels = [];
    let backgroundColors = [];
    let chartData = [];
    $.each(invertData['ecological_data'], function (index, ecologicalData) {
        labels.push(ecologicalData['value']);
        backgroundColors.push(ecologicalData['color']);
        chartData.push(ecologicalData['count']);
    });
    let invertChartDataset = {
        labels: labels,
        datasets: [{
            data: chartData,
            backgroundColor: backgroundColors,
            borderWidth: 1
        }]
    };
    createDonutGraph(invertContainer, invertChartDataset);
}

function createAlgaeChart(algaeData) {
    if (!algaeData) {
        return;
    }
    $('#chart-algae').parent().empty().append('<canvas id="chart-algae" width="150px" height="150px"></canvas>');
    let algaeContainer = document.getElementById("chart-algae");
    $('#algae-total-records').html(algaeData['total']);
    $('#algae-total-sites').html(algaeData['total_site']);
    let algaeChartDataset = {
        labels: ['Algae'],
        datasets: [{
            data: [algaeData['total']],
            backgroundColor: ['#18A090'],
            borderWidth: 1
        }]
    };
    createDonutGraph(algaeContainer, algaeChartDataset);
}

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