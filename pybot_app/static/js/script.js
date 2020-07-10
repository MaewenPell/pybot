$(document).ready(function(){
  var chat_area, query, image_user, bot_image;
  var map;
  
  chat_area = $('#chat-area');
  image_user = 'static/imgs/user.svg'
  bot_image = 'static/imgs/ai.svg'
  map = initMap()

  $('#NewItemForm').on('submit', function (e) {
    e.preventDefault();
    query = $('input:text').val();
    display_new('User', 'Hey PyBot ! Please give me information on : ' + query,
      image_user, chat_area)
    $.ajax({
      data : query,
      type : 'POST',
      url : '/process',
      success : function (data) {
        bot_reply('Here are the informations for : ' + data, bot_image, chat_area);
        codeAdress(data, map)
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
  var latlng = new google.maps.LatLng(-34.397, 150.644);
  var mapOptions = {
    zoom : 8,
    center : latlng
  }
  map = new google.maps.Map(
    document.getElementById('map'), mapOptions);
  
    return map
}

function codeAdress(query, map) {
  var address = query;
  var geocoder = new google.maps.Geocoder();
  geocoder.geocode( {'address': address }, function(results, status) {
    if (status == 'OK') {
      map.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
        map: map,
        position: results[0].geometry.location
      });
    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
}

