$(document).ready(function(){
  var chat_area, query, image_user, bot_image;
  var lat, lng
  var map;
  var LatLng;
  var marker;

  chat_area = $('#chat-area');
  image_user = '/static/imgs/user.svg';
  bot_image = 'static/imgs/bot.svg';
  map = initMap();
  LatLng = new google.maps.LatLng(0, 0);
  var marker = new google.maps.Marker({
    map: map,
    position: LatLng
  });

  $('#NewItemForm').on('submit', function (e) {
    e.preventDefault();
    query = $('input:text').val();
    $.ajax({
      data : query,
      type : 'POST',
      url : '/process',
      success : function (data) {
        query = data[0]
        information = data[1]
        lat = data[2]
        lng = data[3]
        address = data[4]
        address_wanted = data[5]
        info_wanted = data[6]
        user_asking(query, chat_area, image_user)
        bot_reply(information, chat_area, bot_image, address_wanted, address, info_wanted);
        updateMap(lat, lng, map, marker);
        $(map).show();
      }
    });

    $('input:text').val('');
  });

});

function bot_reply(reply, place, img, address_wanted, address, info_wanted) {
  var text = "";
  text += '<div class="row">'
  text += '<div id="bot_talk_area" class="col-10 col-md-8 rounded my-2 mx-auto">';
  text += '<h3 class="botName font-weight-bold text-center">Pybot &#129302;</h3>';
  text += '<h6 class="botInfo brown-text font-weight-light text-center">The internet scrapper</h6>';
  if (address_wanted == true) {
    text += "<p>Voila l'adresse demandée :</p>";
    text += "<p class='botTalk'>" + address + "</p>";
  }
  if (info_wanted == true) {
    text += '<p>Voila vos résultats :</p>';
    text += '<p class="botTalk">' + reply + '</p>';
  }
  if (address_wanted == false && info_wanted == false) {
    text += "<p> Je ne suis pas sur d'avoir compris la requête ? Voulez vous des informations et / ou une addresse ?";
  }
  text += '</div>';
  text += "<div class = 'col-2 my-auto d-none d-md-block' id='logo-pybot'>";
  text += "<img class='img-fluid' src=" + img + " alt='BotImage' height='100' width='100'>";
  text += "</div>"
  text += '</div>';
  $(text).appendTo(place);
}


function user_asking(query, place, img) {
  var text = "";
  text += '<div class="row">'
  text += "<div class = 'col-2 my-auto d-none d-md-block' id='logo-user'>";
  text += "<img class='img-fluid' src=" + img + " alt='UserImage' height='100' width='100'>";
  text += "</div>"
  text += '<div id="user_asking_area" class="col-10 col-md-8 rounded my-2 mx-auto">';
  text += '<h3 class="UserName font-weight-bold text-center">User</h3>';
  text += '<p class="userTalk">'+ query + '</p>';
  text += '</div>';
  text += '</div>';
  $(text).appendTo(place);
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
