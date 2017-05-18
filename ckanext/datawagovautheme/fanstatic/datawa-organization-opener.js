"use strict";

ckan.module('datawa-organization-opener', function($, _){
  return {
    initialize: function(){
      $.proxyAll(this, /_on/);
      this.el.on('click', this._onClick);
    },

    _onClick: function(e) {
      var $target = $(e.target);
      if($target.is('li')){
        $target.toggleClass('open');
      }
    }
  }
});
