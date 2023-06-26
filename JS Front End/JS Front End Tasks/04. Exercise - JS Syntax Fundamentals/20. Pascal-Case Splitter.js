function pascalCaseSplitter(text) {
    let separatedText = text.split(/(?=[A-Z])/)
    console.log(separatedText.join(', '))
}

pascalCaseSplitter('SplitMeIfYouCanHaHaYouCantOrYouCan')
pascalCaseSplitter('HoldTheDoor')
pascalCaseSplitter('ThisIsSoAnnoyingToDo')