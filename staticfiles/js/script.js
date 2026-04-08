let menu = document.getElementById("menu");
let navbar = document.getElementById("navbar");

menu.onclick = () => {
    navbar.classList.toggle("active");
}

const btns = document.querySelectorAll(".nav-btn");
const slides = document.querySelectorAll(".video-slide");
const contents = document.querySelectorAll(".content");

var sliderNav = function(manual){

btns.forEach((btn)=>{
btn.classList.remove("active");
});

slides.forEach((slide)=>{
slide.classList.remove("active");
});

contents.forEach((content)=>{
content.classList.remove("active");
});

btns[manual].classList.add("active");
slides[manual].classList.add("active");
contents[manual].classList.add("active");

}

btns.forEach((btn,i)=>{
btn.addEventListener("click",()=>{
sliderNav(i);
});
});


const slider = document.getElementById('brandSlider');
let isDown = false;
let startX;
let scrollLeft;

slider.addEventListener('mousedown', (e) => {
  isDown = true;
  slider.classList.add('active');
  startX = e.pageX - slider.offsetLeft;
  scrollLeft = slider.scrollLeft;
});

slider.addEventListener('mouseleave', () => {
  isDown = false;
  slider.classList.remove('active');
});

slider.addEventListener('mouseup', () => {
  isDown = false;
  slider.classList.remove('active');
});

slider.addEventListener('mousemove', (e) => {
  if(!isDown) return;
  e.preventDefault();
  const x = e.pageX - slider.offsetLeft;
  const walk = (x - startX) * 2; //scroll-fast
  slider.scrollLeft = scrollLeft - walk;
});


document.addEventListener("DOMContentLoaded", () => {
    const slider = document.querySelector(".brand-slider");
    let scrollAmount = 0;
    const slideWidth = 150 + 30; // width + gap
    setInterval(() => {
        if (scrollAmount >= slider.scrollWidth - slider.clientWidth) {
            scrollAmount = 0;
        } else {
            scrollAmount += slideWidth;
        }
        slider.scrollTo({
            left: scrollAmount,
            behavior: "smooth"
        });
    }, 2000); // slide every 2 seconds
});
