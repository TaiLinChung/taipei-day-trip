const messageBlock=document.querySelector(".messageBlock");
const attractionNameContent=document.querySelector(".attractionNameContent");
const orderDateContent=document.querySelector(".orderDateContent");
const orderTimeContent=document.querySelector(".orderTimeContent");
const orderFeeContent=document.querySelector(".orderFeeContent");
const orderAddressContent=document.querySelector(".orderAddressContent");
const imageBlock=document.querySelector(".imageBlock");
const bookingTotalPrice=document.querySelector(".bookingTotalPrice");
const trashcan=document.querySelector(".trashcan");



//check cookie status
function checkBookingToken(){
    let url="/api/user/auth";
    fetch(url,{
        method:"GET",
    }).then(function(response){
        return response.json();
    }).then(function(data){
        if(data.data){
            // console.log("目前為登入狀態",data["data"]);
        }
        else{
            // console.log("非登入狀態",data);
            let url="/"
            window.location.href = url;
        }
    })
}


//listener reflash
window.addEventListener("load", function() {
    // console.log("抓到你刷新頁面了吧，讓我檢查看看Token");
    checkBookingToken();
});




const bookingName=document.querySelector(".bookingName");
const bookingEmail=document.querySelector(".bookingEmail");
const bookingCellphone=document.querySelector(".bookingCellphone");
let username="";
function getBookingData(){
    fetch("/api/booking",{
        method:"GET",
    }).then(function(response){
        return response.json();
    }).then(function(data){
        if(data.data){
            username=data["username"];
            messageBlock.textContent="您好，"+data["username"]+"，待預定的行程如下 :";
            bookingName.value=data["username"];
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
            username=data["username"];
            displayNone();
        }
    })
}
getBookingData();







trashcan.addEventListener('click',function(){
    attractionId={"attractionId":(trashcan.getAttribute("id"))}
    deleteBooking(attractionId);
    // messageDownBlock.style.display="none";
})


function deleteBooking(attractionId){
    fetch(("/api/booking"),{
        method:"DELETE",
        body:JSON.stringify(attractionId),
        headers:new Headers({
            "content-type":"application/json"
        })
    }).then(function(){
        displayNone();
    })
    // .then(function(){
    //     // console.log("delete Done");
    //     // return response.json();
    //     displayNone();
    // })
}




const mainBefore=document.querySelector(".mainBefore");
const mainAfter=document.querySelector(".mainAfter");
const footerBefore=document.querySelector(".footerBefore");
mainAfter.style.display="none";
const footerAfter=document.querySelector(".footerAfter");

//下面不見
function displayNone(){
    mainBefore.style.display="none";
    mainAfter.style.display="block";
    footerBefore.style.display="none";
    footerAfter.style.display="block";
    let newMessageBlock=document.querySelectorAll(".messageBlock");
    newMessageBlock[1].textContent="您好，"+username+"，待預定的行程如下 :";
}

























//===========================   tapPay  ==========================
//=========================== setting bar attribute  =============

// TPDirect.setupSDK(`${APP_ID}`,`${APP_KEY}`, 'sandbox');
const bookingConfirmButton=document.querySelector(".bookingConfirmButton");
// TPDirect.setupSDK(126870,"app_SAUPg4xuOEWyb4B2874iGEv8LT1xYmzsj87ChJ9wFFbAFwciRpUA5HJtn2DJ", 'sandbox');
TPDirect.setupSDK(`${APP_ID}`,`${APP_KEY}`, 'sandbox');
TPDirect.card.setup({
    
    // Display ccv field
    fields : {
        number: {
            // css selector
            element: '#card-number',
            placeholder: '**** **** **** ****'
        },
        expirationDate: {
            // DOM object
            element: document.getElementById('card-expiration-date'),
            placeholder: 'MM / YY'
        },
        ccv: {
            element: '#card-ccv',
            placeholder: 'ccv'
        }
    },

    styles: {
        // Style all elements
        'input': {
            'color': 'gray'
        },
        // Styling ccv field
        'input.ccv': {
            // 'font-size': '16px'
        },
        // Styling expiration-date field
        'input.expiration-date': {
            // 'font-size': '16px'
        },
        // Styling card-number field
        'input.card-number': {
            // 'font-size': '16px'
        },
        // style focus state
        ':focus': {
            // 'color': 'black'
        },
        // style valid state
        '.valid': {
            'color': 'green'
        },
        // style invalid state
        '.invalid': {
            'color': 'red'
        },
        // Media queries
        // Note that these apply to the iframe, not the root window.
        '@media screen and (max-width: 400px)': {
            'input': {
                'color': 'orange'
            }
        }
    },
    // 此設定會顯示卡號輸入正確後，會顯示前六後四碼信用卡卡號
    isMaskCreditCardNumber: true,
    maskCreditCardNumberRange: {
        beginIndex: 6,
        endIndex: 11
    }
})


// 預設disabled確認訂購並付款的button
function disableBookingConfirmButton(){
    bookingConfirmButton.style.cursor = "default";
    bookingConfirmButton.setAttribute('disabled', true)
}
disableBookingConfirmButton();
// 開啟確認訂購並付款的button
function enableBookingConfirmButton(){
    bookingConfirmButton.style.cursor = "pointer";
    bookingConfirmButton.style.backgroundColor="#448899";
    bookingConfirmButton.removeAttribute('disabled');
}

//=========================== checking mechanism  ===========================
TPDirect.card.onUpdate(function (update) {
    // update.canGetPrime === true
    // --> you can call TPDirect.card.getPrime()
    // console.log("RRR");

    if (update.canGetPrime) {
        // Enable submit Button to get prime.
        // submitButton.removeAttribute('disabled')
        // bookingConfirmButton.style.cursor = "pointer";
        // bookingConfirmButton.style.backgroundColor="#448899";
        // bookingConfirmButton.removeAttribute('disabled');
        enableBookingConfirmButton();
        //滑鼠移入物件時
        bookingConfirmButton.addEventListener('mouseover',
        function(){
            bookingConfirmButton.style.backgroundColor = '#696969'}
        );
        //滑鼠離開物件時    
        bookingConfirmButton.addEventListener('mouseout',
        function(){
            bookingConfirmButton.style.backgroundColor = "#448899"}
        );
        

    } else {
        // Disable submit Button to get prime.
        // submitButton.setAttribute('disabled', true)
        // console.log("BBB");
    }

    // cardTypes = ['mastercard', 'visa', 'jcb', 'amex', 'unionpay','unknown']
    if (update.cardType === 'visa') {
        // Handle card type visa.
        // console.log("CCC");
    }

    // number 欄位是錯誤的
    if (update.status.number === 2) {
        // console.log("111");
        // setNumberFormGroupToError()
    } else if (update.status.number === 0) {
        // setNumberFormGroupToSuccess()
        // console.log("222");
    } else {
        // setNumberFormGroupToNormal()
        // console.log("333");
    }

    if (update.status.expiry === 2) {
        // setNumberFormGroupToError()
        // console.log("444");
    } else if (update.status.expiry === 0) {
        // setNumberFormGroupToSuccess()
        // console.log("555");
    } else {
        // setNumberFormGroupToNormal()
        // console.log("666");
    }

    if (update.status.ccv === 2) {
        // setNumberFormGroupToError()
        // console.log("777");
    } else if (update.status.ccv === 0) {
        // setNumberFormGroupToSuccess()
        // console.log("888");
    } else {
        // setNumberFormGroupToNormal()
        // console.log("999");
    }
})




//====== call TPDirect.card.getPrime when user submit form to get tappay prime  ======
const bookingConnectionErrorMessage=document.querySelector(".bookingConnectionErrorMessage");
bookingConfirmButton.addEventListener('click',function(){
    disableBookingConfirmButton();
    if(!(judgeDataIntegrity())){
        bookingConnectionErrorMessage.style.display="block";
        bookingConnectionErrorMessage.textContent="聯絡資訊皆不可為空，請填寫完整後再按下確認";
        enableBookingConfirmButton();
        return
    }
    if(!(judgeEmailFormal())){
        bookingConnectionErrorMessage.style.display="block";
        bookingConnectionErrorMessage.textContent="信箱格式錯誤，請填寫完整後再按下確認";
        enableBookingConfirmButton();
        return
    }
    if(!(judgeNameFormal())){
        bookingConnectionErrorMessage.style.display="block";
        bookingConnectionErrorMessage.textContent="姓名只允許中文或英文，請填寫完整後再按下確認";
        enableBookingConfirmButton();
        return
    }
    onSubmit();
},false)




// $('form').on('submit', onSubmit)
function onSubmit(event) {
    // event.preventDefault() //這幹嘛用的

    // 取得 TapPay Fields 的 status
    const tappayStatus = TPDirect.card.getTappayFieldsStatus()

    // 確認是否可以 getPrime
    if (tappayStatus.canGetPrime === false) {
        alert('can not get prime')
        return
    }

    // Get prime
    TPDirect.card.getPrime((result) => {
        if (result.status !== 0) {
            alert('get prime error ' + result.msg)
            return
        }
        console.log(result.card.prime);
        prime=result.card.prime;
        bookingDataForTappay=collectBookingDataForTappay(prime);
        // console.log(collectBookingDataForTappay(prime));
        postBookingDataForTappayToBackend(bookingDataForTappay);
        // alert('get prime 成功，prime: ' + result.card.prime)
        
        // send prime to your server, to pay with Pay by Prime API .
        // Pay By Prime Docs: https://docs.tappaysdk.com/tutorial/zh/back.html#pay-by-prime-api
    })
}



function judgeDataIntegrity(){
    if(bookingName.value!=="" && bookingEmail.value!=="" && bookingCellphone.value!==""){
        // console.log("true");
        return true
    }
}


// 前端正則表達式
function judgeEmailFormal(){
    let testForEmail = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}$/;
    if(testForEmail.test(bookingEmail.value)==true){
        return true
        
    }
}

function judgeNameFormal(){
    let testForName = /^[\u4e00-\u9fa5a-zA-Z]+$/;
    if(testForName.test(bookingName.value)==true){
        return true
        
        // postRegisterDataToBackEnd();
    }
}




function collectBookingDataForTappay(prime){
    dataForTappay={
        "prime":prime,
        "order":{
            "price":bookingTotalPrice.textContent,
            "trip":{
                "attraction":{
                    "id":trashcan.id,
                    "name":attractionNameContent.textContent,
                    "address":orderAddressContent.textContent,
                    "image":imageBlock.src
                },
                "date":orderDateContent.textContent,
                "time":orderTimeContent.textContent
            },
            "contact":{
                "name":bookingName.value,
                "email":bookingEmail.value,
                "phone":bookingCellphone.value
            }
        }
    }
    return dataForTappay
}




// const result=document.querySelector(".result")
function postBookingDataForTappayToBackend(bookingDataForTappay){
    fetch("/api/orders",{
        method:"POST",
        body:JSON.stringify(bookingDataForTappay),
        headers:new Headers({
            "content-type":"application/json"
        })
    }).then(function(response){
        return response.json();
    }).then(function(data){
        let url;
        if(data.error){
            url="/thankyou?number="+String(data.number);
        }else{
            url="/thankyou?number="+String(data.data.number);
        }
        window.location.href = url;
        
    })
}

function judgeTransactionRecord(transactionRecord){
    if(transactionRecord["data"]["payment"]["status"]===0){
        return true
    }
}

