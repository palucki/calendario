const openModalButtons = document.querySelectorAll('[data-modal-target]')
const closeModalButtons = document.querySelectorAll('[data-close-button]')
const overlay = document.getElementById('overlay')

function setCountdown(element) {
  const countDown = new Date(element.dataset.availableAt * 1000).getTime()

  const second = 1000,
    minute = second * 60,
    hour = minute * 60,
    day = hour * 24;

  const x = setInterval(function () {
    const now = new Date().getTime(), distance = countDown - now;
    const days = Math.floor(distance / (day))
    const hours = Math.floor((distance % (day)) / (hour))
    const minutes = Math.floor((distance % (hour)) / (minute))
    const seconds = Math.floor((distance % (minute)) / second)

    //do something later when date is reached
    if (distance < 0) {
      element.innerText = "dostępne"
      clearInterval(x)
      return
    } 

    timeleft = "dostępne za "
    timeleft += days + " dni "
    timeleft += hours + " godzin "
    timeleft += minutes + " minut "
    timeleft += seconds + " sekund "
    element.innerText = timeleft

  }, 0)
}

const countdowns = document.querySelectorAll('[data-available-at]')
countdowns.forEach(p => {
  setCountdown(p)

})

openModalButtons.forEach(button => {
  button.addEventListener('click', () => {
    const modal = document.querySelector(button.dataset.modalTarget)
    openModal(modal)
  })
})

overlay.addEventListener('click', () => {
  const modals = document.querySelectorAll('.modal.active')
  modals.forEach(modal => {
    closeModal(modal)
  })
})

closeModalButtons.forEach(button => {
  button.addEventListener('click', () => {
    const modal = button.closest('.modal')
    closeModal(modal)
  })
})

function openModal(modal) {
  if (modal == null)
  {
    console.log("EMPTY")
    return
  }
  modal.classList.add('active')
  overlay.classList.add('active')
}

function closeModal(modal) {
  if (modal == null) return
  modal.classList.remove('active')
  overlay.classList.remove('active')
}

// function myFunction(elem) {
//     alert(elem.id);
// }

// const openBtn = document.getElementById('openModalBtn');
// const closeBtn = document.getElementById('closeModalBtn');
// const modal = document.getElementById('modal');

// openBtn.addEventListener('click', () => {
//     modal.classList.add('open');
// });

// closeBtn.addEventListener('click', () => {
//     modal.classList.remove('open');
// });

