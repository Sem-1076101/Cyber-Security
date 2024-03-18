$(document).ready(function() {
    function get_ervaringsdeskundigen() {
        $.ajax({
            url: '/medewerkers/portal/',
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                $('#recent-expert-body').empty();
                $.each(data.ervaringsdeskundigen, function(ervaringsdeskundige){
                    var row = '<tr class="clickable-row" data-href="/medewerkers/ervaringsdeskundige/' + ervaringsdeskundige.deskundige_id + '">' +
                                  '<td>' + ervaringsdeskundige.voornaam + ' ' + ervaringsdeskundige.achternaam + '</td>' +
                                  '<td>' + ervaringsdeskundige.geboortedatum + '</td>' +
                                  '<td>' + ervaringsdeskundige.email + '</td>' +
                                  '<td>' + ervaringsdeskundige.telefoonnummer + '</td>' +
                                  '<td>' + ervaringsdeskundige.soort_beperking + '</td>' +
                                  '<td>' + getStatus(ervaringsdeskundige.account_status) + '</td>' +
                                  '<td>' + ervaringsdeskundige.created_at + '</td>' +
                              '</tr>';
                    $('#recent-expert-body').append(row);
                });
            },
            error: function(xhr, status, error) {
                console.error('Probleem met het ophalen: ', error);
            }
        });
    }

    function getStatus(statusCode) {
        if (statusCode === 0) {
            return 'In behandeling';
        } else if (statusCode === 1) {
            return 'Goedgekeurd';
        } else {
            return 'Afgekeurd';
        }
    }

    get_ervaringsdeskundigen();
    setInterval(get_ervaringsdeskundigen, 1000);
});