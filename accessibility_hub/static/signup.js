
$(document).ready(function() {
    $("#supervisor_div").hide();

    $("#supervisor").change(function() {
        if ($(this).val() === 'ja') {
            $("#supervisor_div").fadeIn();
        } else {
            $("#supervisor_div").fadeOut();
        }
    });
   
    // console.log("jQuery is ready!");
});