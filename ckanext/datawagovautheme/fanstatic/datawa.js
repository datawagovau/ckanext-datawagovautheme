jQuery(document).ready(function () {
	jQuery('#publisher-tree ul:first-child > li > a').contents().unwrap().wrap('<h2 class="parent-organization"/>');
	data_api_button = jQuery('.module-resource .actions ul li:last-child');
	if (data_api_button[0]['childElementCount'] == 0) {
		data_api_button.remove();		
	}
});
