const hamburger=document.getElementById("hamburger");

const navitems=document.getElementsByClassName("nav-items-container")[0];

hamburger.addEventListener('click',()=>
{
    navitems.classList.toggle('show');
});


let tabs = document.querySelectorAll('.domain-box');
let contents = document.querySelectorAll('.domain-detailed');

tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => {
        contents.forEach((content) => {
            content.classList.remove('is-selected');
        });
        tabs.forEach((tab) => {
            tab.classList.remove('is-selected');
        });
        contents[index].classList.add('is-selected');
        tabs[index].classList.add('is-selected');
    });
});
