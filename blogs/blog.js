const hamburger=document.getElementById("hamburger");

const navitems=document.getElementsByClassName("nav-items-container")[0];

hamburger.addEventListener('click',()=>
{
    navitems.classList.toggle('show');
});

