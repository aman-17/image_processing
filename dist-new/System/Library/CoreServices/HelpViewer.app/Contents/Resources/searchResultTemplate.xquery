declare variable $pageTitle as xs:string external;
declare variable $cssPath as xs:string external;
declare variable $jsPath as xs:string external;
declare variable $resultSections external;
declare variable $foundText external;

<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>{$pageTitle}</title>
		<script src="{$jsPath}" type="text/javascript" charset="utf-8"></script>
		<link rel="stylesheet" href="{$cssPath}" type="text/css" media="screen" title="Search Result CSS" charset="utf-8" />
	</head>
	<body onload="load()">
		<div id="wrapper">
			<div id="content">
				{$resultSections}
			</div>
			<div id="footer">
				<div id="footerContent">{$foundText}</div>
			</div>
		</div>
	</body>
</html>