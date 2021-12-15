// Page not found js

function $(el) {
    return document.getElementById(el);
}

function getLocalizedString(key, alternate) {
    try {
        var ret = localizedStrings[key];
        if (ret === undefined)
        ret = alternate;
        return ret;
    } catch (ex) {
        return alternate;
    }
    return key;
}

function setViewStrings(isOnline, isBasic) {
    var tempString;
    var noPageDesc;

    if (isBasic) {
        document.getElementsByTagName("title")[0].innerText = getLocalizedString("QuickTourNotFound", "Quick Tour Not Found");
        $("notFoundTitle").innerText = getLocalizedString("QuickTourNotFound", "Quick Tour Not Found");
        noPageDesc = getLocalizedString("NoQuickTourDescription","The Quick Tour you were trying to view could not be found.");
    } else {
        document.getElementsByTagName("title")[0].innerText = getLocalizedString("PageNotFound", "Page Not Found");
        $("notFoundTitle").innerText = getLocalizedString("PageNotFound", "Page Not Found");
        noPageDesc = getLocalizedString("NoPageDescription","The page you were trying to view could not be found.");
    }
    
    
    if (isOnline) {
        $("notFoundDescription").innerText = noPageDesc;
    } else {
        var noConnectionDesc = getLocalizedString("NoConnectionText", "Connect your Mac to the Internet and try again.");
        tempString = getLocalizedString("NoPageConnectionFormat","[NoPageDescription] [NoConnectionText]");
        tempString = tempString.replace("[NoPageDescription]", noPageDesc);
        tempString = tempString.replace("[NoConnectionText]", noConnectionDesc);
        $("notFoundDescription").innerText = tempString;
    }
}

function initialize() {
    var isOnline = HelpViewer.isOnline();
    setViewStrings(isOnline, false);
}