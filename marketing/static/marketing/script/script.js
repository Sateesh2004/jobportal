let div = document.getElementsByClassName("jobdetail")
let btnshow = document.getElementsByClassName("readmore")

let table = document.getElementsByTagName("table")
let btnhide=document.getElementsByClassName("btnhide")

for(let i = 0; i < btnshow.length; i++){
    btnshow[i].addEventListener("click", function() {
        show(i);
    });
}
function show(i)
{
    
        div[i].style.height="280px";
        table[i].style.display="block";
        btnhide[i].style.display="block";
    
    
    
    
    
}
for(let i = 0; i < btnshow.length; i++){
    btnhide[i].addEventListener("click", function() {
        hide(i);
    });
}
function hide(i){
    div[i].style.height="130px";
        table[i].style.display="none";
        btnhide[i].style.display="none";
}