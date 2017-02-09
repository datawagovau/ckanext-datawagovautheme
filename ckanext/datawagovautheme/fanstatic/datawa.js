jQuery(document).ready(function () {
	$('#publisher-tree ul:first-child > li > a').contents().unwrap().wrap('<h2 class="parent-organization"/>');
});
