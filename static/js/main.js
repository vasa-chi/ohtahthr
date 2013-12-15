(function ($) {
  $(function () {
//    $('.container').ipsum();

    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
      // test that a given url is a same-origin URL
      // url could be relative or scheme relative or absolute
      var host = document.location.host; // host + port
      var protocol = document.location.protocol;
      var sr_origin = '//' + host;
      var origin = protocol + sr_origin;
      // Allow absolute or scheme relative URLs to same origin
      return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
      beforeSend : function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
          // Send the token to same-origin, relative URLs only.
          // Send the token only if the method warrants CSRF protection
          // Using the CSRFToken value acquired earlier
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      }
    });

    $('#some-textarea').wysihtml5({
      locale : 'ru-RU'
    });

    $('div.hr-item')
      .on('click', '.hr-footer>.add-comment button', function (evt) {
        evt.preventDefault();

        var $this = $(this),
          $parent = $this.parents('.hr-item:first'),
          $target = $parent.find('.comment-list'),
          value = $this.closest('.add-comment').find('textarea').val();

        if (value) {
          $.ajax({
            url    : '/comments/add/',
            method : 'POST',
            data   : {
              comment_data : JSON.stringify({
                item_type : $parent.data('type'),
                object_id : $parent.data('id'),
                text      : value
              })}
          }).done(function (result) {
              console.log($target);
              $target.prepend($(result));
            });
        }
      })
      .on('click', '.action-reply', function () {
        var $this = $(this).hide(),
          $target = $this.siblings('div.edit-target:first'),
          $edit = $('.add-comment:first').clone(),
          $parent = $this.parents('.hr-item:first'),
          $comment = $this.parents('.comment-item:first');


        $edit.on('click', 'button', function () {
          $.ajax({
            url     : '/comments/add/',
            method  : 'POST',
            data    : {comment_data : JSON.stringify({
              item_type : $parent.data('type'),
              item_id   : $parent.data('id'),
              refer_to  : $comment.data('id'),
              text      : $edit.find('textarea').val()
            })},
            success : function (result) {
              $target.after($(result));
              $edit.remove();
              $this.show()
            }
          });
        });

        $target.append($edit);
        $edit.find('textarea').focus();
      })
      .on('click', '.action-edit', function () {
        var $this = $(this).hide(),
          $target = $this.siblings('.comment-text').hide(),
          text = $target.text(),
          $edit = $('.add-comment:first').clone()
            .find('button').text('Сохранить').end()
            .find('textarea').val(text).end(),
          $comment = $this.parents('.comment-item:first');

        $edit.on('click', 'button', function () {
          $.ajax({
            url     : '/comments/edit/',
            method  : 'POST',
            data    : {comment_data : JSON.stringify({
              comment_pk : $comment.data('id'),
              text       : $edit.find('textarea').val()
            })},
            success : function (result) {
              $comment.replaceWith(result);
            }
          });
        });

        $target.after($edit);
        $edit.find('textarea').focus();
      })
      .on('click', '.comment-rating-wrapper .glyphicon', function () {
        var $this = $(this),
          $container = $this.closest('.comment-rating-wrapper').find('.comment-rating'),
          $comment = $this.closest('.comment-item'),
          changeType = $this.hasClass('glyphicon-chevron-up') ? 1 : 0;

        $.ajax({
          url    : '/rate/',
          method : 'POST',
          data   : {rating_data : JSON.stringify({
            object_pk : $comment.data('id'),
            item_type : $comment.data('type'),
            type      : changeType
          })}
        }).done(function (result) {
            $container.text(result.rating)
          });
      });

    var tags = $('#tag-input')
      .tagsManager({
        tagsContainer : '#tag-container',
        maxTags       : 10,
        output        : '#tags'
      });
    tags
      .typeahead({
        name  : 'arabic',
        local : ['one', 'two', 'three']
      })
      .on('typeahead:selected', function (e, d) {
        tags.tagsManager("pushTag", d.value);
      })
      .on('tm:hide', function () {
        $(this).closest('.twitter-typeahead').hide()
      })
      .on('tm:show', function () {
        $(this).closest('.twitter-typeahead').show()
      });

    $('.typeahead.input-sm').siblings('input.tt-hint').addClass('hint-small');
    $('.typeahead.input-lg').siblings('input.tt-hint').addClass('hint-large');

  });
}(jQuery));