function randomColorRGBA(a = 1) {
    /* random rgba() creator | wrote: NightFox */
    let _r, _g, _b, _rgba;
    _r = Math.round(Math.random() * 250);
    _g = Math.round(Math.random() * 250);
    _b = Math.round(Math.random() * 250);
    _rgba = "rgba(" + _r + ", " + _g + ", " + _b + ", " + a + ")";
    return _rgba;
}

function saveJSON(id) {
    // Function to save form data as JSON
    document.getElementById('save-json').addEventListener('click', function () {
        // Get the form element
        const form = document.getElementById(id);

        // Create an object to hold the form data
        let formData = {};

        // Loop through each element in the form
        for (let element of form.elements) {
            if (element.name) {
                formData[element.name] = element.value;
            }
        }

        // Convert the form data object to a JSON string
        const json = JSON.stringify(formData, null, 2);

        // Display the JSON string (for demonstration purposes)
        console.log(json);

        // Create a blob of the JSON data
        const blob = new Blob([json], {type: 'application/json'});

        // Create a link element to download the JSON file
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = 'location_data.json';

        // Append the link to the body and click it to trigger the download
        document.body.appendChild(a);
        a.click();

        // Remove the link element after download
        document.body.removeChild(a);
    });
}
