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
        } else {
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
let intervalValue = 1000;
function changeInterval() {
    const intervalInput = document.getElementById('durationInput');
    intervalValue = intervalInput.value;

    // Проверяем, является ли введенное значение числом больше 0
    if (!isNaN(intervalValue) && intervalValue > 0) {

        // Если уже есть интервал, очищаем его перед установкой нового
        if (intervalID) {
            clearInterval(intervalID);
        }

        // Устанавливаем новый интервал изменения изображений
        intervalID = setInterval(changeImage, intervalValue);
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
intervalID = setInterval(changeImage, intervalValue);

function startInterval() {
    // Проверка фокуса страницы при установке интервала
    if (!document.hasFocus()) {
        return; // Не устанавливаем интервал, если страница не в фокусе
    }
    // Если уже есть интервал, очищаем его перед установкой нового
    if (intervalID) {
        clearInterval(intervalID);
    }
    intervalID = setInterval(changeImage, intervalValue);
}

function stopInterval() {
    clearInterval(intervalID);
}

// Обработчики событий focus и blur
window.addEventListener('focus', startInterval);
window.addEventListener('blur', stopInterval);

window.addEventListener("DOMContentLoaded", (event) => {
    const el = document.getElementById('changeDuration');
    if (el) {
      el.addEventListener('click', changeInterval, false);
    }
});

const resultDiv = document.getElementById('resultDate');
let birthdateInput;
window.addEventListener("DOMContentLoaded", (event) => {
    const el = document.getElementById('birthdate');
    if (el) {
      el.addEventListener('change', checkDateBirth, false);
      birthdateInput = el;
    }
});


function checkDateBirth() {
    const birthdate = new Date(birthdateInput.value);
    const currentDate = new Date();
    const age = currentDate.getFullYear() - birthdate.getFullYear();
    birthdate.setFullYear(currentDate.getFullYear());
    if (currentDate < birthdate) {

    }
    const dayOfWeek = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'][birthdate.getDay()];

    let message = `Ваш возраст: ${age} лет.<br> День недели вашей даты рождения: ${dayOfWeek}.`;

    if (age >= 18) {
        message += ' Добро пожаловать!';
    } else {
        message += ' Вы несовершеннолетний. Для использования сайта необходимо разрешение родителей.';
        alert('Для использования сайта необходимо разрешение родителей.');
    }

    resultDiv.innerHTML = message;
}

var cards = document.getElementsByClassName('card');

// Используем стандартный цикл для перебора элементов
for (var i = 0; i < cards.length; i++) {
    // Добавляем обработчики событий для каждой карточки
    cards[i].addEventListener("mouseover", function(event) {
        var cardTitle = this.querySelector('.card-title');
        var cardDesc = this.querySelector('.card-desc');
        var cardMiddle = this.querySelector('.card-mid');
        var cardMiddleHeight = cardTitle.offsetHeight + cardDesc.offsetHeight;
        cardMiddle.style.height = cardMiddleHeight + 15 + "px";
    }, false);

    cards[i].addEventListener("mouseout", function(event) {
        var cardDomMiddle = this.querySelector('.card-mid');
        cardDomMiddle.style.height = 50 + "px";
    }, false);
}


// Функция для запуска обратного отсчета
function startCountdown() {
    const countdownDiv = document.getElementById('countdown');
    const expirationTime = localStorage.getItem('expirationTime');

    if (expirationTime) {
        const now = new Date().getTime();
        const timeLeft = new Date(expirationTime) - now;

        if (timeLeft > 0) {
            const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

            countdownDiv.innerHTML = `Осталось времени: ${minutes} минут ${seconds} секунд`;
        } else {
            countdownDiv.innerHTML = 'Время вышло';
            localStorage.removeItem("expirationTime");
        }
    } else {
        const now = new Date().getTime();
        const expirationTime = new Date(now + 3600000); // 1 час в миллисекундах
        localStorage.setItem('expirationTime', expirationTime.toString());
        startCountdown();
    }
}

startCountdown();

// Обновление таймера каждую секунду
setInterval(startCountdown, 1000);
