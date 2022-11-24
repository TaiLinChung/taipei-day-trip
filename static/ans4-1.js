let button= document.querySelector(".more_button")

let clickCount = 0

button.addEventListener("click",function(){
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function(response){
        return response.json();
    }).then(function(data){
        let attractions = data["result"]["results"]
        let attractionImg = ""
        let attractionName =""
        clickCount ++

        for(let i = 2+8*clickCount ; i< 10+8*clickCount; i++){
            if(attractions[i] === undefined) {
                break
            }
            let more = document.createElement('div')
            more.setAttribute("class","eight_wrap_content")
            let position = document.querySelector(".eight_wrap")
            position.appendChild(more)

            attractionImg = attractions[i]["file"].split("https:")
            attractionImg.splice(0,1)

            attractionName = attractions[i]["stitle"]
            console.log(attractionName)

            let newImg = document.createElement("img")
            newImg.src = "https:"+attractionImg[0]
            console.log(newImg)

            let name = document.createElement("div")
            name.setAttribute("class",'eight_wrap_content_word')
            name.setAttribute("index",attractionName)

            let imgHomeEight = document.querySelectorAll(".eight_wrap_content")
            console.log(more)
            more.appendChild(newImg)
            more.appendChild(name)
        }
    })


})

DATA = [10,12]
console.log(DATA[2])