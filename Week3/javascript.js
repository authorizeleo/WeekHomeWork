const Hamburger = document.querySelector(".Hamberger")
const nav = document.querySelector(".nav")
const button = document.getElementById("loadbutton")
Hamburger.addEventListener("click",()=>{
    Hamburger.classList.toggle("open")
    nav.classList.toggle("open")
})

let proxy = "https://cors-anywhere.herokuapp.com/";
let api = "https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire"

let desk = new XMLHttpRequest()

desk.open("GET", proxy + api, true)
desk.send()
desk.onload = function(){

    let data = JSON.parse(this.responseText);
    console.log(data["result"]['results'])
    let dist ;
    let IgSrc;
    for(let x = 0 ; x < 8 ; x ++){
        dist = data["result"]['results'][x]["stitle"]
        IgSrc = data["result"]['results'][x]["file"]
        first = IgSrc.split(".jpg")[0]
        show(dist, first)
    }
    function img(g){
        for(let y = g; y < g + 8 ; y++ ){
            dist = data["result"]['results'][y]["stitle"]
            IgSrc = data["result"]['results'][y]["file"]
            first = IgSrc.split(".jpg")[0]
            show(dist, first)
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
    cell.className = 'mainItem'
    cell.textContent = "hello world;"
    imgBox.src = src + ".jpg"
    imgBox.alt ="死圖"
    const list = document.getElementById("mainAll")
    list.appendChild(cell)
    cell.appendChild(imgBox)
    cell.appendChild(h1)
}

