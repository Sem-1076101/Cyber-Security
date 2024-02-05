document.addEventListener('DOMContentLoaded', function() {
  var clickableRows = document.querySelectorAll('.clickable-row');
  clickableRows.forEach(function(row) {
    row.addEventListener('click', function() {
      window.location = row.dataset.href;
    });
  });
});
