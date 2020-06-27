$(document).ready(function(){
  var chat_area, text, image_user, bot_image;
  var map;
  chat_area = $('#chat-area');
  image_user = 'static/imgs/user.svg'
  bot_image = 'static/imgs/ai.svg'

  $('#NewItemForm').on('submit', function (e) {
    text = $('input:text').val();

    $.ajax({
      data : text,
      type : 'POST',
      url : '/process'
    }).done(function() {
      console.log('Done')
    });

    display_new('User', 'Bonjour je voudrais des info sur ceci : ' + text,
                image_user, chat_area)

    bot_reply('Here are the informations : ' + text, bot_image, chat_area);

    $('input:text').val('');
    e.preventDefault();
    initMap()
  });
});

function display_new(name, text, img, place) {
  $('<div/>', { 'class': 'row' }).append(
    $('<div/>', { 'class': 'col-2', 'id': 'logo-pybot' }).append(
      $('<img/>', { 'class': 'img-fluid', 
                    'src': img, 
                    'alt': 'UserImage',
                    'height': '100px',
                    'width':'100px'}
                    )),

    $('<div/>', { 'class': 'col-6' }).append(
      $('<h3/>', { 'class': 'font-weight-bold mb-3 botName', 'text': name }),
      $('<h6/>', { 'class': 'brown-text font-weight-bold mb-3 text-info', 'text': 'Internet Guide' }),
      $('<p/>', { 'class': 'botTalk justify-content-right', 'text': text })
    )).appendTo(place);
}

function bot_reply(text, img, place) {
  $('<div/>', { 'class': 'row' }).append(
    $('<div/>', { 'class': 'col-2', 'id': 'logo-pybot' }).append(
      $('<img/>', {
        'class': 'img-fluid',
        'src': img,
        'alt': 'UserImage',
        'height': '100px',
        'width': '100px'
      }
      )),

    $('<div/>', { 'class': 'col-6' }).append(
      $('<h3/>', { 'class': 'font-weight-bold mb-3 botName', 'text': 'Pybot' }),
      $('<h6/>', { 'class': 'brown-text font-weight-bold mb-3 text-info', 'text': 'Internet Guide' }),
      $('<p/>', { 'class': 'botTalk justify-content-right',
                  'text': 'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, \
                             consectetur, adipisci velit' })
    )).appendTo(place);
}

// Initialize and add the map
function initMap() {
  // The location of Uluru
  var uluru = {
    lat: -25.344,
    lng: 131.036
  };
  // The map, centered at Uluru
  var map = new google.maps.Map(
    document.getElementById('map'), {
    zoom: 4,
    center: uluru
  });
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({
    position: uluru,
    map: map
  });
}
