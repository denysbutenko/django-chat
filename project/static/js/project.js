/* Project specific Javascript goes here. */
$(document).ready(function () {
  $('#createChannelSubmit').click(function() {
    var channel_name = $('#name').val();
    console.log(channel_name);
    if(channel_name) {
      $('#createChannelForm').submit();
    } else {
      $('#name').focus();
    }
  });
  $('#createChannelModal').on('shown.bs.modal', function (e) {
    $('#name').focus();
  })
});
