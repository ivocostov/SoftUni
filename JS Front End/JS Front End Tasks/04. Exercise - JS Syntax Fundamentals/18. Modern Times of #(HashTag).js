function modernTimes(text) {
    
    let splittedText = text.split(' ')
    const regex = /\#[A-Za-z]+/g;
    let searchedWords = text.match(regex)
    // console.log(searchedWords)

    for (let i = 0; i < searchedWords.length; i++) {
        let currentWord = searchedWords[i].replace('#', '')
        console.log(currentWord)
        
    }
}


modernTimes('Nowadays everyone uses # to tag a #special word in #socialMedia')
modernTimes('The symbol # is known #variously in English-speaking #regions as the #number sign')