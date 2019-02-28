ckan.module('resource-uploaded-warning', function($, _) {
  'use strict';

  return {
    options: {
      uploaded: null,
      edit: null,
    },
    initialize: function() {
      $.proxyAll(this, /_on/);
      var edit = this.options.edit && this.options.edit != 'False' ? true: false;
      if (edit) {
        var uploaded = this.options.uploaded == 'upload' ? true: false;
        this._updateWarning(uploaded);
      } else {
        this._updateWarning(false);
      }
      $('.image-upload .controls a, .image-upload .controls input').on('click', this._onClick);
    },
    _updateWarning(value) {
      var level_access = $('#field-access_level'),
          war_msg = $('#res-uploaded-warning');
      value ? (
          level_access.val('open'),
          level_access.closest('.form-group').css('display', 'None'),
          war_msg.show()
        ):(
          level_access.closest('.form-group').css('display', 'Block'),
          war_msg.hide()
        );
    },
    _onClick: function(event) {
      var name = event.currentTarget.name;
      var text = event.currentTarget.text;

      if (name && name == 'upload' && !text) {
        this._updateWarning(true);
      }

      if (!name && text == 'Link') {
        this._updateWarning(false);
      }
    }
  };
});
