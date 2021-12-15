declare variable $sectionID as xs:string external;
declare variable $sectionTitle as xs:string external;
declare variable $searchResults external;


<div>
	<h3>{$sectionTitle}</h3>
	{
		for $result in $searchResults
		return
			<p style="padding:0 15px; margin: 5px 0;">
				<a href="{data($result/url)}" class="result" title="{data($result/summary)}" style="margin:0;padding:0; font-size:14px;">
					<!--<img src="{data($result/iconPath)}" class="icon" style="float:none;" align="left"/>-->
					{data($result/title)}
				</a>
				<br />
				<span>{data($result/summary)}</span>
			</p>
	}
</div>