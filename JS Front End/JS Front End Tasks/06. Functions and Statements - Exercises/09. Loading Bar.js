function loadingBar(number) {
    let loadBar = ""
    let percentage = number / 10
    
    if (number === 100) {
        console.log('100% Complete!')
        
    } else {
        for (let i = 0; i < percentage; i++) {
            loadBar += '%'
        }
        for (let j = percentage; j < 10; j++) {
            loadBar += '.'
        } console.log(`${number}% [${loadBar}] \nStill loading...`)
    } 
}

loadingBar(30)
loadingBar(50)
loadingBar(100)