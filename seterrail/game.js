const mapContainer = document.getElementById('map-container');

// Function to create city dots
function createCityDots() {
    cities.forEach(city => {
        const dot = document.createElement('div');
        dot.classList.add('city-dot');
        dot.style.left = `${city.x}px`;
        dot.style.top = `${city.y}px`;
        dot.dataset.name = city.name;
        dot.dataset.region = city.region;
        dot.dataset.attempts = 0;
        dot.dataset.guessed = false;
        mapContainer.appendChild(dot);
    });
}

createCityDots();
let currentCityIndex = 0;
let currentCity = cities[currentCityIndex];

document.getElementById('current-city').textContent = currentCity.name;

// Event listener for city dots
mapContainer.addEventListener('click', function(event) {
    if (event.target.classList.contains('city-dot')) {
        handleCityClick(event.target);
    }
});

function handleCityClick(dot) {
    if (dot.dataset.guessed === 'true') {
        // Already guessed correctly
        return;
    }

    if (dot.dataset.name === currentCity.name) {
        // Correct guess
        dot.dataset.guessed = 'true';
        let attempts = parseInt(dot.dataset.attempts);

        if (attempts === 0) {
            dot.style.backgroundColor = 'white';
        } else if (attempts === 1) {
            dot.style.backgroundColor = 'yellow';
        }
        nextCity();
    } else {
        // Wrong guess
        if (dot.dataset.attempts === '0') {
            dot.dataset.attempts = '1';
            showLabel(dot, `${dot.dataset.name} (${dot.dataset.region})`);
        }

        let attempts = parseInt(currentCity.attempts || '0');
        currentCity.attempts = attempts + 1;

        if (currentCity.attempts >= 3) {
            blinkDot(dot);
        }
    }
}

function nextCity() {
    currentCityIndex++;
    if (currentCityIndex < cities.length) {
        currentCity = cities[currentCityIndex];
        document.getElementById('current-city').textContent = currentCity.name;
    } else {
        alert('Game Over!');
    }
}

function showLabel(dot, text) {
    const label = document.createElement('div');
    label.classList.add('label');
    label.textContent = text;
    label.style.left = `${parseInt(dot.style.left) + 15}px`;
    label.style.top = `${parseInt(dot.style.top) - 10}px`;
    mapContainer.appendChild(label);

    // Optional: Draw a line between the dot and the label
}

function blinkDot(dot) {
    dot.style.backgroundColor = 'red';
    dot.classList.add('blink');
    // Add CSS animation for blinking
}
