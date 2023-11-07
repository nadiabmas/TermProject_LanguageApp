document.getElementById('quiz-form').addEventListener('submit', function(event) {
 event.preventDefault();

 let correctAnswers = 0;
 let answers = ['A', 'B', 'C'];

 for (let i = 0; i < answers.length; i++) {
    let answer = document.getElementsByName('question' + (i + 1))[0].value;
    if (answer === answers[i]) {
      correctAnswers++;
    }
 }

 let resultsDiv = document.getElementById('results');
 resultsDiv.innerHTML = 'You got ' + correctAnswers + ' out of ' + answers.length + ' correct.';
});