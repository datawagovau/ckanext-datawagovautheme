"use strict";

ckan.module('drop_down_menu', function ($, _) {
  return {
    initialize: function () {
    	$.proxyAll(this, /_on/);
      	console.log("I've been initialized for element: ", this.el);
      	// $('a').attr('href') == location.pathname ? $('a').parent().addClass('active') : '';
      	$('.masthead .navigation ul.nav li a').each(function() {
      		if ($(this).attr('href') == location.pathname) {
      			$(this).parent().addClass('active');
      		}
      	});
      	$('.masthead .navigation ul.nav li a').on('click', function(event) {
      		console.log($(this));
      		event.preventDefault();
      	});
      }
  };
});