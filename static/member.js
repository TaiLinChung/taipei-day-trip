
//check cookie status
function getToken(){
    fetch("/api/user/auth",{
        method:"GET",
    }).then(function(response){
        return response.json();
    }).then(function(data){
        if(!data.data){
            window.location.href="/";
        }else{
            getMemberInformation();
        }
        
    })
}

//listener reflash
window.addEventListener("load", function() {
    getToken();
});


function getMemberInformation(){
    fetch("/api/member",{
        method:"GET",
    }).then(function(response){
        return response.json();
    }).then(function(data){
        console.log("data");
        // console.log(data);
        key_in_member_information(data)
    })
}

const memberName=document.querySelector(".memberName");
const memberEmail=document.querySelector(".memberEmail");
const memberPassword=document.querySelector(".memberPassword");
const memberMessage=document.querySelector(".memberMessage");
function key_in_member_information(data){
    memberName.value=data.name;
    memberEmail.value=data.email;
    memberPassword.value=data.password;
}
const footerBefore=document.querySelector(".footerBefore");
footerBefore.style.position="fixed";
footerBefore.style.bottom = "0px";



const changeInformationBTN=document.querySelector(".changeInformationBTN");
changeInformationBTN.addEventListener('click',function(){
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

const checkEyeMember = document.getElementById("checkEyeMember");
      const floatingMemberPassword =  document.getElementById("floatingMemberPassword");
      checkEyeMember.addEventListener("click", function(e){
        if(e.target.classList.contains('fa-eye')){
          e.target.classList.remove('fa-eye');
          e.target.classList.add('fa-eye-slash');
          floatingMemberPassword.setAttribute('type','text')
        }else{
            floatingMemberPassword.setAttribute('type','password');
          e.target.classList.remove('fa-eye-slash');
          e.target.classList.add('fa-eye')
        }
      });





