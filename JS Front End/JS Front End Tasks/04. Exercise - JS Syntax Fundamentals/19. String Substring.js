function stringSubstring(word, text) {
    let lowerCaseText = text.toLowerCase()
    let lowerCaseWord = word.toLowerCase()

    if (lowerCaseText.includes(lowerCaseWord)) {
        console.log(word)
    } else {
        console.log(`${lowerCaseWord} not found!`)
    }
}

stringSubstring('javascript', 'JavaScript is the best programming language')
stringSubstring('python', 'JavaScript is the best programming language')