$(function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').click(function () {
    const items = $('ul.my_list li');
    if (length.items > 0) {
      last_item = items[items.length - 1];
      last_item.remove();
    }
  });
  $('div#clear_list').click(function () {
    $('ul.my_list').clear();
  });
});
