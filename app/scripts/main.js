(function ($) {
  var comment = '<div class="comment-item">\n  <div class="media">\n    <a class="pull-left" href="#">\n      <img class="media-object img-circle"\n           src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABp0lEQVRYR2O0vL3mP8MAAsZRB4yGwGgIjIbAaAgM2hD4+/ELw8cZ2xh+P33LwBfnzMCuLsvwfsomhp/n7zII5vkxcNrooNQgpKqHacZZF3zZdpqBVU6UgUmEj+FN6VwGbi9TBkZ2NgZubxOGF7E9DDwhNgyMjAwMnPZ6DG8blzBw2ukxsGvL4VQvMbeQgYmXE6Paw1sZ/XnzkeFlUj8Dl6shA3+WDwMTMzPD9zO3GD5M3Mgg1JnI8CZjCthAvlgnBt5QOwZ86sVm5jIwc3EQ74B/v/8wMPz9x/Dz0n2GD5M3MYhPy2H4duI6w0cgW6QrhYFdQ4bhy6aTDJ+W7GUQn5XHwMgNNJyAemy1Ps4QeNO0jIHLWZ+B3UCJ4WViP4NgSTDDu5blDMKNMQysylJgs14Xz2b4+/I9A3+OL8OPEzfxqgcFPyMoztAATgf8vPuM4U3hLLByniArhv8//zB83XoKzGfi5wZHy/8fvxg4nQ0Y3lYuYBAoC2F4D3Q0LvWgECQ5DYCj4c8/BiZONqLaTKSqBxk62iIaDYHREBgNgdEQGA2BAQ8BACMzBRDyXK0iAAAAAElFTkSuQmCC"\n           alt="32x32">\n    </a>\n\n    <div class="media-body">\n      <div class="media-heading">\n        <a href="#">username</a>\n                        <span>\n                          <i class="glyphicon glyphicon-chevron-up"></i> 0 <i\n                            class="glyphicon glyphicon-chevron-down"></i>\n                          <i class="glyphicon glyphicon-star-empty"></i>\n                        </span>\n        <small class="pull-right">сегодня 16:00</small>\n      </div>\n      <span class="lorem_p1"></span>\n      <small class="action-reply"><i class="fa fa-reply"></i> ответить</small>\n      <div class="edit-target"></div>\n    </div>\n  </div>\n</div>';

  $(function () {
//    $('.container').ipsum();

//    $('#some-textarea').wysihtml5({
//      locale: 'ru-RU'
//    });

    $('div.hr-item').on('click', '.hr-footer>.add-comment button', function (evt) {
      evt.preventDefault();

      var $this = $(this),
        $parent = $this.parents('.hr-item'),
        $target = $parent.find('.comment-list');
      console.log($this.closest('.add-comment').find('textarea').value())
      var value = $this.closest('.add-comment').find('textarea').value();

      if (value) {
        $.post({
          url    : 'comments/add/',
          data   : {
            article_type: $parent.data('type'),
            object_id   : $parent.data('id'),
            text        : value
          },
          success: function (result) {
            $target.append($(result));
          }
        });
      }
    });

    $('div.comment-list').on('click', '.action-reply', function (evt) {
      evt.preventDefault();

      var $this = $(this).hide(),
        $target = $this.siblings('div.edit-target:first'),
        $edit = $('.add-comment:first').clone(),
        $parent = $this.parents('.hr-item'),
        $comment = $this.parents('.comment-item');


      $edit.on('click', 'button', function () {
        $.post({
          url    : 'comments/add/',
          data   : {
            article_type: $parent.data('type'),
            object_id   : $parent.data('id'),
            refer_to    : $comment.data('id'),
            text        : $edit.find('textarea').value()
          },
          success: function (result) {
            $target.after($(result).ipsum());
            $edit.remove();
            $this.show()
          }
        });
      });

      $target.append($edit);
      $edit.find('textarea').focus();
    })
  });
}(jQuery));