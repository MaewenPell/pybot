$(function () {
  var $section, $chat_area, $bot_name
  $section = $('section');
  $chat_area = $('#chat-area');
  $bot_name = $('.botName').html();

  $('#NewItemForm').on('submit', function (e) {
    e.preventDefault();
    var text = $('input:text').val();
    $section.append(<li> text </li>);
    $('input:text').val('');
  });
});
