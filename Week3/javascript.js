const Hamburger = document.querySelector(".Hamberger")
const nav = document.querySelector(".nav")

let proxy = "https://cors-anywhere.herokuapp.com/";
let api = "https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire"

Hamburger.addEventListener("click",()=>{
    Hamburger.classList.toggle("open")
    nav.classList.toggle("open")
})

let desk = new XMLHttpRequest()

desk.open("GET", proxy + api, true)
desk.send()
desk.onload = function(){

    let data = JSON.parse(this.responseText);
    console.log(data["result"]['results'])
    let dist,IgSrc ;
    for(let x = 0 ; x < 8 ; x ++){
        dist = data["result"]['results'][x]["stitle"]
        IgSrc = data["result"]['results'][x]["file"]
        first = IgSrc.split(".jpg")[0]
        show(dist, first)
    }
    ClickHeader(()=>{
        for(let x = 8 ; x < 16 ; x ++){
            dist = data["result"]['results'][x]["stitle"]
            IgSrc = data["result"]['results'][x]["file"]
            first = IgSrc.split(".jpg")[0]
            show(dist, first)
    }})
}

document.body.onload = show()
function show(data,src){
    let cell = document.createElement('div');
    let imgBox = document.createElement('img') 
    let h1 = document.createElement('h1')
    h1.textContent = data
    cell.className = 'mainItem'
    cell.textContent = "hello world;"
    imgBox.src = src + ".jpg"
    const list = document.getElementById("mainAll")
    list.appendChild(cell)
    cell.appendChild(imgBox)
    cell.appendChild(h1)
}

// const button = document.getElementById("loadbutton")
// button.addEventListener("click", ClickHeader())