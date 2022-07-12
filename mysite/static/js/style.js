const nameInput = document.querySelector("#name");
const email = document.querySelector("#name");
const message = document.querySelector("#name");
const success = document.querySelector("#name");
const errorm = document.querySelector("#name");

//validating the data

function validateForm() {
  if (nameInput.ariaValueMax.length < 1) {
    errorm[0].innerText = "Name cannot be blank";
    nameInput.classList.add("error-border");
  }
  
}