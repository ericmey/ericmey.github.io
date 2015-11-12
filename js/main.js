$(document).ready(function() {
  // TinyNav.js
  $('#nav').tinyNav({ header: 'Navigation' });

  // FitVid.js
  $(".main-container").fitVids();

  // Fancybox.js
  $('.fancybox').fancybox();

  // BackStretch.js
  $("#masthead").backstretch("/img/masthead@2x.jpg");
});
