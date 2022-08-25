const hamburger=document.getElementById("hamburger");

const navitems=document.getElementsByClassName("nav-items-container")[0];

hamburger.addEventListener('click',()=>
{
    navitems.classList.toggle('show');
});






let tabs = document.querySelectorAll('.tabs__toggle'),
    contents = document.querySelectorAll('.tabs__content');

tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => {
        contents.forEach((content) => {
            content.classList.remove('is-active');
        });
        tabs.forEach((tab) => {
            tab.classList.remove('is-active');
        });
        contents[index].classList.add('is-active');
        tabs[index].classList.add('is-active');
    });
});

let activebtn=document.getElementsByClassName('active-btn')[0];
  

activebtn.addEventListener('click',linking);

function linking()
{
    tabs.forEach((tab, index) => {
        
            contents.forEach((content) => {
                content.classList.remove('is-active');
            });
            tabs.forEach((tab) => {
                tab.classList.remove('is-active');
            });
            
});
        contents[1].classList.add('is-active');
            tabs[1].classList.add('is-active');
}

let archivebtn=document.getElementsByClassName('archive-btn')[0];
  

archivebtn.addEventListener('click',linking2);

function linking2()
{
    tabs.forEach((tab, index) => {
        
            contents.forEach((content) => {
                content.classList.remove('is-active');
            });
            tabs.forEach((tab) => {
                tab.classList.remove('is-active');
            });
            
});
        contents[2].classList.add('is-active');
            tabs[2].classList.add('is-active');
}