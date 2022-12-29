
const result=document.querySelector(".result")
const transactionNumber=document.querySelector(".transactionNumber")
const contactName=document.querySelector(".contactName")
const contactEmail=document.querySelector(".contactEmail")
const contactPhone=document.querySelector(".contactPhone")

// console.log(window.location.search);
thankyouUrlSearch=window.location.search;
let orderUrl="api/order/"+thankyouUrlSearch.replace("?number=","");
if(orderUrl!=="api/order/"){
    checkUserToken();
}else{
    window.location.href = "/";
}

// console.log(orderUrl);
function getDataFromOrdersUrl(orderUrl){
    fetch(orderUrl).then(function(response){
        return response.json();
    }).then(function(data){
        if(data.error!=true){
            transactionNumber.textContent=data.data.number;
            contactName.textContent=data.data.contact.name;
            contactEmail.textContent=data.data.contact.email;
            contactPhone.textContent=data.data.contact.phone;
            if (data.data.status===0){
                result.textContent="訂單建立成功";
            }else{
                result.textContent="訂單建立失敗";
            }
        }else{
            // window.location.href = "/";
            document.querySelector(".thankYouPage").style.display="none";
            document.querySelector(".errorPage").style.display="flex";
            document.querySelector(".errorResult").textContent=data.message;
        }
        
    });
}


//check cookie status
function checkUserToken(){
    fetch("/api/user/auth",{
        method:"GET",
    }).then(function(response){
        return response.json();
    }).then(function(data){
        // console.log(data);
        if(data.data!=null){
            getDataFromOrdersUrl(orderUrl);
        }
        else{
            window.location.href = "/";
        }
    })
}
// checkUserToken();