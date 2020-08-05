$(document).ready(function(){
  var chat_area, query, image_user, bot_image;
  var lat, lng
  var map;
  var LatLng
  var marker
  
  chat_area = $('#chat-area');
  image_user = 'static/imgs/user.svg'
  bot_image = 'static/imgs/ai.svg'
  map = initMap();
  LatLng = new google.maps.LatLng(0, 0);
  var marker = new google.maps.Marker({
    map: map,
    position: LatLng
  });

  $('#NewItemForm').on('submit', function (e) {
    e.preventDefault();
    query = $('input:text').val();
    display_new('User' + query,
      image_user, chat_area)
    $.ajax({
      data : query,
      type : 'POST',
      url : '/process',
      success : function (data) {
        query = data[0]
        information = data[1]
        lat = data[2]
        lng = data[3]
        bot_reply('Voila les resultats' + information, bot_image, chat_area);
        updateMap(lat, lng, map, marker);
      }
    });

    $('input:text').val('');
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
                  'text': text } )
    )).appendTo(place);
}

// Initialize and add the map
function initMap() {
  var LatLng = new google.maps.LatLng(-34.397, 150.644);
  var mapOptions = {
    zoom : 8,
    center : LatLng
  }
  map = new google.maps.Map(
    document.getElementById('map'), mapOptions);
    return map
}

function updateMap(lat, lng, map, marker) {
  LatLng = new google.maps.LatLng(lat, lng);
  marker.setPosition(LatLng)
  map.setCenter(LatLng);
  marker.setMap(map)
}
