$(document).ready(function(){
  var section, chat_area, bot_name, text;
  chat_area = $('#chat-area');
  bot_name = $('.botName').html();

  $('#NewItemForm').on('submit', function (e) {
    e.preventDefault();
    text = $('input:text').val();

    display_new('Pybot', 'Test function', 'static/imgs/ai.svg', 'bot', chat_area)

    $('input:text').val('');
  });

});

function display_new(name, text, img, type, place) {
  $('<div/>', { 'class': 'row' }).append(
    $('<div/>', { 'class': 'col-2', 'id': 'logo-pybot' }).append(
      $('<img/>', { 'class': 'img-fluid', 'src': img, 'alt': 'BotImage' })),

    $('<div/>', { 'class': 'col-6' }).append(
      $('<h3/>', { 'class': 'font-weight-bold mb-3 botName', 'text': name }),
      $('<h6/>', { 'class': 'brown-text font-weight-bold mb-3 text-info', 'text': 'Internet Guide' }),
      $('<p/>', { 'class': 'botTalk justify-content-center', 'text': text })
    )).appendTo(place);
}

