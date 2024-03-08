$(document).ready(function() {

    // $("#supervisor").change(function() {
    //     if ($(this).val() === 'ja') {
    //         $("#supervisor_div").fadeIn();
    //     } else {
    //         $("#supervisor_div").fadeOut();
    //     }
    // });
    $("#afkeur_form").hide();
    
    $("#afkeur_btn").on("click", function() {
        $("#afkeur_form").fadeIn();
    })

    $("#terug_btn_afkeur").on("click", function() {
        $("#afkeur_form").fadeOut(10);
    })
    
});