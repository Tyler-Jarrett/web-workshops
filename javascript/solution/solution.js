//Simple loop, makes random guess, checks against number, returns guess count
function makeGuesses(numFingers){
    let correctGuess = false;
    let guessCount = 1;

    while(!correctGuess){
        let guess = Math.floor(Math.random() * 6);

        if (guess == numFingers){
            correctGuess = true;
        }
        else{
            guessCount++;
        }

        if (guessCount > 100){
            console.warn("Something has gone wrong with the guessing game, exiting now")
            return null;
        }
    }

    return guessCount;
}

document.getElementById("first_guess").onclick = function(){
    let numFingers = document.forms["first_game"]["number_select"].value
    let guessCount = makeGuesses(numFingers);

    if (guessCount == null){
        return;
    }

    window.alert("I got it, you were holding up " + numFingers + " fingers, I got it in " + guessCount + " guesses!")
}