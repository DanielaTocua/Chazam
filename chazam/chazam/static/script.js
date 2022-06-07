//Activa la visibilidad del elemento con id "popup+num"
function showPopUp(popupId) {
	var state = document.getElementById(popupId).style.visibility;
	if (state == "visible"){
		document.getElementById(popupId).style.visibility= "hidden";
	}else{
		document.getElementById(popupId).style.visibility= "visible";
	}
}


// customChaza
let popup1 = document.getElementById("popup-1")
let openPopup1 = document.getElementById("open-popup-1")
let closePopup1 = document.getElementById('close-popup-1')

openPopup1.addEventListener('click', () => {
	popup1.style.display = "block";
	openPopup1.style.display = "none";

})

closePopup1.addEventListener('click', () => {
	popup1.style.display = "none";
	openPopup1.style.display = "block";
})