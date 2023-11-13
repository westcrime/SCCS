var lastScrollTop = 0; // This Varibale will store the top position
navbar = document.getElementById('header'); // Get The NavBar
const car = document.getElementById('pink_car');
const smoke = document.getElementById('smoke');
car_is_crashed = false;
window.addEventListener('scroll',function(){
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    //This line will get the location on scroll
    if (car_is_crashed === false) {
        let value = scrollY;
        if (value >= 245) {
            car_is_crashed = true;
        }
        else {
            car.style.left = `+${value / 0.5}px`;
        }
    }
    if(scrollTop > lastScrollTop){ //if it will be greater than the previous
        navbar.style.top='-80px';
        //set the value to the negative of height of navbar
    }
    else{
        navbar.style.top='0';
    }

    lastScrollTop = scrollTop; //New Position Stored
});

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
       console.log(entry)
       if (entry.isIntersecting) {
            entry.target.classList.add('show');
       }
       else {
            entry.target.classList.remove('show');
       }
    });
});
const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => {
    observer.observe(el);
})


// Массив с путями к изображениям для смены
const images = [
    "static/images/ad1.png",
    "static/images/ad2.png",
    "static/images/ad3.png"
];

const hrefs = [
    "https://1xbet.by/",
    "https://youtube.com/",
    "https://github.com/"
];

let currentImageIndex = 0; // Начальный индекс изображения
let currentHrefIndex = 0; // Начальный индекс изображения
let intervalID; // Переменная для хранения ID интервала
function startInterval() {
    const intervalInput = document.getElementById('durationInput');
    const intervalValue = intervalInput.value;

    // Проверяем, является ли введенное значение числом больше 0
    if (!isNaN(intervalValue) && intervalValue > 0) {
        // Преобразуем введенное значение в миллисекунды (умножаем на 1000)
        const intervalInMillis = intervalValue * 1000;

        // Если уже есть интервал, очищаем его перед установкой нового
        if (intervalID) {
            clearInterval(intervalID);
        }

        // Устанавливаем новый интервал изменения изображений
        intervalID = setInterval(changeImage, intervalInMillis);
    } else {
        alert('Пожалуйста, введите корректное значение интервала (в миллисекундах)');
    }
}
function changeImage() {
    const adImage = document.getElementById('ad_img');
    const adHref = document.getElementById('ad_href');
    adImage.src = images[currentImageIndex]; // Устанавливаем новое изображение
    adHref.href = hrefs[currentHrefIndex];

    // Увеличиваем индекс изображения или сбрасываем, если достигли конца массива
    currentImageIndex = (currentImageIndex + 1) % images.length;
    currentHrefIndex = (currentHrefIndex + 1) % hrefs.length;
}
// Обработчик нажатия на кнопку "Установить интервал"
document.getElementById('changeDuration').addEventListener('click', startInterval);
intervalID = setInterval(changeImage, 1000);