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