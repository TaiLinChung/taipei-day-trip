//  全域變數
//getUrl/<id>
let urlAttraction="";
let urlModel="/api";
urlAttraction=urlModel+location.pathname
// console.log('location.href: '+location.href);
// console.log('location.pathname: '+(urlModel+location.pathname));

//sectionLeft
let imgBackground=document.querySelector(".imgBackground");
let imgBackgroundList=[];
let imgAmounts=0;

//sectionRight
let attractionName=document.querySelector(".attractionName");
let attractionSort=document.querySelector(".attractionSort");
let dateIn=document.querySelector(".dateIn");
let Btnmorning=document.querySelector(".Btnmorning");
let Btnnoon=document.querySelector(".Btnnoon");
let fee=document.querySelector(".fee");

let describe=document.querySelector(".describe");
let address=document.querySelector(".address");
let transport=document.querySelector(".transport");



//goBackToHome
let goBackToHome=document.querySelector(".leftBar");
goBackToHome.addEventListener('click',function(e){
    let url="/"
    window.location.href = url;
},false)



//Price of morning & noon 
Btnmorning.addEventListener('click',function(e){
    fee.textContent="新台幣 2000 元"
},false)
Btnnoon.addEventListener('click',function(e){
    fee.textContent="新台幣 2500 元"
},false)



//getAttractionDatas
//urlAttraction=urlModel+"{id}"
function getAttractionData(){
    fetch(urlAttraction).then(function(response){
        return response.json();
    }).then(function(data){
        // console.log(data["data"]["images"][0]);
        imgBackgroundList=data["data"]["images"]
        console.log(imgBackgroundList);
        imgBackground.setAttribute('src',imgBackgroundList[0]);
        // console.log(data["data"]);
        attractionName.textContent=data["data"]["name"];
        attractionSort.textContent=(data["data"]["category"]+"at"+data["data"]["mrt"])
        describe.textContent=data["data"]["description"];
        address.textContent=data["data"]["address"];
        transport.textContent=data["data"]["transport"];
        carouselFunction();
        // apple();

    })
}
getAttractionData();



//carouselfunction
// let carouseBlackPoint="";
let carousePosition=0;
let eachCarouselInturnID=0;
function carouselFunction(){
    carousePosition=0;
    console.log(carousePosition);
    imgAmounts=imgBackgroundList.length;
    console.log(imgAmounts);
    //createBlackPoint
    let carouselUnderBlock=document.querySelector(".carouselUnderBlock");
    for(let i=0;i<imgAmounts;i++){
        let carouselInturn=document.createElement('div');
        carouselInturn.setAttribute('class','carouselInturn');
        //carouselInturn add id attribute by img position
        carouselInturn.setAttribute('id',i);
        let carouselInturnshow=document.createElement('div');
        carouselInturnshow.setAttribute('class','carouselInturnshow');
        //carouselInturnshow add id attribute by img position
        carouselInturnshow.setAttribute('id',i);
        carouselInturn.appendChild(carouselInturnshow);
        carouselUnderBlock.appendChild(carouselInturn);
        //set listener to each BlackPointBlock
        eachCarouselInturnID=i;
        setListenerforEachCarouselInturn();
    }
    //Default Black Point show the first one
    let carouseBlackPoint=document.querySelectorAll(".carouselInturnshow");
    carouseBlackPoint[0].style.display="block";

    //BtnLeft
    let BtnLeft=document.querySelector(".carouselBtnleft");
    BtnLeft.addEventListener('click',function(e){
        carousePosition-=1
        carouseReturnJudge();
        setBlackPoint();
        console.log("left");
        console.log(carousePosition);
    },false)

    //BtnRight
    let BtnRight=document.querySelector(".carouselBtnright");
    BtnRight.addEventListener('click',function(e){       
        carousePosition+=1
        carouseReturnJudge();
        setBlackPoint();
        console.log("right");
        console.log(carousePosition);
    },false)
}



//ReturnJudge
function carouseReturnJudge(){
    if(carousePosition<0){
        carousePosition=imgAmounts-1;
    }
    else if(carousePosition==imgAmounts){
        carousePosition=0;
    }
}



//  displayNoneBlackPoint and set the BlackPoint
function setBlackPoint(){
    //  displayNoneBlackPoint
    let carouseBlackPoint=document.querySelectorAll(".carouselInturnshow");
    let length=carouseBlackPoint.length;
    for(let i=0;i<length;i++){
        carouseBlackPoint[i].style.display="none";
    }
    // console.log("我在這",carousePosition);
    //  set the position
    carouseBlackPoint[carousePosition].style.display="block";
    imgBackground.setAttribute('src',imgBackgroundList[carousePosition]);
}




//替每個白球設置監聽事件----------
function setListenerforEachCarouselInturn(){
    let CarouselInturnListener=document.getElementById(eachCarouselInturnID);
    CarouselInturnListener.onclick=function(event){
        // console.log(event);
        //All blackPoints display:none
        //the new position
        carousePosition=Number(event.target.id);
        // console.log(typeof(carousePosition));
        setBlackPoint();
    }
}










//-----------------------------------------------

// let positionapple=0;
// function apple(){
//     //imgBackgroundList
//     console.log(imgBackgroundList);
//     // console.log(imgBackgroundList[0]);
//     // console.log(imgBackgroundList.length);
//     // console.log(positionapple);
    
//     let left=document.querySelector(".carouselBtnleft");
//     left.addEventListener("click",function(){
//         positionapple-=1;
//         console.log(positionapple);
//         // console.log(imgBackgroundList[positionapple]);

//     },false)

//     let right=document.querySelector(".carouselBtnright");
//     right.addEventListener("click",function(){
//         positionapple+=1;
//         console.log(positionapple);
//         // console.log(imgBackgroundList[positionapple]);

//     },false)
// }

