jQuery(document).ready(function () {
	$('ul.hierarchy-tree-top > li > a').contents().unwrap().wrap('<h2 class="parent-organization"/>');
});
