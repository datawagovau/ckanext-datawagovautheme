"use strict";

ckan.module('drop_down_menu', function ($, _) {
  return {
    initialize: function () {
    	$.proxyAll(this, /_on/);
      	this.el.find('li a').each(function() {
      		if ($(this).attr('href') == location.pathname) {
      			$(this).parent().addClass('active');
      		}
      	});
      	this.el.find('li.active').parents('.nav.dropdown-menu').css({
      		"display": "block"
      	})
      	this.el.find('li.active').parents('li').addClass('children-active');
      	if (this.el.find('li.children-active').length == 1) {
			$('#content').css("padding-top", "121px");
		} else {
			console.log("li.children-active not found");
			$('#content').css("padding-top", "0px");
		}
      }
  };
});