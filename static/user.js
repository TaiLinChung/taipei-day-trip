
//BackToHome
const navBackToHome=document.querySelector(".navBackToHome");
navBackToHome.addEventListener('click',function(){
    let url="/"
    window.location.href = url;
},false)


const navSignInRegiste=document.querySelector(".SigninRegister");
const filmBackground=document.querySelector(".filmBackground");
const signinPage=document.querySelector(".signinBlock");
const signinCreateAccount=document.querySelector(".signinCreateAccount");
const registePage=document.querySelector(".registerBlock");
const registerSignInTo=document.querySelector(".registerSignInTo");
const signinClose=document.querySelector(".signinClose");
const registerClose=document.querySelector(".registerClose");
const member=document.querySelector(".member");
member.style.display="none";
//listener
navSignInRegiste.addEventListener('click',function(){
    filmBackground.style.display="block";
    signinPage.style.display="flex";
},false)

//listener
signinCreateAccount.addEventListener('click',function(){
    signinPage.style.display="none";
    registePage.style.display="flex";
},false)

// listener
registerSignInTo.addEventListener('click',function(){
    registePage.style.display="none";
    signinPage.style.display="flex";
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
    signinPage.style.display="none";
    registePage.style.display="none";
    filmBackground.style.display="none";
    registerMessage.style.display="none";
    registerContent.style.height="322px";
    registerSignInTo.style.top="70px";
    document.querySelector(".registerName").value="";
    document.querySelector(".registerEmail").value="";
    document.querySelector(".registerPassword").value="";
}





// =================================      register    =================================
let registerData={};
const registerBtn=document.querySelector(".registerBtn");
registerBtn.addEventListener('click',function(){
    registerName=document.querySelector(".registerName").value;
    registerEmail=document.querySelector(".registerEmail").value;
    registerPassword=document.querySelector(".registerPassword").value;
    checkRegisterFront(registerName,registerEmail,registerPassword);
    registerData={"name":registerName,"email":registerEmail,"password":registerPassword};
    // postRegisterDataToBackEnd();
    
},false)


// =================================      前端正則表達式    =================================

//前端正則表達式
function checkRegisterFront(registerName,registerEmail,registerPassword){
    console.log("前端檢查中");
    let testForEmail = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}$/;
    let testForName = /^[\u4e00-\u9fa5a-zA-Z]+$/;
    // console.log(regex.test(registerEmail));
    if(registerEmail != "" & registerName != "" & registerPassword != ""){
        if(testForEmail.test(registerEmail)==true & testForName.test(registerName)==true){
            console.log("通過前端");
            postRegisterDataToBackEnd();
        }
        else{
            if(testForName.test(registerName)!=true) {
                responseFromBackend={"message":"姓名只接受英文跟中文形式，點此重新輸入"};
                dealRegistResponseFromBackend();
            }
            else if(testForEmail.test(registerEmail)!=true) {
                // XXXXresponseFromBackend["message"]
                responseFromBackend={"message":"請輸入正確信箱格式，點此重新輸入"};
                dealRegistResponseFromBackend();
            }
        }
        
        
    }else{
        responseFromBackend={"message":"註冊資料不可為空，點此重新輸入"};
        dealRegistResponseFromBackend();
    }
    
}

// ------------------------------------------------------------------



//post method to returndata to backend
let responseFromBackend=""
function postRegisterDataToBackEnd(){
    fetch("/api/user",{
        method:"POST",
        body:JSON.stringify(registerData),
        headers:new Headers({
            "content-type":"application/json"
        })
    }).then(function(response){
        return response.json();
    }).then(function(data){
        responseFromBackend=data;
        // console.log(responseFromBackend);
        dealRegistResponseFromBackend();
    })
}


//the page of Register
const registerMessage=document.querySelector(".registerMessage");
const registerContent=document.querySelector(".registerContent");
function dealRegistResponseFromBackend(){
    registerContent.style.height="350px";
    registerMessage.style.display="flex";
    //換位置
    registerMessage.style.top="50px";
    registerSignInTo.style.top="100px";
    if(responseFromBackend.ok==true){
        registerMessage.textContent="註冊成功";
        registerMessage.style.color="green";
    }
    else{
        registerMessage.textContent=responseFromBackend.message

        registerMessage.addEventListener('click',function(){
            close();
            filmBackground.style.display="block";
            registePage.style.display="flex";
            registerContent.style.height="322px";
            registerSignInTo.style.top="70px";
        },false)
    }
}


//get signin data
let signinEmail="";
let signinPassword="";
let signinData={}
const signinBtn=document.querySelector(".signinBtn");
signinBtn.addEventListener('click',function(){
    signinEmail=document.querySelector(".signinEmail").value;
    signinPassword=document.querySelector(".signinPassword").value;
    signinData={"email":signinEmail,"password":signinPassword};
    pushSigninDataToBackEnd();
},false)


//get method to returndata to backend
function pushSigninDataToBackEnd(){
    fetch("/api/user/auth",{
        method:"PUT",
        body:JSON.stringify(signinData),
        headers:new Headers({
            "content-type":"application/json"
        })
    }).then(function(response){
        // console.log("1",response);
        // console.log(response.status);
        return response.json();
    }).then(function(data){
        responseFromBackend=data;
        dealSigninResponseFromBackend();
        checkToken();
    })
}


//the page of signin
const signinContent=document.querySelector(".signinContent");
const signinMessage=document.querySelector(".signinMessage");
function dealSigninResponseFromBackend(){
    signinContent.style.height="290px";
    signinCreateAccount.style.top="90px";
    signinMessage.style.display="flex";

    if(responseFromBackend.ok==true){
        location.reload();
        signinMessage.textContent="登入成功";
        signinMessage.style.color="green";
    }
    else{
        signinMessage.textContent=responseFromBackend.message;
    }
}

//listener reflash
window.addEventListener("load", function() {
    checkToken()
});


let SignOut=document.querySelector(".SignOut");
function checkToken(){
    let url="/api/user/auth";
    fetch(url,{
        method:"GET",
    }).then(function(response){
        return response.json();
    }).then(function(data){
        if(data["data"]!=null){
            // console.log("目前為登入狀態");
            navSignInRegiste.style.display="none";
            SignOut.style.display="flex";
            member.style.display="flex";
        }
        else{
            // console.log("非登入狀態");
        }
    })
}


//listener execute signout
SignOut.addEventListener('click',function(){
    pushSignOutRequestToBackEnd()
},false)



//delete method to returndata to backend
function pushSignOutRequestToBackEnd(){
    fetch("/api/user/auth",{
        method:"DELETE",
        headers:new Headers({
            "content-type":"application/json"
        })
    }).then(function(response){
        location.reload();
        return response.json();
    })
}






///-------------------------------  BOOKING -------------------------------

//reserveJourney
const goToBooking=document.querySelector(".reserveJourney");
goToBooking.addEventListener('click',function(){
    checkUserToken();
},false)



//check cookie status
function checkUserToken(){
    let url="/api/user/auth";
    fetch(url,{
        method:"GET",
    }).then(function(response){
        return response.json();
    }).then(function(data){
        if(data["data"]!=null){
            window.location.href = "/booking";
        }
        else{
            filmBackground.style.display="block";
            signinPage.style.display="flex";
        }
    })
}


member.addEventListener('click',function(){
    window.location.href = "/member";
},false)