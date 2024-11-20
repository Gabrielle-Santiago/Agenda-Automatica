// Utilizando flatpickr para configurar o horário e a data

document.addEventListener("DOMContentLoaded", function () {
    flatpickr("#appointmentTime", {
        // Formatação do horário para ficar de 13:30 à 19:00, com pausa (15:40 à 16:20)
        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
        time_24hr: true,
        minTime: "13:30",
        maxTime: "19:00",
        minuteIncrement: 10,

        // Abaixo é para aparecer um alerta pois o horário não pode
        onChange: (selectedDates, dateStr, instance) => {
            const disabledIntervals = [
                { from: "15:40", to: "16:20" }
            ];
            const selectedTime = dateStr;
        
            disabledIntervals.forEach(interval => {
                if (selectedTime >= interval.from && selectedTime <= interval.to) {
                    alert("Horário indisponível, escolha outro.");
                    instance.clear();
                }
            });
        }   
    });
});

// Configuração das datas, retirando o domingo e só marca a partir do dia atual
document.addEventListener("DOMContentLoaded", function () {
    flatpickr("#appointmentDate", {
        locale: "pt",
        minDate: "today",
        "disable": [
        function(date) {
            return (date.getDay() === 0 || date.getDay() === 7);
        }
    ]
    })
});