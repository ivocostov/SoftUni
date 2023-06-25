function roadRadar(speed, area) {
    let availableAreas = {
        'motorway': 130,
        'interstate': 90,
        'city': 50,
        'residential': 20
    }

    if (speed <= availableAreas[area]) {
        console.log(`Driving ${speed} km/h in a ${availableAreas[area]} zone`)
    } else {
        difference = speed - availableAreas[area]
        speedingStatus = ''
        
        if (difference <= 20) {
            speedingStatus = 'speeding'
        } else if (difference <= 40) {
            speedingStatus = 'excessive speeding'
        } else {
            speedingStatus = 'reckless driving'
        }

        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${availableAreas[area]} - ${speedingStatus}`)
    }
}

roadRadar(40, 'city')
roadRadar(21, 'residential')
roadRadar(120, 'interstate')
roadRadar(200, 'motorway')