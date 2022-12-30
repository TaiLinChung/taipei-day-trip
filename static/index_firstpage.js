
//全域變數===========================================================
let nextPage=0;                         //下一頁變數
let urlModel="/api/attractions?page=";  //網址模版
let urlPage="";                         //可讀取網址
let judgeContinue=0;                    //判斷是否可以loadmore
let urlKeywordmodel="/api/attractions?page=0&keyword=";
let keyword="";

//loadinPicture()
let attractions = "";
let attractionImg = "";
let attractionName ="";
let attractionLocation="";
let attractionSort="";
let attractionAmount=0;

//listenPicture()
let attractionId ="";


//Default start from first page
urlPage=urlModel+nextPage;
getData();


// urlPage="/api/attractions?page=100"
//Default getData HomePage
function getData(){
    fetch(urlPage).then(function(response){
        return response.json();
    }).then(function(data){

        if (data["error"]===true){
            // console.log("the end");
        }else{
            // console.log("continue")
            attractions = data["data"];
            nextPage=data["nextPage"];
            attractionAmount=attractions.length;
            loadingPicture();
            judgeContinueFunction();
            loadmore();

        }
    });
}



//judgeContinue
function judgeContinueFunction(){
    if ( nextPage != null){
        judgeContinue=1;
        if(urlPage.includes("keyword")){
            urlPage="/api/attractions?page="+nextPage+"&keyword="+keyword;
        }else{
            urlPage=urlModel+nextPage;
        }
    }else{
        judgeContinue=0;
    }
}


//loadingPicture
let loadingDonePosition=0;
function loadingPicture(){
    let containerBlock = document.querySelector('.container-block')
    for(let i = 0; i < attractionAmount; i++){
        attractionImg=attractions[i]["images"][0]
        attractionName=attractions[i]["name"]
        attractionId=attractions[i]["id"]
        attractionLocation=attractions[i]["mrt"]
        attractionSort=attractions[i]["category"]
        if(attractionLocation==null){
            attractionLocation="無捷運站";
        }
        //createItemBlock
        let item = document.createElement('div');
        item.setAttribute('class','item') ;
        let imgBlock = document.createElement('div');
        imgBlock.setAttribute('class','img-block');
        let sort = document.createElement('div');
        sort.setAttribute('class','sort');
        item.appendChild(imgBlock);
        item.appendChild(sort);
        containerBlock.appendChild(item);
        
        //putInIMG
        let newImg = document.createElement("img")
        newImg.setAttribute("class","img-block")
        newImg.setAttribute("src",attractionImg)
        imgBlock.appendChild(newImg)
        
        //putInDatas
        let newName = document.createElement("p")
        newName.textContent=attractionName
        document.querySelectorAll('.img-block')[i].appendChild(newName)
        //.item setAttribute 'name'  & 'id'
        document.querySelectorAll('.item')[loadingDonePosition+i].setAttribute('name',attractionName)
        document.querySelectorAll('.item')[loadingDonePosition+i].setAttribute('id',attractionId)
        imgBlock.appendChild(newName)

        let newMrt = document.createElement("p")
        newMrt.textContent=attractionLocation
        document.querySelectorAll('.sort')[i].appendChild(newMrt)
        // document.querySelectorAll('.sort')[loadingDonePosition+i].setAttribute('id',attractionId)
        sort.appendChild(newMrt)

        let newCategory = document.createElement("p")
        newCategory.textContent=attractionSort;
        // newCategory.setAttribute("id",attractionId);
        document.querySelectorAll('.sort')[i].appendChild(newCategory)
        sort.appendChild(newCategory)

        setListenerforEachID();
    }
    //update the Loading position
    loadingDonePosition+=attractionAmount;
}



function setListenerforEachID(){
    //替每個id所屬picture都設置監聽事件----------
    let pictureListener=document.getElementById(attractionId);
    pictureListener.onclick=function(event){
        // console.log("currentTarget: ",event.currentTarget);
        // console.log(event.target.id);//點擊對所在區塊的小白兔--------------------------------
        // console.log(event.currentTarget.id);//直接點擊監聽的所在區塊

        if(event.currentTarget.id != ""){
            let url="/attraction/"+event.currentTarget.id
            window.location.href = url;
        }
    }
}




function loadmore(){
    if (judgeContinue==1){
        //setting condition
        // const loading = document.querySelector('.loading');
        window.addEventListener("scroll",()=>{
            let scrolled = window.scrollY;           
            if ((scrolled+ window.innerHeight>document.documentElement.scrollHeight-50) && judgeContinue==1){
                judgeContinue=0;
                showLoading();
            }
        });

        function showLoading() {
            // loading.classList.add('show');
            setTimeout(getPost(), 1000);
        }

        //use New urlPage
        function getPost(){
            fetch(urlPage).then(function(response){
                return response.json();
            }).then(function(data){
                attractions = data["data"]
                attractionAmount=data["data"].length;
                loadingPicture();
                nextPage=data["nextPage"];
                judgeContinueFunction();
                urlPage=urlModel+nextPage;
                loadmore();
            });
        }

    }else{
        // console.log("結束loadmore");
    }
}



//click the searchBar then display search container and create items
let searchBlock = document.querySelector(".search");
function submitBtn() {
    // console.log("searchBar");
    let searchcontainer = document.querySelector(".searchcontainer");
    let searchItemform=document.querySelector(".searchForm");
    //remove Allchild
    while(searchItemform.hasChildNodes()){
        searchItemform.removeChild(searchItemform.firstChild)
    }

    //create searchitems
    searchcontainer.style.display="block";
    fetch("/api/categories").then(function(response){
        return response.json();
    }).then(function(data){
        let amountcategories=data["data"].length;
        for(let i = 0; i < amountcategories; i++){
            //create items
            let searchItemDIV = document.createElement('div');
            searchItemDIV.setAttribute('class','searchItem');
            searchItemDIV.setAttribute('id',data["data"][i]);
            let searchForm = document.querySelector('.searchForm');
            let searchItemName=data["data"][i];
            searchItemDIV.textContent=searchItemName;
            searchForm.appendChild(searchItemDIV);
            
            //add Listener to each item
            let itemName="#"+data["data"][i];
            let keyinSearch = document.querySelector(itemName);           
            keyinSearch.onclick=function(event){
                let searchBar = document.querySelector(".search");
                searchBar.value=event.target.id;
                // console.log(event);
                searchcontainer.style.display="none";
            }
        }

        
        //touchBody close the search item
        let touchBody=document.querySelector(".body");
        touchBody.addEventListener('click',function(e){
            // console.log(e.target.className);
            if(e.target.className!="searchForm" && e.target.className!="searchItem" && e.target.className!="search"){
                searchcontainer.style.display="none";
            };
        },false);
        
    });


}


//click the icon 刪小孩不刪爸爸
searchBlock.addEventListener("click", submitBtn );
function icon(){
    let createBtn=document.querySelector(".icon");
    createBtn.addEventListener("click",function(){
        let containerBlock=document.querySelector(".container-block");
        while(containerBlock.hasChildNodes()){
            containerBlock.removeChild(containerBlock.firstChild)
        }
        // containerBlock.style.display="none";
        // console.log(searchBlock.value);
        urlPage=urlKeywordmodel+searchBlock.value;
        // console.log(urlPage);
        //updateKeyword
        keyword=searchBlock.value;
        //setIdreset
        loadingDonePosition=0;
        getData();
    },false);
}
icon();



const checkEyeSignin = document.getElementById("checkEyeSignin");
      const floatingSigninPassword =  document.getElementById("floatingSigninPassword");
      checkEyeSignin.addEventListener("click", function(e){
        if(e.target.classList.contains('fa-eye')){
        //換class 病患 type
          e.target.classList.remove('fa-eye');
          e.target.classList.add('fa-eye-slash');
          floatingSigninPassword.setAttribute('type','text')
        }else{
            floatingSigninPassword.setAttribute('type','password');
          e.target.classList.remove('fa-eye-slash');
          e.target.classList.add('fa-eye')
        }
      });


const checkEyeRegister = document.getElementById("checkEyeRegister");
      const floatingRegisterPassword =  document.getElementById("floatingRegisterPassword");
      checkEyeRegister.addEventListener("click", function(e){
        if(e.target.classList.contains('fa-eye')){
        //換class 病患 type
          e.target.classList.remove('fa-eye');
          e.target.classList.add('fa-eye-slash');
          floatingRegisterPassword.setAttribute('type','text')
        }else{
            floatingRegisterPassword.setAttribute('type','password');
          e.target.classList.remove('fa-eye-slash');
          e.target.classList.add('fa-eye')
        }
      });