var results = [];
var selectedIndex = null;
var newResults;

String.prototype.trim = function () {
    return this.replace(/^\s*/, "").replace(/\s*$/, "");
}

function load()
{
	populateResultsArray()

	//selectItem(0) //to highlight the first one on load
	document.addEventListener("keydown", keypressed , false)
}

function isdefined( variable)
{
    return (typeof(window[variable]) == "undefined")?  false: true;
}

function $(elementName) {return document.getElementById(elementName);}

function populateResultsArray()
{
	results = [];
	
	var sections = document.getElementsByClassName("resultSection");
	
	var totals = [];
	
	for(j = 0; j < sections.length; j++)
	{
		var links = sections.item(j).getElementsByClassName("result");

		for (i = 0; i < links.length; i++)
			results.push(links.item(i))	
			
		var title = sections.item(j).getElementsByTagName("h3").item(0).innerText;
		var total = links.length;
		totals.push(total + " " + title.toLowerCase());
	}
}

function selectItem(rowIndex)
{
	if(rowIndex >= 0 && rowIndex < results.length && selectedIndex != rowIndex)
	{

		unselectSelectedRow();

		//'selected' will get written to file, so need this for when page is reaccessed from history
		if(results[rowIndex].className.indexOf("selected") == -1) 
			results[rowIndex].className += " selected";

		selectedIndex = rowIndex;				
	}
	scrollToRevealSelectedItem();
}

function unselectSelectedRow()
{
	if(selectedIndex != null)
	{
		selectedItem = results[selectedIndex]
		selectedItem.className = selectedItem.className.replace("selected", "").trim();
	}
}

function scrollToRevealSelectedItem()
{
	var obj = results[selectedIndex];
	
	if(!obj)
		return;
	
	//figure out the distance from the top of the content to the top of the selected item
	var offsetY = 0;
	var content = document.getElementById('content');	
	do
	{
		offsetY += obj.offsetTop;
		obj = obj.offsetParent;
	} while (obj && obj != content);
	
	var elementTop = offsetY;
	var elementHeight = results[selectedIndex].clientHeight;
	var elementBottom = elementTop + elementHeight;
	var footerHeight = document.getElementById('footer').clientHeight;
	var topOfVisibleArea = window.scrollY;
	var bottomOfVisibleArea = topOfVisibleArea + window.innerHeight - footerHeight;
	
	//if the element is outside of visible area, scroll so it isn't
	if(elementBottom > bottomOfVisibleArea)
		window.scrollBy(0, elementBottom - bottomOfVisibleArea);
	else if (elementTop < topOfVisibleArea)
		window.scrollBy(0, elementTop - topOfVisibleArea);
	else if(selectedIndex == 0 && window.scrollY > 0) //after the last one, show the section title too
		window.scrollTo(0,0);
}

//support for disclosure triangles that we aren't using
function closeSelectedSection()
{
	var sectionDiv = results[selectedIndex].parentNode.parentNode;
	if(sectionDiv.className.indexOf("closed") == -1)
		sectionDiv.className += " closed";
}

function openSelectedSection () {
	var sectionDiv = results[selectedIndex].parentNode.parentNode;
	sectionDiv.className = sectionDiv.className.replace("closed", "").trim();
}

function keypressed(event)
{
	var preventDefault = true;
	
	switch (event.keyCode)
	{
		case 37: //left
			// closeSelectedSection();
			break;
		case 38: // up
			selectItem(selectedIndex == null ? 0 : selectedIndex-1)
			break;
		case 39: //right
			// openSelectedSection();
			break;
		case 40: //down
			selectItem(selectedIndex == null ? 0 : selectedIndex+1)
			break;					
		case 13:
		case 3:
			clickSelectedLink()
			break;
		default:
			preventDefault = false;
			break;
	}
	if(preventDefault)
		event.preventDefault();
}

function refreshResultsSection(newHTML, totalsFoundString)
{
	var content = document.getElementById("content");
	content.innerHTML = newHTML;

	populateResultsArray();
	$('footerContent').innerText = totalsFoundString;
	
	var tempSelectedIndex = selectedIndex;
	selectedIndex = null;
	selectItem(tempSelectedIndex);

	//hack because its sometimes drawing the footer too high
	//TODO: figure out a better way than this workaround
	setTimeout("$('footer').style.bottom = '1px';", 0)
	setTimeout("$('footer').style.bottom = '0px';", 1)

	return document.documentElement.outerHTML;
}

function clickSelectedLink (event, clickedLink) {

	if(clickedLink && clickedLink.className.indexOf("selected") != -1)
		unselectSelectedRow();

	var currentLink = clickedLink ? clickedLink : results[selectedIndex];
	if(currentLink.target)
		window.open(currentLink.href, target);
	else
		window.location = currentLink.href;
	
	if(event)
	{
		event.preventDefault();
		event.stopPropagation();
	}
}

