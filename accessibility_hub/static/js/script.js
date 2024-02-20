document.addEventListener('DOMContentLoaded', function () {
    var clickableRows = document.querySelectorAll('.clickable-row');
    clickableRows.forEach(function (row) {
        row.addEventListener('click', function () {
            window.location = row.dataset.href;
        });
    });
});

function checkForUpdates() {
    fetch('../updates/', {method: 'GET'})
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector('#list-recent-organisation tbody');
            tbody.innerHTML = '';

            data.forEach(organisatie => {
                const row = document.createElement('tr');
                row.classList.add('clickable-row');
                row.setAttribute('data-href', `/medewerkers/organisatie/${organisatie.id}`);

                const dateJoined = new Date(organisatie.date_joined);

                const formattedDate = `${('0' + dateJoined.getDate()).slice(-2)}-${('0' + (dateJoined.getMonth() + 1)).slice(-2)}-${dateJoined.getFullYear()} ${('0' + dateJoined.getHours()).slice(-2)}:${('0' + dateJoined.getMinutes()).slice(-2)}:${('0' + dateJoined.getSeconds()).slice(-2)}`;

                row.innerHTML = `
                    <td>${organisatie.bedrijfsnaam}</td>
                    <td>${organisatie.email}</td>
                    <td>${organisatie.first_name}</td>
                    <td>${organisatie.last_name}</td>
                    <td>${organisatie.status}</td>
                    <td>${formattedDate}</td>
                `;

                tbody.appendChild(row);
            });

            document.querySelectorAll('.clickable-row').forEach(row => {
                row.addEventListener('click', function() {
                    window.location.href = row.getAttribute('data-href');
                });
            });
        })
        .catch(error => {
            console.error('Fout bij het ophalen van updates:', error);
        });
}

setInterval(checkForUpdates, 2000);
