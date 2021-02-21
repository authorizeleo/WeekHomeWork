const Hamburger = document.querySelector(".Hamberger")
const nav =document.querySelector(".nav")


Hamburger.addEventListener("click",()=>{
    Hamburger.classList.toggle("open")
    nav.classList.toggle("open")
})