(function() {
    const sliders = [...document.querySelectorAll('.slider__body')];
    const arrowNext = document.querySelector('#next');
    const arrowBefore = document.querySelector('#before');
    const swiper = document.querySelectorAll('.slide__swiper');
    let value = 0;

    /* funcionamiento de las flechas del slider */
    arrowNext.addEventListener('click', ()=> changePosition(1));
    arrowBefore.addEventListener('click', ()=>changePosition(-1));

    /* funcionamiento del cambio de slider */
    function changePosition(change) {
        const currentElement = Number(document.querySelector('.slider__body-show').dataset.id);
    
        value = currentElement;
        value += change;
    
        if(value === 0 || value == sliders.length + 1) {
            value = value === 0 ? sliders.length : 1;
        }
    
        sliders[currentElement-1].classList.toggle('slider__body-show');
        sliders[value-1].classList.toggle('slider__body-show');

        /* swiper */
        for (let i = 0; i < swiper.length; i++) {
        swiper[i].className = swiper[i].className.replace(" active", ""); 
        }

        swiper[value - 1].className += " active";
    }

    /* slider automatico */
    setInterval(changePosition, 10000, 1);
})()

