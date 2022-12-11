let openBtn = document.getElementById('openBtn')
let closeBtn = document.getElementById('closeBtn')
console.log(openBtn)


openBtn.addEventListener('click', function() {
    document.getElementById("mySidenav").style.width = "250px";
})

closeBtn.addEventListener('click', function() {
    document.getElementById("mySidenav").style.width = "0";
})


function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}