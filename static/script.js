document.addEventListener('DOMContentLoaded', function () {
    let search = document.querySelector('#search');
    let box = document.querySelector('.searchedbox');
    search.addEventListener('focusin', () =>{
        if (box.children.length > 0) {
            box.style.display = 'block';
        }
    });
    search.addEventListener('focusout', (event) =>{
        setTimeout(() => {
            box.style.display = 'none';
        }, 200);
    });
    box.addEventListener('mousedown', (event) => {
        event.preventDefault();
    });
    search.addEventListener('input', async () => {
        let response = await fetch('/searched?q=' + search.value);
        let results = await response.json();
        let html = '';
        for (var result of results){
            html += '<li class="m-2 fw-bold"><a href="/pokemon/'+result.id+'">' + result.name + '</a></li>';
        }
        box.innerHTML = html;
    });
    let rows = document.querySelectorAll("table tr");
    rows.forEach(row => {
        let chart = row.querySelector("td .chart")
        chart.style.width= parseFloat(row.querySelector(".value").textContent.trim())/255*100+"%";
        val = parseInt(row.querySelector(".value").textContent.trim());
        if (val >= 120){
            chart.style.backgroundColor = "green";
        }
        else if (val >= 100){
            chart.style.backgroundColor = "lime";
        }
        else if(val >= 80){
            chart.style.backgroundColor = "yellow"
        }
        else if(val >= 60){
            chart.style.backgroundColor = "orange"
        }
        else if(val >= 30){
            chart.style.backgroundColor = "#FF2400"
        }
        else{
            chart.style.backgroundColor = "red"
        }
    });
});