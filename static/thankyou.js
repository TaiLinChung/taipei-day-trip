
const result=document.querySelector(".result")
const transactionNumber=document.querySelector(".transactionNumber")
const contactName=document.querySelector(".contactName")
const contactEmail=document.querySelector(".contactEmail")
const contactPhone=document.querySelector(".contactPhone")

console.log(window.location.search);
thankyouUrlSearch=window.location.search;
let url="api/order/"+thankyouUrlSearch.replace("?number=","");
console.log(url);
function getDataFromOrdersUrl(url){
    fetch(url).then(function(response){
        return response.json();
    }).then(function(data){
        console.log(data);
        if(data["error"]!=true){
            transactionNumber.textContent=data["data"]["number"];
            contactName.textContent=data["data"]["contact"]["name"];
            contactEmail.textContent=data["data"]["contact"]["email"];
            contactPhone.textContent=data["data"]["contact"]["phone"];
            if (data["data"]["status"]===0){
                result.textContent="訂單建立成功";
            }else{
                result.textContent="訂單建立失敗";
            }
        }
        
    });
}
getDataFromOrdersUrl(url);