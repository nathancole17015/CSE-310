let character = document.getElementById("character")
let block = document.getElementById("block")
let scoreDisplay = document.getElementById("score")
let score = 0;


function jump() {
    if (character.classList != "animate") {
        character.classList.add("animate")
     }
    setTimeout(function(){
        character.classList.remove("animate")
    },500)
}
function updateScore(){
   score += 1/7 ;
   scoreDisplay.innerText = "Score: " + Math.floor(score);
}

function restartGame() {
    character.style.top = "150px";
    block.style.left = "480px";
    block.style.animation = "block 1s infinite linear";
    score = 0;
    scoreDisplay.innerText = "Score: 0";
    block.style.display = "block";

    
    clearInterval(hitBlock);
    hitBlock = setInterval(function () {

        var characterTop = parseInt(window.getComputedStyle(character).getPropertyValue("top"));
        var blockLeft = parseInt(window.getComputedStyle(block).getPropertyValue("left"));

        if (blockLeft < 0) {
            updateScore();
        }

        if (blockLeft < 20 && blockLeft > 0 && characterTop >= 130) {
            block.style.animation = "none";
            block.style.display = "none";
            alert("Caught! Game Over.");
            restartGame(); 
        }
    }, 10);
}


var hitBlock = setInterval(function() {
    var characterTop = parseInt(window.getComputedStyle(character).getPropertyValue("top"));
    var blockLeft = parseInt(window.getComputedStyle(block).getPropertyValue("left"));

    if (blockLeft < 0) {
        updateScore();
    }

    if (blockLeft < 20 && blockLeft > 0 && characterTop >= 130) {
        block.style.animation = "none";
        block.style.display = "none";
        alert("Caught! Game Over.");
        restartGame();
    }
}, 10);
