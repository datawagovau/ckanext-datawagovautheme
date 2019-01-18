ckan.module('resource-warning', function($, _) {
  'use strict';

  return {
    options: {
      match: null,
      target: null,
      inverse: false
    },
    initialize: function() {
      $.proxyAll(this, /_on/);
      this.el.on('change', this._onChange);

      this._onChange();
    },
    _onChange: function() {
      var options = (this.options.match).split(',');
      var val = this.el.val();
      var target = $(this.options.target);

      jQuery.inArray(val, options) > -1 ? (
          target.hide()
        ):(
          target.show()
        );
    }
  };
});
