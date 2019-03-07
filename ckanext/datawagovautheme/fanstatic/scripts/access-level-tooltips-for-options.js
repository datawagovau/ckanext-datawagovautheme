ckan.module('access-level-tooltips', function($, _) {
  'use strict';

  return {
    options: {
      list: {},
      select: null
    },
    initialize: function() {
      $.proxyAll(this, /_on/);
      var list = this.options.list;
      var access_level = this.options.select ? $(this.options.select) : '';

      if (access_level) {
        $.each(access_level.children(), function(index, option){
            if (option.value in list) {
                option.textContent = option.text + ' - ' + list[option.value];
            }
        });
      };
    },
  };
});
