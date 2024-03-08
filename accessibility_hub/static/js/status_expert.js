$(document).ready(function() {
    $("#afkeur_form").hide();
    
    $("#afkeur_btn").on("click", function() {
        $("#afkeur_form").fadeIn();
    })

    $("#terug_btn_afkeur").on("click", function() {
        $("#afkeur_form").fadeOut(10);
    })
    
});