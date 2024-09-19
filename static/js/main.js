document.querySelector("#predict-button").addEventListener("click", () => {
    const features = [/* your feature data here */];

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ features: features }),
    })
    .then(response => response.json())
    .then(data => {
        alert("Prediction: " + data.prediction);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
