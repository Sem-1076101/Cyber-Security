$(document).ready(function() {
    $("#afkeur_form").hide();
    $("#terug_btn_afkeur").hide();

    
    $("#afkeur_btn").on("click", function() {
        $("#afkeur_form").toggle(400);
    })
    
});