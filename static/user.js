let SigninRegister=document.querySelector(".SigninRegister");
let filmBackground=document.querySelector(".filmBackground");
let signinBlock=document.querySelector(".signinBlock");
let signinCreateAccount=document.querySelector(".signinCreateAccount");
let registerBlock=document.querySelector(".registerBlock");
let registerSignInTo=document.querySelector(".registerSignInTo");
let signinClose=document.querySelector(".signinClose");
let registerClose=document.querySelector(".registerClose");


//listener
SigninRegister.addEventListener('click',function(){
    filmBackground.style.display="block";
    signinBlock.style.display="flex";
},false)

//listener
signinCreateAccount.addEventListener('click',function(){
    signinBlock.style.display="none";
    registerBlock.style.display="flex";
},false)

// listener
registerSignInTo.addEventListener('click',function(){
    registerBlock.style.display="none";
    signinBlock.style.display="flex";
},false)

// listener
signinClose.addEventListener('click',function(){
    close();
},false)

// listener
registerClose.addEventListener('click',function(){
    close();
},false)

function close(){
    signinBlock.style.display="none";
    registerBlock.style.display="none";
    filmBackground.style.display="none";
    registerMessage.style.display="none";
    registerContent.style.height="100%";
    document.querySelector(".registerName").value="";
    document.querySelector(".registerEmail").value="";
    document.querySelector(".registerPassword").value="";
}

//get register data
let registerName="";
let registerEmail="";
let registerPassword="";
let registerData={}
let registerBtn=document.querySelector(".registerBtn");
registerBtn.addEventListener('click',function(){
    registerName=document.querySelector(".registerName").value;
    registerEmail=document.querySelector(".registerEmail").value;
    registerPassword=document.querySelector(".registerPassword").value;
    registerData={"name":registerName,"email":registerEmail,"password":registerPassword};
    pushRegisterDataToBackEnd();
},false)


//post method to returndata to backend
let responseFromBackend=""
function pushRegisterDataToBackEnd(){
    fetch("/api/user",{
        method:"POST",
        credentials:"include",
        body:JSON.stringify(registerData),
        cache:"no-cache",
        headers:new Headers({
            "content-type":"application/json"
        })
    }).then(function(response){
        //packing and return to Backend
        return response.json();
    }).then(function(data){
        //getresponseFromBackend
        responseFromBackend=data;
        console.log(responseFromBackend);
        dealRegistResponseFromBackend();
    })
}


//the page of Register
let registerMessage=document.querySelector(".registerMessage");
let registerContent=document.querySelector(".registerContent");
function dealRegistResponseFromBackend(){
    registerContent.style.height="350px";
    registerMessage.style.display="flex";
    //換位置
    registerMessage.style.top="50px";
    registerSignInTo.style.top="100px";
    if(responseFromBackend["ok"]==true){
        console.log("註冊成功");
        registerMessage.textContent="註冊成功"
    }
    else{
        console.log("註冊失敗");
        registerMessage.textContent="註冊失敗，點此重新註冊"

        // listener
        registerMessage.addEventListener('click',function(){
            close();
            filmBackground.style.display="block";
            registerBlock.style.display="flex";
            registerContent.style.height="340px";
            registerSignInTo.style.top="70px";
        },false)
    }
}


//get signin data
let signinEmail="";
let signinPassword="";
let signinData={}
let signinBtn=document.querySelector(".signinBtn");
signinBtn.addEventListener('click',function(){
    signinEmail=document.querySelector(".signinEmail").value;
    signinPassword=document.querySelector(".signinPassword").value;
    signinData={"email":signinEmail,"password":signinPassword};
    console.log("註冊資料",signinData);
    pushSigninDataToBackEnd();
},false)


//get method to returndata to backend
function pushSigninDataToBackEnd(){
    fetch("/api/user/auth",{
        method:"PUT",
        credentials:"include",
        body:JSON.stringify(signinData),
        cache:"no-cache",
        headers:new Headers({
            "content-type":"application/json"
        })
    }).then(function(response){
        //packing and return to Backend
        return response.json();
    }).then(function(data){
        //getresponseFromBackend
        responseFromBackend=data;
        dealSigninResponseFromBackend();
        userStatus();
    })
}


//the page of signin
let signinContent=document.querySelector(".signinContent");
let signinMessage=document.querySelector(".signinMessage");
function dealSigninResponseFromBackend(){
    signinContent.style.height="290px";
    signinCreateAccount.style.top="90px";
    signinMessage.style.display="flex";
    if(responseFromBackend["ok"]==true){
        signinMessage.textContent="登入成功";
        //登入成功就做刷新頁面
        location.reload();
    }
    else{
        signinMessage.textContent="登入失敗";
    }
}

//listener reflash
window.addEventListener("load", function(event) {
    console.log("抓到你刷新頁面了吧，讓我檢查看看Token");
    userStatus()
});


let SignOut=document.querySelector(".SignOut");
//check cookie status
function userStatus(){
    let url="/api/user/auth";
    fetch(url,{
        method:"GET",
    }).then(function(response){
        //packing and return to Backend
        return response.json();
    }).then(function(data){
        console.log("取得後端token資料",data);
        // 如果回傳的token帶登入狀態 右上角改成登出字樣
        if(data["data"]!=null){
            console.log("目前為登入狀態");
            SigninRegister.style.display="none";
            SignOut.style.display="flex";
        }
        else{
            console.log("非登入狀態");
        }
    })
}


//listener execute signout
SignOut.addEventListener('click',function(){
    signinData={};
    // 原本
    // pushSigninDataToBackEnd();
    // 新的
    pushSignOutRequestToBackEnd()
    // location.reload();
},false)



//delete method to returndata to backend
function pushSignOutRequestToBackEnd(){
    fetch("/api/user/auth",{
        method:"DELETE",
        credentials:"include",
        body:JSON.stringify(signinData),
        cache:"no-cache",
        headers:new Headers({
            "content-type":"application/json"
        })
    }).then(function(response){
        //packing and return to Backend
        return response.json();
    }).then(function(){
        //confirm 後才reload
        location.reload();
    })
}

