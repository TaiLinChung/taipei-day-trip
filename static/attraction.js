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
const attractionName=document.querySelector(".attractionName");
const attractionSort=document.querySelector(".attractionSort");
let dateIn=document.querySelector(".dateIn");
const Btnmorning=document.querySelector(".Btnmorning");
const Btnnoon=document.querySelector(".Btnnoon");
const fee=document.querySelector(".fee");

let describe=document.querySelector(".describe");
let address=document.querySelector(".address");
let transport=document.querySelector(".transport");



// //goBackToHome
// let goBackToHome=document.querySelector(".leftBar");
// goBackToHome.addEventListener('click',function(){
//     let url="/"
//     window.location.href = url;
// },false)


//set the date of today
let Today=new Date();
// console.log("time is: ",Today.getFullYear(),Today.getMonth()+1,Today.getDate());
todayModel=String(Today.getFullYear())+"-"+String(Today.getMonth()+1)+"-"+String(Today.getDate())
// console.log(todayModel);
dateIn=document.querySelector(".dateIn");
dateIn.value=todayModel
dateIn.min=todayModel



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
        // console.log(imgBackgroundList);
        imgBackground.setAttribute('src',imgBackgroundList[0]);
        // console.log(data["data"]);
        attractionName.textContent=data["data"]["name"];
        attractionSort.textContent=(data["data"]["category"]+"at"+data["data"]["mrt"])
        describe.textContent=data["data"]["description"];
        address.textContent=data["data"]["address"];
        transport.textContent=data["data"]["transport"];
        carouselFunction();

    })
}
getAttractionData();



//carouselfunction
// let carouseBlackPoint="";
let carousePosition=0;
let eachCarouselInturnID=0;
function carouselFunction(){
    carousePosition=0;
    // console.log(carousePosition);
    imgAmounts=imgBackgroundList.length;
    // console.log(imgAmounts);
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
    const carouseBlackPoint=document.querySelectorAll(".carouselInturnshow");
    carouseBlackPoint[0].style.display="block";

    //BtnLeft
    const BtnLeft=document.querySelector(".carouselBtnleft");
    BtnLeft.addEventListener('click',function(e){
        carousePosition-=1
        carouseReturnJudge();
        setBlackPoint();
        // console.log("left");
        // console.log(carousePosition);
    },false)

    //BtnRight
    const BtnRight=document.querySelector(".carouselBtnright");
    BtnRight.addEventListener('click',function(e){       
        carousePosition+=1
        carouseReturnJudge();
        setBlackPoint();
        // console.log("right");
        // console.log(carousePosition);
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







// //------------------------------------------for booking

const orderBtn=document.querySelector(".orderBtn");
orderBtn.addEventListener('click',function(){
    checkAttractionToken();
},false)


//check cookie status
function checkAttractionToken(){
    let url="/api/user/auth";
    fetch(url,{
        method:"GET",
    }).then(function(response){
        return response.json();
    }).then(function(data){
        if(data.data === null){
            // console.log("請登入");
            const filmBackground=document.querySelector(".filmBackground");
            const signinBlock=document.querySelector(".signinBlock");
            filmBackground.style.display="block";
            signinBlock.style.display="flex";
        }else{
            bookingData=getDataForBooking();
            postBookingDataToBackEnd(bookingData);
        }
    })
}



function getDataForBooking(){
    let attractionUrl=String(window.location.pathname);
    let attractionId=attractionUrl.replace("/attraction/","");
    let attractionPrice=fee.textContent.replaceAll(" ","").replace("新台幣","").replace("元","");
    let time="";
    if(attractionPrice=="2000"){
        time="morning";
    }else{
        time="afternoon";
    }
    bookingData={
        "attractionId":attractionId,
        "date":dateIn.value,
        "price":attractionPrice,
        "time":time
    }
    return bookingData
}



//post method to Passdata to backend
const orderMessage=document.querySelector(".orderMessage");
function postBookingDataToBackEnd(bookingData){
    fetch("/api/booking",{
        method:"POST",
        body:JSON.stringify(bookingData),
        headers:new Headers({
            "content-type":"application/json"
        })
    }).then(function(response){
        return response.json();
    }).then(function(data){
        if (data["ok"]==true){
            orderMessage.style.display="block";
            orderMessage.textContent="資料填寫無誤";
            orderMessage.style.color="green";
            orderBtn.style.marginTop="10px";
            window.location.href = "/booking";
        }else{
            orderMessage.style.display="block";
            orderMessage.textContent=data["message"];
            orderMessage.style.color="red";
            orderBtn.style.marginTop="10px";
        }
    })
}