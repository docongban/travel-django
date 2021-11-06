//Slider
const slider=document.querySelector('.slider')
const sliderMain = document.querySelector('.slider-main')
const sliderItems = document.querySelectorAll('.slider-item')
const nextBtn = document.querySelector('.slider-right')
const prevBtn = document.querySelector('.slider-left')
const sliderItemWidth = sliderItems[0].offsetWidth
const numberOfSliderItems = sliderItems.length 

var slideNumber = 0

//Next Slider
nextBtn.addEventListener('click',() => {
  slideNumber++;
  
  if(slideNumber > (numberOfSliderItems-1) ){
      slideNumber = 0;
  }

  sliderMain.style.left = "-"+sliderItemWidth*slideNumber+"px"
})

//Prev Slider
prevBtn.addEventListener('click',() => {
  slideNumber--;
  
  if(slideNumber < 0){
      slideNumber = numberOfSliderItems-1;
  }

  sliderMain.style.left = "-"+sliderItemWidth*slideNumber+"px"
})

//Auto Play
var playSlider;
var auto = () => {
  playSlider = setInterval(() =>{
      slideNumber++;
      
      if(slideNumber > (numberOfSliderItems-1) ){
          slideNumber=0;
      }
  
      sliderMain.style.left = "-"+sliderItemWidth*slideNumber+"px"
  }, 5000)
}
auto()

// auto increment counter
const total = document.querySelector('#counter-total')
const tour = document.querySelector('#counter-tour')
const happy = document.querySelector('#counter-happy')

function animateNumber(finalNumber, delay, startNumber = 0, callback) {
    let currentNumber = startNumber
    const interval = window.setInterval(updateNumber, delay)
    function updateNumber() {
      if (currentNumber >= finalNumber) {
        clearInterval(interval)
      } else {
        currentNumber++
        callback(currentNumber)
      }
    }
  }
  
document.addEventListener('DOMContentLoaded', function () {
    animateNumber(378, 10, 0, function (number) {
      const formattedNumber = number.toLocaleString()
      total.innerText = formattedNumber
    })
    
    animateNumber(30, 100, 0, function (number) {
      const formattedNumber = number.toLocaleString()
      tour.innerText = formattedNumber
    })
    
    animateNumber(2263, 5, 0, function (number) {
      const formattedNumber = number.toLocaleString()
      happy.innerText = formattedNumber
    })
})