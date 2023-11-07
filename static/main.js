// Quiz data (questions are shuffled)
const quizData = [
  {
    question: "What does DevSecOps primarily focus on?",
    options: ["Development security", "DevOps processes", "Security collaboration", "Scalability"],
    answer: "Development security",
  },
  {
    question: "In DevSecOps, security is integrated into which phase of the software development lifecycle?",
    options: ["Planning", "Coding", "Testing", "All of the above"],
    answer: "All of the above",
  },
  {
    question: "What is the goal of secure code analysis in DevSecOps?",
    options: ["To identify and fix security vulnerabilities early", "To speed up development", "To improve user experience", "To reduce infrastructure costs"],
    answer: "To identify and fix security vulnerabilities early",
  },
  {
    question: "Which tool is used for scanning container images for security vulnerabilities?",
    options: ["Clair", "Jenkins", "SonarQube", "OWASP ZAP"],
    answer: "Clair",
  },
  {
    question: "What is the practice of automatically identifying and responding to security incidents in DevSecOps?",
    options: ["Security Automation", "Incident Response", "Security Monitoring", "Continuous Integration"],
    answer: "Security Automation",
  },
  {
    question: "What is the primary purpose of penetration testing in DevSecOps?",
    options: ["To identify and fix security vulnerabilities", "To automate software deployments", "To monitor system performance", "To improve user experience"],
    answer: "To identify and fix security vulnerabilities",
  },
  {
    question: "Which DevSecOps principle emphasizes that security should be part of the development process from the beginning?",
    options: ["Shift Left", "Collaboration", "Automation", "Scalability"],
    answer: "Shift Left",
  },
  // Add more DevSecOps-related questions here
];

// Personalized messages for the result
const resultMessages = {
  0: "You can do better next time!",
  1: "Nice try!",
  2: "Good job!",
  // Add more messages as needed
};

// Initialize quiz variables
let currentQuestionIndex = 0;
let score = 0;
let timer;
let totalTime = 0;

// Function to shuffle the order of questions
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

// Shuffle the order of questions
shuffleArray(quizData);

// Function to start the timer for each question
function startTimer() {
  timer = setInterval(() => {
    totalTime++;
  }, 1000); // Update time every second (1000 ms)
}

// Function to stop the timer
function stopTimer() {
  clearInterval(timer);
}

// Function to load and render the current question
function loadQuestion() {
  const currentQuestion = quizData[currentQuestionIndex];
  const questionText = document.querySelector(".question-text");
  const optionsContainer = document.querySelector(".options-container");
  const progressBar = document.getElementById("progress-bar");

  questionText.textContent = currentQuestion.question;
  optionsContainer.innerHTML = "";

  // Update progress bar
  const progressPercentage = (currentQuestionIndex / quizData.length) * 100;
  progressBar.style.width = progressPercentage + "%";

  currentQuestion.options.forEach((option, index) => {
    const optionButton = document.createElement("button");
    optionButton.textContent = option;
    optionButton.onclick = () => checkAnswer(option);
    optionsContainer.appendChild(optionButton);
  });

  // Start the timer for this question
  startTimer();
}

// Function to check the user's answer
function checkAnswer(selectedOption) {
  stopTimer(); // Stop the timer when an answer is selected
  const currentQuestion = quizData[currentQuestionIndex];
  if (selectedOption === currentQuestion.answer) {
    score++;
  }

  currentQuestionIndex++;
  if (currentQuestionIndex < quizData.length) {
    startTimer(); // Start the timer for the next question
    loadQuestion();
  } else {
    displayResult();
  }
}

// Function to display the user's score and a message
function displayResult() {
  const resultContainer = document.getElementById("result");
  const scoreMessage = resultMessages[score] || "Congratulations!";
  resultContainer.innerHTML = `You scored ${score} out of ${quizData.length}! ${scoreMessage} Total time taken: ${totalTime} seconds`;
  resultContainer.classList remove("hidden");
  document.getElementById("next-button").style.display = "none";
}

// Function to move to the next question
function nextQuestion() {
  if (currentQuestionIndex < quizData.length) {
    loadQuestion();
  }
}

// Initial load of the first question
loadQuestion();
