let counter = 0;



function count() {
    console.log('counter');
    counter++;
    document.querySelector('h1').innerHTML = counter; 
    document.querySelector('title').innerHTML = `Counter ${counter}`;
    console.log('counter');
    if (counter % 10 === 0) {
        alert(`Hehe it's ${counter}`);
    }
}

document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('button').onsubmit = count;
    console.log(counter);

 })
