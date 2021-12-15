declare variable $sectionID as xs:string external;
declare variable $sectionTitle as xs:string external;
declare variable $searchResults external;

<div id="{$sectionID}" class="resultSection">
	<h3>{$sectionTitle}</h3>
	<div class="resultsList">
	{
		for $result in $searchResults
		return
		if ($result/@rowColor = "blue")
		then  <a href="{data($result/url)}" onclick="clickSelectedLink(event, this)" class="result blue" title="{data($result/summary)}" target="{data($result/target)}">
				<img src="{data($result/iconPath)}" class="icon" />
				<div class="title">{data($result/title)}</div>
				<div class="summary">{data($result/summary)}</div>				
			</a>
		else 
			<a href="{data($result/url)}" onclick="clickSelectedLink(event, this)" class="result" title="{data($result/summary)}" target="{data($result/target)}">
				<img src="{data($result/iconPath)}" class="icon" />
				<div class="title">{data($result/title)}</div>
				<div class="summary">{data($result/summary)}</div>				
			</a>
	}
	</div>
</div>
