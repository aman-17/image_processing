
function createSpinner () 
{
	var spinnerDiv = document.querySelector(".spinner");
	for ( x = 0; x < 12; x++ )
	{
		spinnerDiv.appendChild(document.createElement("DIV"));
	}
}
