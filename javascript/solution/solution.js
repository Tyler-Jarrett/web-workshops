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
            return;
        }
    }

    window.alert("I got it, you were holding up " + numFingers + " fingers, I got it in " + guessCount + " guesses!")
    return;
}

function changeLetters(){
   
    for (const letter of letters){
        if (letter.id == "letter_e"){
            if (Math.random() < SWAP_CHANCE) {
                if (letter.innerText == "E")
                    letter.innerText = "3"
                else 
                    letter.innerText = "E"
            }
        } else if (letter.id == "letter_l"){
            if (Math.random() < SWAP_CHANCE) {
                if (letter.innerText == "LL")
                    letter.innerText = "77"
                else 
                    letter.innerText = "LL"
            }
        } else if (letter.id == "letter_o"){
            if (Math.random() < SWAP_CHANCE) {
                if (letter.innerText == "O")
                    letter.innerText = "0"
                else 
                    letter.innerText = "O"
            }
        }
    }
}

function validationIsInRange(value, lowerBound, upperBound){
    if (value < lowerBound)
        return false;
    if (value > upperBound)
        return false;
    return true;
}


//Main logic thread
document.getElementById("first_guess").onclick = function(){

    let numFingers = document.forms["first_game"]["number_select"].value;
    let guessCount = makeGuesses(numFingers);
}

document.getElementById("second_guess").onclick = function(){
    let numFingers = document.forms["second_game"]["number_input"].value;
    numFingers = parseInt(numFingers);
    console.log(numFingers)

    if (isNaN(numFingers)){
        window.alert("That's not a number, you can find the number keys above the letters");
        return;
    } else if (!validationIsInRange(numFingers,0,5)){
        window.alert("I don't know if you've got some hideous deformity, or if you just can't count, but I'm concerned either way, try a normal number of fingers")
        return;
    }

    let guessCount = makeGuesses(numFingers);
}

const SWAP_CHANCE = 0.1;
let letters;

window.onload = function(){
    letters = document.getElementsByClassName("js_letter");
    console.log(letters);
    setInterval(changeLetters, 300);
}
