function menu() {
    document.querySelector('.menu-line-1').classList.toggle('menu-1-active');
    document.querySelector('.menu-line-2').classList.toggle('menu-2-active');
    document.querySelector('.menu-line-3').classList.toggle('menu-3-active');

    document.querySelector('.menu').classList.toggle('menu-active')
}


var codeLink = document.querySelector(".code-link");

codeLink.addEventListener("mouseenter", popdown);


var codeLines = document.querySelectorAll(".codeline");

function popdown() {
    for (var i = 0; i < codeLines.length; i++) {
        var codeLine = codeLines[i];

        codeLine.keyframes = [{
            transform: "scale(100%)",
        }, {
            transform: "scale(120%)",
        }, {
            transform: "scale(0%)",
        }];

        codeLine.animProps = {
            fill: "forwards",
            duration: 500,
            easing: "ease-out",
            iterations: 1,
        }

        var animationPlayer = codeLine.animate(codeLine.keyframes, codeLine.animProps);
    }

    setTimeout(popup, 800); 
};

function popup() {
    var order = [1, 4, 8, 3, 6, 9, 2, 7, 5, 10];

    for (var i = 0; i < codeLines.length; i++) {
        var codeLine = codeLines[i];

        codeLine.keyframes = [{
            transform: "scale(0%)",
            offset: 0,
        },{
            transform: "scale(130%)",
            offset: 0.8,
        },{
            transform: "scale(100%)",
            offset: 1,
        }];


        codeLine.animProps = {
            fill: "forwards",
            duration: 750,
            easing: "ease-in",
            delay: 200 * order[i],
            iterations: 1
        }

        var animationPlayer = codeLine.animate(codeLine.keyframes, codeLine.animProps);
    }
}