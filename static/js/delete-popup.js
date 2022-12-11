let deleteBtn = document.getElementById('deleteBtn')
let deletePop = document.getElementById('deletePop')
let noBtn = document.getElementById('noBtn')

deletePop.style.display = 'none'

deleteBtn.addEventListener('click', ShowDeletePopUp)
noBtn.addEventListener('click', hidePopup)

function ShowDeletePopUp() {
    deletePop.style.display = ''
}

function hidePopup() {
    deletePop.style.display = 'none'
}