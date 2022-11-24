// // console.log("666")
// nextPage=0; //下一頁變數
// let urlModel="/api/attractions?page="  //網址模版
// let urlPage=""                         //可讀取網址

// if (nextPage==0){
//     getData();
    
// }

// function getData(){
//         fetch("/api/attractions?page=0").then(function(response){
//             return response.json();
//         }).then(function(data){
//             // console.log(data)
//             // console.log("----------------")
//             // console.log(data["data"][0])
//             let attractions = data["data"];
//             let attractionImg = "";
//             let attractionName ="";
//             let attractionLocation="";
//             let attractionSort="";

            
//             for(let i = 0; i < 12; i++){
//                 // // console.log(attractions)
//                 // console.log((attractions[i]["images"]))
//                 attractionImg=attractions[i]["images"][0];
//                 // console.log(attractionImg);
//                 attractionName=attractions[i]["name"];
//                 attractionLocation=attractions[i]["mrt"];
//                 attractionSort=attractions[i]["category"];

//                 let newImg = document.createElement("img");
//                 newImg.setAttribute("class","img-block");
//                 // console.log(newImg.class)
//                 newImg.setAttribute("src",attractionImg);
//                 let imgTwelve=document.querySelectorAll(".apple");

                
//                 imgTwelve[i].appendChild(newImg);

//                 let newName = document.createElement("p");
//                 newName.textContent=attractionName;
//                 // console.log(newName)
//                 document.querySelectorAll('.apple')[i].appendChild(newName);

//                 let newMrt = document.createElement("p");
//                 newMrt.textContent=attractionLocation;
//                 document.querySelectorAll('.sort')[i].appendChild(newMrt);

//                 let newCategory = document.createElement("p");
//                 newCategory.textContent=attractionSort;
//                 document.querySelectorAll('.sort')[i].appendChild(newCategory);
                
//             }


//             // console.log("the type is ",typeof(data["nextPage"]))
//             // console.log(data["nextPage"])
//             console.log("*****");
//             urlPage=urlModel+0;
//             console.log(urlPage);
//             if (data["nextPage"]!=null){
//                 nextPage=data["nextPage"];  //下一頁變數更新
//                 urlPage=urlModel+nextPage;
//                 console.log(urlPage);
//                 loadmore();
//             }
//             // judgeNextpage()
            

//         });
// }
// // getData();

// // function judgeNextpage(){
// //     if (data["nextPage"]!=null){
// //         nextPage=data["nextPage"];
// //         url=url+nextPage;
// //         loadmore();
// //     }
// // }



// function loadmore(){
//     const loading = document.querySelector('.loading');

//     window.addEventListener("scroll",()=>{
//         // let scrolled = window.scrollY;
//         // console.log(scrolled);

//         let scrollable = document.documentElement.scrollHeight-window.innerHeight;
//         // let scrollable= window.outerHeight - window.innerHeight;
//         let scrolled = window.scrollY;
//         // console.log(scrolled);
        

//         if (Math.ceil(scrolled)===scrollable){
//             // alert("You\'ve reached the bottom!");
//             showLoading();
//         }

//     });

//     function showLoading() {
//         loading.classList.add('show');
        
//         // load more data
//         setTimeout(getPost, 1000)
//     }

//     function getPost(){
//         fetch(urlPage).then(function(response){
//             return response.json();
//         }).then(function(data){
//             // console.log(data)
//             // console.log("----------------")
//             // console.log(data["data"][0])
//             let attractions = data["data"]
//             let attractionImg = ""
//             let attractionName =""
//             let attractionLocation=""
//             let attractionSort=""
            
//             for(let i = 0; i < 12; i++){

//                 let more = document.createElement('div')
//                 more.setAttribute('class','item')
//                 let position =document.querySelector('.container-block')
//                 position.appendChild(more)
//                 let apple = document.createElement('div')
//                 apple.setAttribute('class','img-block')
//                 let sort = document.createElement('div')
//                 sort.setAttribute('class','sort')
//                 more.appendChild(apple)
//                 more.appendChild(sort)

//                 attractionImg=attractions[i]["images"][0]
//                 attractionName=attractions[i]["name"]
//                 attractionLocation=attractions[i]["mrt"]
//                 attractionSort=attractions[i]["category"]

//                 let newImg = document.createElement("img")
//                 newImg.setAttribute("class","img-block")
//                 newImg.setAttribute("src",attractionImg)
                
                
//                 let newName = document.createElement("p")
//                 newName.textContent=attractionName
//                 // newName.setAttribute("class","")
//                 // console.log(newName)
//                 document.querySelectorAll('.apple')[i].appendChild(newName)

//                 let newMrt = document.createElement("p")
//                 newMrt.textContent=attractionLocation
//                 document.querySelectorAll('.sort')[i].appendChild(newMrt)

//                 let newCategory = document.createElement("p")
//                 newCategory.textContent=attractionSort
//                 document.querySelectorAll('.sort')[i].appendChild(newCategory)
                
//                 apple.appendChild(newImg)
//                 apple.appendChild(newName)
//                 sort.appendChild(newMrt)
//                 sort.appendChild(newCategory)
//             }

//             // const container = document.getElementById('container');
//             // const containerTwelve = document.getElementsByClassName('container-twelve');
//             // container.appendChild(containerTwelve);
            

//             // console.log(data["nextPage"])
            
//             // container.appendChild(containerTwelve);
//             // loading.classList.remove('show');


//                 // console.log("目前頁數",)
//                 // console.log("接下來的頁數",data["nextPage"])
//                 if (data["nextPage"]!=null){
//                     urlPage=urlModel+data["nextPage"];
//                     console.log("接下來要讀取的頁數",urlPage);
//                     // console.log("接下來要讀取的頁數",data["nextPage"])
//                     // loadmore();
//                 }else{
//                     alert("You\'ve reached the bottom!");
//                 }

//                 //urlModel
//                 // if (data["nextPage"]!=null){
//                 //     nextPage=data["nextPage"];
//                 //     urlPage=urlPage+nextPage;
//                 //     loadmore();
//                 // }
                



//         });
//     }


// }






// // const loading = document.querySelector('.loading');

// // // getPost();

// // window.addEventListener("scroll",()=>{
// //     // let scrolled = window.scrollY;
// //     // console.log(scrolled);

// //     let scrollable = document.documentElement.scrollHeight-window.innerHeight;
// //     // let scrollable= window.outerHeight - window.innerHeight;
// //     let scrolled = window.scrollY;
// //     console.log(scrolled);

// //     if (Math.ceil(scrolled)===scrollable){
// //         // alert("You\'ve reached the bottom!");
// //         showLoading();
// //     }

// // });

// // function showLoading() {
// // 	loading.classList.add('show');
	
// // 	// load more data
// // 	setTimeout(getPost, 1000)
// // }

// // function getPost(){
// //     // alert("You\'ve reached the bottom!");
// //     fetch("/api/attractions?page=1").then(function(response){
// //         return response.json();
// //     }).then(function(data){
// //         // console.log(data)
// //         // console.log("----------------")
// //         // console.log(data["data"][0])
// //         let attractions = data["data"]
// //         let attractionImg = ""
// //         let attractionName =""
// //         let attractionLocation=""
// //         let attractionSort=""

        
// //         for(let i = 0; i < 12; i++){
// //             // // console.log(attractions)
// //             // console.log((attractions[i]["images"]))
// //             attractionImg=attractions[i]["images"][0]
// //             // console.log(attractionImg);
// //             attractionName=attractions[i]["name"]
// //             attractionLocation=attractions[i]["mrt"]
// //             attractionSort=attractions[i]["category"]

// //             let newImg = document.createElement("img")
// //             newImg.setAttribute("class","img-block")
// //             // console.log(newImg.class)
// //             newImg.setAttribute("src",attractionImg)
// //             let imgTwelve=document.querySelectorAll(".apple")

            
// //             // imgTwelve[i].appendChild(newImg)

// //             // let newName = document.createElement("p")
// //             // newName.textContent=attractionName
// //             // // console.log(newName)
// //             // document.querySelectorAll('.apple')[i].appendChild(newName)

// //             // let newMrt = document.createElement("p")
// //             // newMrt.textContent=attractionLocation
// //             // document.querySelectorAll('.sort')[i].appendChild(newMrt)

// //             // let newCategory = document.createElement("p")
// //             // newCategory.textContent=attractionSort
// //             // document.querySelectorAll('.sort')[i].appendChild(newCategory)
            
// //         }
// //         // const container = document.getElementById('container');
// //         // const containerTwelve = document.getElementsByClassName('container-twelve');
// //         // container.appendChild(containerTwelve);
        

// //         // console.log(data["nextPage"])
        
// //         // container.appendChild(containerTwelve);
// // 	    // loading.classList.remove('show');




            



// //     });
// // }
