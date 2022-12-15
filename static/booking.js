let messageBlock=document.querySelector(".messageBlock");
let attractionNameContent=document.querySelector(".attractionNameContent");
let orderDateContent=document.querySelector(".orderDateContent");
let orderTimeContent=document.querySelector(".orderTimeContent");
let orderFeeContent=document.querySelector(".orderFeeContent");
let orderAddressContent=document.querySelector(".orderAddressContent");
let imageBlock=document.querySelector(".imageBlock");
let bookingTotalPrice=document.querySelector(".bookingTotalPrice");
let trashcan=document.querySelector(".trashcan");



//check cookie status
function checkBookingToken(){
    let url="/api/user/auth";
    fetch(url,{
        method:"GET",
    }).then(function(response){
        //packing and return to Backend
        return response.json();
    }).then(function(data){
        // console.log("取得後端token資料",data);
        if(data["data"]!=null){
            // console.log("目前為登入狀態");
            // SigninRegister.style.display="none";
            // SignOut.style.display="flex";
        }
        else{
            // console.log("非登入狀態");
            let url="/"
            window.location.href = url;
        }
    })
}
// // checkBookingToken();


//listener reflash
window.addEventListener("load", function() {
    // console.log("抓到你刷新頁面了吧，讓我檢查看看Token");
    checkBookingToken();

});






let username="";
function getBookingData(){
    fetch("/api/booking",{
        method:"GET",
    }).then(function(response){
        //packing and return to Backend
        return response.json();
    }).then(function(data){
        console.log("GET",data);
        console.log("-----------");
        if(data["data"]!=null){
            username=data["username"];
            messageBlock.textContent="你好，"+data["username"]+"，待預定的行程如下 :";
            attractionNameContent.textContent=data["data"]["attraction"]["name"];
            orderDateContent.textContent=data["data"]["date"];
            if(data["data"]["time"]=="morning"){
                orderTimeContent.textContent="早上 9 點到下午 4 點";
                orderFeeContent.textContent=data["data"]["price"];
                bookingTotalPrice.textContent=data["data"]["price"];
            }
            else{
                orderTimeContent.textContent="下午 4 點到晚上 8 點";
                orderFeeContent.textContent=data["data"]["price"];
                bookingTotalPrice.textContent=data["data"]["price"];
            }
            orderAddressContent.textContent=data["data"]["attraction"]["address"];
            imageBlock.setAttribute('src',data["data"]["attraction"]["image"]);

            //set ID for trashcan
            trashcan.setAttribute('id',data["data"]["attraction"]["id"]);

        }
        else{
            console.log("none");
            username=data["username"];
            console.log(username);
            displayNone();
        }
        
    })
}
getBookingData();





// // // // let messageDownBlock=document.querySelector(".messageDownBlock");



trashcan.addEventListener('click',function(){
    // console.log("just delete");
    // console.log(trashcan.getAttribute("id"));
    attractionId={"attractionId":(trashcan.getAttribute("id"))}
    // console.log(attractionId);
    deleteBooking(attractionId);
    // messageDownBlock.style.display="none";
})


function deleteBooking(){
    fetch(("/api/booking"),{
        method:"DELETE",
        body:JSON.stringify(attractionId),
        headers:new Headers({
            "content-type":"application/json"
        })
    }).then(function(){
        //packing and return to Backend
        console.log("delete Done");
        // return response.json();
        // displayNone();
    }).then(function(){
        //packing and return to Backend
        console.log("delete Done");
        // return response.json();
        displayNone();
    })
}




let mainBefore=document.querySelector(".mainBefore");
let mainAfter=document.querySelector(".mainAfter");
let footerBefore=document.querySelector(".footerBefore");
mainAfter.style.display="none";
let footerAfter=document.querySelector(".footerAfter");
// let introduceContent=document.querySelector(".introduceContent");
// let messageDownBlock=document.querySelector(".messageDownBlock");
// let bookingConnection=document.querySelector(".bookingConnection");
//下面不見
function displayNone(){
    mainBefore.style.display="none";
    mainAfter.style.display="block";
    footerBefore.style.display="none";
    footerAfter.style.display="block";
    // let newMessageBlock=document.getElementsByClassName(".messageBlock");
    let newMessageBlock=document.querySelectorAll(".messageBlock");
    // console.log(newMessageBlock[0]);
    // console.log(newMessageBlock[1]);
    // newMessageBlock.innerHTML="你好";
    newMessageBlock[1].textContent="你好，"+username+"，待預定的行程如下 :";

}

