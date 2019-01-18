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
      $('.image-upload .controls').on('click', this._onClick);
    },
    _updateWarning(value) {
      value ? (
          $('#field-access_level').closest('.form-group').css('display', 'None'),
          $('#res-uploaded-warning').show()
        ):(
          $('#field-access_level').closest('.form-group').css('display', 'Block'),
          $('#res-uploaded-warning').hide()
        );
    },
    _onClick: function(event) {
      var name = event.target.name;
      var text = event.target.text;

      if (name && name == 'upload' && !text) {
        this._updateWarning(true);
      }

      if (!name && text == 'Link') {
        this._updateWarning(false);
      }
    }
  };
});
