/**
 * Updated bag quatity on click
 */
$(".update-link").click(function (e) {
  let form = $(this).prev(".update-form");
  form.submit();
});
