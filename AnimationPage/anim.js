//  Animax Web App Funtions


// Landing Page Animation

window.addEventListener('load', function () {

    // Landing Page Animation Function

    var btn = document.getElementById('playRotate');
    btn.onclick = function (e) {
        document.getElementById("rotate").classList.add('rotate');
        setTimeout(function () {
            document.getElementById("rotate").classList.remove('rotate');
        }, 5000);
    }

    var btn1 = document.getElementById('playBounce');
    btn1.onclick = function (e) {
        document.getElementById("bounce").classList.add('bounce');
        setTimeout(function () {
            document.getElementById("bounce").classList.remove('bounce');
        }, 5000);
    }

    var btn2 = document.getElementById('playFade');
    btn2.onclick = function (e) {
        document.getElementById("fade-in-out").classList.add('fade-in-out');
        setTimeout(function () {
            document.getElementById("fade-in-out").classList.remove('fade-in-out');
        }, 5000);
    }

    var btn3 = document.getElementById('playAlt');
    btn3.onclick = function (e) {
        document.getElementById("alternate-colour").classList.add('alternate-colour');
        setTimeout(function () {
            document.getElementById("alternate-colour").classList.remove('alternate-colour');
        }, 5000);
    }
})

// Animation Page Function

// Bounce

const animB = document.getElementById('bounce-1x');
const rangeB1 = document.getElementById('delay-range');
rangeB1.addEventListener('input', () => {
    animB.style.animationDelay = rangeB1.value + 's';
    console.log(rangeB1.value);
})
const modeB = document.getElementById('play-mode');
modeB.addEventListener('change', () => {
    animB.style.animationPlayState = modeB.value;
    console.log(modeB.value);
})
const vectorB = document.getElementById('direction');
vectorB.addEventListener('change', () => {
    animB.style.animationDirection = vectorB.value;
    console.log(vectorB.value);
})
const timeB = document.getElementById('timing-function');
timeB.addEventListener('change', () => {
    animB.style.animationTimingFunction = timeB.value;
    console.log(timeB.value);
})
const iterB = document.getElementById('iteration');
iterB.addEventListener('change', () => {
    animB.style.animationIterationCount = iterB.value;
    console.log(iterB.value);
})
const rangeB = document.getElementById('duration-range');
rangeB.addEventListener('input', () => {
    animB.style.animationDuration = rangeB.value + 's';
    code.innerText = `'Duration: 1 + ${rangeB.value} + 's' + 'Timing-Function: ' + ${timeB.value}`;

    console.log(rangeB.value);
})
var checker = document.getElementById('infinite');

checker.addEventListener('change', () => {
    if (checker.checked) {
        console.log(checker.checked);
        animB.style.animationIterationCount = 'infinite';
    }
    else {
        animB.style.animationIterationCount = iterBN.value;
    }
})


// Bounce Natural

const code = document.getElementById('code-template');
const animBN = document.getElementById('bounce-natural');
// const animF = document.getElementById('fade-in');
// const animBL = document.getElementById('blink');
// const animR = document.getElementById('spin');
// const animP = document.getElementById('pulse');
// const animH = document.getElementById('heartbeat');
// const animSQ = document.getElementById('squash-and-stretch');



const rangeBN1 = document.getElementById('delay-range');
rangeBN1.addEventListener('input', () => {
    animBN.style.animationDelay = rangeBN1.value + 's';
    console.log(rangeBN1.value);
})
const modeBN = document.getElementById('play-mode');
modeBN.addEventListener('change', () => {
    animBN.style.animationPlayState = modeBN.value;
    console.log(modeBN.value);
})
const vectorBN = document.getElementById('direction');
vectorBN.addEventListener('change', () => {
    animBN.style.animationDirection = vectorBN.value;
    console.log(vectorBN.value);
})
const timeBN = document.getElementById('timing-function');
timeBN.addEventListener('change', () => {
    animBN.style.animationTimingFunction = timeBN.value;
    console.log(timeBN.value);
})
const iterBN = document.getElementById('iteration');
iterBN.addEventListener('change', () => {
    animBN.style.animationIterationCount = iterBN.value;
    console.log(iterBN.value);
})
const rangeBN = document.getElementById('duration-range');
rangeBN.addEventListener('input', () => {
    animBN.style.animationDuration = rangeBN.value + 's';
    code.innerText = `'Duration: 1 + ${rangeBN.value} + 's' + 'Timing-Function: ' + ${timeBN.value}`;
    console.log(rangeBN.value);
})
var checkbox = document.getElementById('infinite');
checkbox.addEventListener('change', () => {
    if (checkbox.checked) {
        console.log(checkbox.checked);
        animBN.style.animationIterationCount = 'infinite';
        animB.style.animationIterationCount = 'infinite';
    }
    else {
        animBN.style.animationIterationCount = iterBN.value;
        animB.style.animationIterationCount = iterBN.value;
    }
})



