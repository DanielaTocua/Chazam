//Activa la visibilidad del elemento con id "popup+num"
function showPopUp(popupId) {
	var state = document.getElementById(popupId).style.visibility;
	if (state == "visible"){
		document.getElementById(popupId).style.visibility= "hidden";
	}else{
		document.getElementById(popupId).style.visibility= "visible";
	}
}