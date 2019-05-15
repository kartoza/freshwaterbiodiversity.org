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
        }
    })
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
    if (invertData.hasOwnProperty('total')) {
        totalInvert += invertData['total'];
    }
    if (invertData.hasOwnProperty('total_site')) {
        totalSite += invertData['total_site'];
    }
    $('#invert-total-records').html(totalInvert);
    $('#invert-total-sites').html(totalSite);
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