// memberUrl=window.location.href;
// console.log(memberUrl);


//check cookie status
function getToken(){
    let url="/api/user/auth";
    fetch(url,{
        method:"GET",
    }).then(function(response){
        return response.json();
    }).then(function(data){
        // console.log("data");
        // console.log(data);
        if(!data.data){
            window.location.href="/";
        }else{
            // console.log(data.data.id);
            let memberUrl="/api/member/"+String(data.data.id);
            // window.location.href=memberUrl;
            getMemberInformation(memberUrl);
        }
        
    })
}

//listener reflash
window.addEventListener("load", function() {
    // console.log("catch");
    getToken();
});


function getMemberInformation(memberUrl){
    fetch(memberUrl,{
        method:"GET",
    }).then(function(response){
        return response.json();
    }).then(function(data){
        // console.log("data");
        // console.log(data);
        key_in_member_information(data)
    })
}

const memberName=document.querySelector(".memberName");
const memberEmail=document.querySelector(".memberEmail");
const memberPassword=document.querySelector(".memberPassword");
const memberMessage=document.querySelector(".memberMessage");
function key_in_member_information(data){
    // console.log(data);
    memberName.value=data.name;
    memberEmail.value=data.email;
    memberPassword.value=data.password;
}
const footerBefore=document.querySelector(".footerBefore");
// const footerAfter=document.querySelector(".footerAfter");
footerBefore.style.position="fixed";
footerBefore.style.bottom = "10px";
// footerBefore.style.display="none";

// footerAfter.style.height="104px";
// footerAfter.style.bottom = "0";



const changeInformationBTN=document.querySelector(".changeInformationBTN");
changeInformationBTN.addEventListener('click',function(){
    // console.log(memberName.value);
    let newMemberData={
        "name":memberName.value,
        "email":memberEmail.value,
        "password":memberPassword.value
    }
    postNewMemberData(newMemberData);
})


function postNewMemberData(newMemberData){
    fetch(("/api/member"),{
        method:"POST",
        body:JSON.stringify(newMemberData),
        headers:new Headers({
            "content-type":"application/json"
        })
    }).then(function(response){
        return response.json();
    })
    .then(function(data){
        console.log(data);
        if(data.error){
            document.querySelector(".memberMessage").style.display="block";
            document.querySelector(".memberMessage").style.color="red";
            document.querySelector(".memberMessage").textContent=data.message;
        }else{
            document.querySelector(".memberMessage").style.color="green";
            document.querySelector(".memberMessage").textContent="更改成功";
        }
    })
}