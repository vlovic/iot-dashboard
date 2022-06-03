const ctx = document.getElementById('myChart').getContext('2d');

config = {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: "pm02",
            data: []
        }]
    }
}

const myChart = new Chart(ctx, config);

const source = new EventSource("/stream");

source.onmessage = function (event) {
    console.log("onmessage triggered");
    const data = JSON.parse(event.data);
    if (config.data.labels.length === 30) {
        config.data.labels.shift();
        config.data.datasets[0].data.shift();
    }
    config.data.labels.push(data.time);
    config.data.datasets[0].data.push(data.value);
    myChart.update();
}


