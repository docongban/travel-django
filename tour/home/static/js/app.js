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


// bot chat
class Chatbox {
  constructor() {
      this.args = {
          openButton: document.querySelector('.chatbox__button'),
          chatBox: document.querySelector('.chatbox__support'),
          sendButton: document.querySelector('.send__button')
      }

      this.state = false;
      this.messages = [];
  }

  display() {
      const {openButton, chatBox, sendButton} = this.args;

      openButton.addEventListener('click', () => this.toggleState(chatBox))

      sendButton.addEventListener('click', () => this.onSendButton(chatBox))

      const node = chatBox.querySelector('input');
      node.addEventListener("keyup", ({key}) => {
          if (key === "Enter") {
              this.onSendButton(chatBox)
          }
      })
  }

  toggleState(chatbox) {
      this.state = !this.state;

      // show or hides the box
      if(this.state) {
          chatbox.classList.add('chatbox--active')
      } else {
          chatbox.classList.remove('chatbox--active')
      }
  }

  onSendButton(chatbox) {
      var textField = chatbox.querySelector('input');
      let text1 = textField.value
      if (text1 === "") {
          return;
      }

      let msg1 = { name: "User", message: text1 }
      this.messages.push(msg1);

      fetch('http://127.0.0.1:5000/predict', {
          method: 'POST',
          body: JSON.stringify({ message: text1 }),
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json'
          },
        })
        .then(r => r.json())
        .then(r => {
          let msg2 = { name: "Sam", message: r.answer };
          this.messages.push(msg2);
          this.updateChatText(chatbox)
          textField.value = ''

      }).catch((error) => {
          console.error('Error:', error);
          this.updateChatText(chatbox)
          textField.value = ''
        });
  }

  updateChatText(chatbox) {
      var html = '';
      this.messages.slice().reverse().forEach(function(item, index) {
          if (item.name === "Sam")
          {
              html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
          }
          else
          {
              html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
          }
        });

      const chatmessage = chatbox.querySelector('.chatbox__messages');
      chatmessage.innerHTML = html;
  }
}


const chatbox = new Chatbox();
chatbox.display();