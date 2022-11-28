
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


if (nextPage==0){
    urlPage=urlModel+nextPage
    getData();
    
}


function loadingPicture(){
    for(let i = 0; i < attractionAmount; i++){
        // let containerBlock=document.createElement("div")
        // containerBlock.setAttribute("class","container-block")
        // let tweleve =document.createElement('div')
        // tweleve.setAttribute('class',"container-twelve")

        // console.log(i);
        let item = document.createElement('div')
        item.setAttribute('class','item') 
        let imgBlock = document.createElement('div')
        imgBlock.setAttribute('class','img-block')
        let sort = document.createElement('div')
        sort.setAttribute('class','sort')
        item.appendChild(imgBlock)
        item.appendChild(sort)

        let containerBlock = document.querySelector('.container-block')
        containerBlock.appendChild(item)
        // let containerTwelve =document.querySelector('.container-twelve')
        // containerTwelve.appendChild(containerBlock);


        // tweleve.appendChild(position)
        // containerBlock.appendChild(more)

        attractionImg=attractions[i]["images"][0]
        attractionName=attractions[i]["name"]
        attractionLocation=attractions[i]["mrt"]
        attractionSort=attractions[i]["category"]

        let newImg = document.createElement("img")
        newImg.setAttribute("class","img-block")
        newImg.setAttribute("src",attractionImg)
        
        let newName = document.createElement("p")
        newName.textContent=attractionName
        document.querySelectorAll('.img-block')[i].appendChild(newName)

        let newMrt = document.createElement("p")
        newMrt.textContent=attractionLocation
        document.querySelectorAll('.sort')[i].appendChild(newMrt)

        let newCategory = document.createElement("p")
        newCategory.textContent=attractionSort
        document.querySelectorAll('.sort')[i].appendChild(newCategory)
        
        imgBlock.appendChild(newImg)
        imgBlock.appendChild(newName)
        sort.appendChild(newMrt)
        sort.appendChild(newCategory)
    }
}


function getData(){
    // loadPicture();
    fetch(urlPage).then(function(response){
        return response.json();
    }).then(function(data){

        if (data["error"]==true){
            console.log("the end");
        }else{
            console.log("continue")
            attractions = data["data"];
            // let attractionImg = "";
            // let attractionName ="";
            // let attractionLocation="";
            // let attractionSort="";
            attractionAmount=attractions.length
            loadingPicture();

            if (data["nextPage"]!=null){
                judgeContinue=1
            }else{
                judgeContinue=0
            }

            if(urlPage.includes("keyword")){
                console.log("keyword 判定");
                urlPage="/api/attractions?page="+data["nextPage"]+"&keyword="+keyword;
            }else{
                console.log("nextPage= ",data["nextPage"]);
                urlPage=urlModel+data["nextPage"];
                // console.log("777",urlPage);
                judgeContinue=1;
                loadmore();

            }
            
            
        }
    });
}




function loadmore(){
    if (judgeContinue==1){
        // console.log("我有在loadmore");
        const loading = document.querySelector('.loading');

        window.addEventListener("scroll",()=>{
            // let scrolled = window.scrollY;
            // console.log(scrolled);

            // let scrollable = document.documentElement.scrollHeight-window.innerHeight;
            // let scrollable= window.outerHeight - window.innerHeight;
            let scrolled = window.scrollY;
            // console.log(scrolled);
            
            if ((scrolled+ window.innerHeight>document.documentElement.scrollHeight-50) && judgeContinue==1){
            // if (Math.ceil(scrolled)===scrollable){
                // alert("You\'ve reached the bottom!");
                judgeContinue=0;
                showLoading();
                console.log("觸發");
                console.log(urlPage);
            }

        });

        function showLoading() {
            // loading.classList.add('show');
            // console.log(urlPage);
            setTimeout(getPost(), 1000);
        }


        function getPost(){
            fetch(urlPage).then(function(response){
                return response.json();
            }).then(function(data){
                attractions = data["data"]
                // attractionImg = ""
                // attractionName =""
                // attractionLocation=""
                // attractionSort=""
                attractionAmount=data["data"].length;
                loadingPicture();
                
                console.log("接下來的頁數",data["nextPage"])
                if (data["nextPage"]!=null){
                    urlPage=urlModel+data["nextPage"];

                    judgeContinue=1
                    loadmore();
                }else{
                    // alert("You\'ve reached the bottom!");
                }             

            });
        }


    }else{
        console.log("結束loadmore");
    }


}





//20221125
// =================display search bar and create items

let searchBlock = document.querySelector(".search");
// 觸發searchname事件
function submitBtn() {
    let searchcontainer = document.querySelector(".searchcontainer");
    let searchItemall = document.querySelectorAll(".searchItem");
    // console.log("first",searchItemall.length);
    let searchItemform=document.querySelector(".searchForm");

    if(searchItemall.length!=0){
        // console.log("即將刪幾個",searchItemall.length);
        searchItemform.innerHTML="";
        // //確認被刪除的物件唯一性 address ------------------------
        // for(let i=0; i<searchItemall.length; i++){
        //     console.log(i);
        //     searchItemform.removeChild(searchItemform.childNodes[0]);
        // }
    }
    searchcontainer.style.display="block";
    fetch("/api/categories").then(function(response){
        return response.json();
    }).then(function(data){
        
        let amountcategories=data["data"].length;
        // console.log("創建了幾個",amountcategories);
        for(let i = 0; i < amountcategories; i++){
            let more = document.createElement('div');
            // more.addEventListener
            more.setAttribute('class','searchItem');
            more.setAttribute('id',data["data"][i]);
            let position = document.querySelector('.searchForm');
            let itemName=data["data"][i];
            more.textContent=itemName;
            position.appendChild(more);
        }
       
        for (let i = 0;i< amountcategories; i++){
            let itemName="#"+data["data"][i];
            let keyinSearch = document.querySelector(itemName);
            keyinSearch.onclick=function(event){
                let searchBar = document.querySelector(".search");
                searchBar.value=event.target.id;
                // let searchForm = document.querySelector(".search");
                searchcontainer.style.display="none";
               
            }
        }
        //touchBody close the search item
        let touchBody=document.querySelector("#body");
        touchBody.addEventListener('click',function(e){
            // console.log(e.target.className);
            if(e.target.className!="searchForm" && e.target.className!="searchItem" && e.target.className!="search"){
                searchcontainer.style.display="none";
            };
            // icon();
        },false);
        
    });


}


//touch icon
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
        keyword=searchBlock.value;
        console.log(urlPage);
        // judgeContinue=1;
        // loadmore();
        getData();
        // create()
    },false);
}
icon();





// let src="https://api.kcg.gov.tw/api/service/Get/9c8e1450-e833-499c-8320-29b36b7ace5c";
    
// fetch(src).then((response)=>{
//     return response.json();
// }).then((data)=>{
//     console.log("Fetch 1");
//     console.log(data["data"]["XML_Head"]["Listname"]);
// });

// fetch(src).then((response)=>{
//     return response.json();
// }).then((data)=>{
//     console.log("Fetch 2");
//     console.log(data["data"]["XML_Head"]["Listname"]);
// });

// fetch(src).then((response)=>{
//     return response.json();
// }).then((data)=>{
//     console.log("Fetch 3");
//     console.log(data["data"]["XML_Head"]["Listname"]);
// });

// let src="https://api.kcg.gov.tw/api/service/Get/9c8e1450-e833-499c-8320-29b36b7ace5c";
// function ajax(){
//     return fetch(src).then((response)=>{
//         return response.json();
//     });
// }
// ajax().then((data1)=>{
//     console.log("Fetch 1");
//     // console.log(response);
//     console.log(data1["data"]["XML_Head"]["Listname"]);
//     return ajax();
// }).then((data2)=>{
//     console.log("Fetch 2");
//     console.log(data2["data"]["XML_Head"]["Listname"]);
//     return ajax();
// }).then((data3)=>{
//     console.log("Fetch 3");
//     console.log(data3["data"]["XML_Head"]["Listname"]);
// })