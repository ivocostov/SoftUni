function revealWords(words, text) {
    let splittedText = text.split(' ')
    let splittedWords = words.split(', ')
    
    // console.log(splittedText)

    for (let w = 0; w < splittedWords.length; w++) {
        let currentWord = splittedWords[w]
        for (let i = 0; i < splittedText.length; i++) {
            let currentText = splittedText[i]
            if (currentText.includes('*')) {
                if (currentWord.length === currentText.length) {
                    text = text.replace(currentText, currentWord)
                }
            }
        }
    }
    console.log(text)
}

revealWords('great', 'softuni is ***** place for learning new programming languages')
revealWords('great, learning', 'softuni is ***** place for ******** new programming languages')