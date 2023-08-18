const weather = document.getElementById('weather');
const weatherButton = document.getElementById('weatherButton');
const key = 'fc51288f3361495ca3b192012231708';
const city = document.getElementById('city')
const temp = document.getElementById('temp')
const wind = document.getElementById('wind')
const localData = document.getElementById('local-data')
const weatherImage = document.getElementById('weather-img')
const country = document.getElementById('country')
const region = document.getElementById('region')
const nameC = document.getElementById('name')
const timeC = document.getElementById('time')
console.log('hello')
weatherButton.addEventListener('click', function ()
{
    console.log('hello')
    weather.dispatchEvent(new Event('submit'));
});

weather.addEventListener('submit', function (e)
{
    e.preventDefault();
    formData = new FormData(e.target);
    local = formData.get('city');
    fetch('http://api.weatherapi.com/v1/current.json?key=' + key + '&q=' + local + '&aqi=no')
        .then(response => response.json())
        .then(data =>
        {
            console.log(data);
            if(! data.error) {
                localData.style.display = "block"
            }
            weatherImage.src = data.current.condition.icon
            city.innerText = data.current.condition.text
            temp.innerText = data.current.feelslike_f + "\u00B0F"
            wind.innerText = data.current.wind_mph + " mph"
            country.innerText = data.location.country
            region.innerText = data.location.region
            nameC.innerText = data.location.name
            time.innerText = data.location.localtime
            let cityData = {
                'condition': data.current.condition.text,
                'temp': data.current.feelslike_f + ' degF',
                'wind': data.current.wind_mph + ' mph',
                'country': data.location.country,
                'region': data.location.region,
                'city': data.location.name,
                'time': data.location.localtime
            }
            console.log(cityData)
        })
        .catch(error =>
        {
            console.log(error);
        });
})



