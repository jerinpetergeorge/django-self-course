function setChartOnPosition(response) {
    var ctx = document.getElementById('random-chart').getContext('2d');
    var randomChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: response.labels,
            datasets: response.datasets
        },
    });

}

function setRandomChart(randomDataURL) {
    console.log(randomDataURL);
    $.ajax({
        url: randomDataURL,
        method: "GET",
        success: function (response) {
            console.log(response.labels)
            setChartOnPosition(response);

        }
    });


}

