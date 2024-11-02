let timeLeft = document.querySelector(".time-left");
let quizContainer = document.getElementById("container");
let nextBtn = document.getElementById("next-button");
let countOfQuestion = document.querySelector(".number-of-question");
let displayContainer = document.getElementById("display-container");
let scoreContainer = document.querySelector(".score-container");
let restart = document.getElementById("restart");
let userScore = document.getElementById("user-score");
let startScreen = document.querySelector(".start-screen");
let startButton = document.getElementById("start-button");
let questionCount = 0;
let scoreCount = 0;
let count = 11;
let countdown;

// Questions array with sliders
const questions = [
    {
        question: "How are you feeling today?",
        options: [1, 2, 3, 4, 5]
    },
    {
        question: "How would you rate your energy levels?",
        options: [1, 2, 3, 4, 5]
    },
    {
        question: "How would you rate your stress level?",
        options: [1, 2, 3, 4, 5]
    }
];

/// Done Button - takes user to the home screen
doneButton.addEventListener("click", () => {
    // Redirect to the home screen (replace 'home.html' with your actual home page URL)
    window.location.href = 'homescreen.html';
});

});

// Next Button
nextBtn.addEventListener("click", () => {
    let selectedValue = document.getElementById("feeling-slider").value;

    // Increment score if response is above threshold
    if (selectedValue >= 4) {
        scoreCount++;
    }

    // Increment question count
    questionCount++;

    // If last question
    if (questionCount === questions.length) {
        displayContainer.classList.add("hide");
        scoreContainer.classList.remove("hide");
        userScore.innerHTML = "Your score is " + scoreCount + " out of " + questions.length;
    } else {
        // Display next question
        countOfQuestion.innerHTML = `Question ${questionCount + 1} of ${questions.length}`;
        displayQuestion(questionCount);
        count = 11;
        clearInterval(countdown);
        timerDisplay();
    }
});

// Timer
const timerDisplay = () => {
    countdown = setInterval(() => {
        count--;
        timeLeft.innerHTML = `${count}s`;
        if (count === 0) {
            clearInterval(countdown);
            nextBtn.click();
        }
    }, 1000);
};

// Display question
const displayQuestion = (questionCount) => {
    let currentQuestion = questions[questionCount];
    document.getElementById("question-text").innerText = currentQuestion.question;
    document.getElementById("feeling-slider").value = 3; // Reset slider
};

// Initial setup
function initial() {
    questionCount = 0;
    scoreCount = 0;
    count = 11;
    clearInterval(countdown);
    timerDisplay();
    displayQuestion(questionCount);
    countOfQuestion.innerHTML = `Question ${questionCount + 1} of ${questions.length}`;
}

// When user clicks on start button
startButton.addEventListener("click", () => {
    startScreen.classList.add("hide");
    displayContainer.classList.remove("hide");
    initial();
});

// Hide quiz and display start screen
window.onload = () => {
    startScreen.classList.remove("hide");
    displayContainer.classList.add("hide");
};
