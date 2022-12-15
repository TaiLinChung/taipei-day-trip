
//BackToHome
let goBackToHome=document.querySelector(".nav-bar-left");
goBackToHome.addEventListener('click',function(){
    let url="/"
    window.location.href = url;
},false)

// //reserveJourney
// let goToBooking=document.querySelector(".reserveJourney");
// goToBooking.addEventListener('click',function(){
//     console.log("reserveJourney");
//     checkUserToken();
// },false)



// //check cookie status
// function checkUserToken(){
//     // let url="/api"+attractionUrl;
//     let url="/api/user/auth";
//     fetch(url,{
//         method:"GET",
//     }).then(function(response){
//         //packing and return to Backend
//         return response.json();
//     }).then(function(data){
//         console.log("取得後端token資料",data);
//         // statusResponse=data;
//         // console.log(statusResponse);
//         // 如果回傳的token帶登入狀態 右上角改成登出字樣
//         if(data["data"]!=null){
//             console.log("目前為登入狀態");
//             // SigninRegister.style.display="none";
//             // SignOut.style.display="flex";
//             window.location.href = "/booking";

//         }
//         else{
//             // console.log("booking非登入狀態");
//             filmBackground.style.display="block";
//             signinBlock.style.display="flex";
//             // let url="/"
//             // window.location.href = url;
//         }
//     })
// }







// let SignOut=document.querySelector(".SignOut");
// SignOut.addEventListener('click',function(){
//     // checkUserToken();
//     console.log("123");
// },false)