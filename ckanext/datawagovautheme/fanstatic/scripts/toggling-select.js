ckan.module('toggling-select', function($, _) {
  'use strict';

  return {
    options: {
      match: null,
      target: null,
      extendTo: null,
      inverse: false
    },
    initialize: function() {
      $.proxyAll(this, /_on/);
      this.el.on('change', this._onChange);

      this._onChange();
    },
    _onChange: function() {
      var val = this.el.val();
      var target = $(this.options.target);
      if (this.options.extendTo) {
        target = target.closest(this.options.extendTo);
      }
      !!val.match(this.options.match) ^ this.options.inverse
        ? (target.find('input').attr('disabled', true), target.hide())
        : (target.find('input').removeAttr('disabled'), target.show());
    }
  };
});
