const Hamburger = document.querySelector(".Hamberger")
const nav = document.querySelector(".nav")
const button = document.getElementById("loadbutton")

Hamburger.addEventListener("click",()=>{
    Hamburger.classList.toggle("open")
    nav.classList.toggle("open")
})

// let proxy = "https://cors-anywhere.herokuapp.com/";
let api = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"

let connect = new XMLHttpRequest()

connect.open("GET",  api, true)
connect.send()
connect.onload = function(){
    let data = JSON.parse(this.responseText);
    // console.log(data["result"]['results'])
    let Attractions ;
    let IgSrc;

    for(let x = 0 ; x < 8 ; x ++){
        Attractions = data["result"]['results'][x]["stitle"]
        IgSrc = data["result"]['results'][x]["file"]
        first = IgSrc.split('http')[1]
        show(Attractions, first)
    }

    function img(g){
        for(let y = g; y < g + 8 ; y++ ){
            Attractions = data["result"]['results'][y]["stitle"]
            IgSrc = data["result"]['results'][y]["file"]
            first = IgSrc.split(`http`)[1]
            console.log(first)
            show(Attractions, first)
        }
    }
    
    let g = 0
    button.addEventListener("click", CK)
    function CK(){ 
       g += 8 
       img(g)  
    }
}


function show(data,src){
    let cell = document.createElement('div');
    let imgBox = document.createElement('img') 
    let h1 = document.createElement('h1')
    h1.textContent = data
    if (data.length > 13) {
        h1.style.fontSize = "15px"
    }
    cell.className = 'mainItem'
    imgBox.src =   "http" + src  
    imgBox.alt ="死圖"
    const list = document.getElementById("mainAll")
    list.appendChild(cell)
    cell.appendChild(imgBox)
    cell.appendChild(h1)
}

