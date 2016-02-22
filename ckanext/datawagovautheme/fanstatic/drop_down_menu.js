"use strict";

ckan.module('drop_down_menu', function ($, _) {
  return {
    initialize: function () {
    	$.proxyAll(this, /_on/);
      	console.log("I've been initialized for element: ", this.el);
      	this.el.find('li a').each(function() {
      		if ($(this).attr('href') == location.pathname) {
      			$(this).parent().addClass('active');
      		}
      	});
      	this.el.find('li.active').parents('.nav.dropdown-menu').css({
      		"display": "block"
      	})
      	//console.log(this.el.find('.nav:not(.dropdown-menu)').find('li'));
      	this.el.find('li.active').parents('li').addClass('children-active');
      	//console.log(this.el.closest('ul.nav:not(.dropdown-menu)'));
      	// this.el.find('li a').on('click', function(event) {
      	// 	console.log($(this));
      	// 	//event.preventDefault();
      	// });
      }
  };
});