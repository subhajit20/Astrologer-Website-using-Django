let timer;
const waitTime = 1500;

function showResults() {
    val = document.getElementById("place").value;
    res = document.getElementById("result");
    if (val == '' || val.length < 3) {
        res.innerHTML = '';
        return;
    }
    var url = '/api/getplace/'
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    clearTimeout(timer);
    timer = setTimeout(() => {
        if (val.length > 2) {
            $.ajax({
                headers: { 'X-CSRFToken': csrftoken },
                method: 'POST',
                url: url,
                data: {
                    'place': val,
                },
                beforeSend: function () {
                    load = "<div>Searching...</div>"
                    res.innerHTML = load
                },
                success: function (res) {
                    var data = res.geonames
                    if (data) {
                        dropDown(data)
                    }
                },
                error: function (){
                    var load = "<div>Oops, can't find places</div>"
                    res.innerHTML = load
                }
            })
        }
    }, waitTime);
}

function dropDown(data) {
    val = data
    res = document.getElementById("result");
    res.innerHTML = '';
    inputplace = document.getElementById("place")
    inputlat = document.getElementById("lat")
    inputlon = document.getElementById("lon")
    inputzone = document.getElementById("tzone")
    for (i = 0; i < data.length; i++) {
        suggestion = document.createElement('div');
        suggestion.setAttribute('id', i);
        suggestion.innerHTML = data[i].place_name;
        suggestion.addEventListener('click', function () {
            inputplace.value = this.innerHTML;
            inputlat.value = data[suggestion.id].latitude
            inputlon.value = data[suggestion.id].longitude
            inputzone.value = data[suggestion.id].timezone_id
            res.innerHTML = '';
        });
        suggestion.style.cursor = 'pointer';
        res.appendChild(suggestion);
    }
}

const formEle = document.getElementById("formEle");
if(formEle){
    formEle.addEventListener('submit', async e => {
        e.preventDefault();
        try{
            let response = await fetch('/api/report/', {
              method: 'POST',
              body: new FormData(formEle)
            });
            if (response.ok){
                let result = await response.json();
                if(result.status){
                    toast("Downloading...");
                    downloadFile(result.message)
                } else {
                    toast(result.message);
                }
            } else {
                toast("Server error, Try again later")
            }
        
        } catch(e){
            toast("Failed to send")
        }
    })
}

function toast(message){
    const toastEle = document.getElementById('liveToast')
    document.getElementById('toastMess').innerHTML = message
    const toast = new bootstrap.Toast(toastEle)
    toast.show()
}

function downloadFile(url){
    fetch(url).then(res => res.blob()).then(data => {
        let tempUrl = URL.createObjectURL(data);
        console.log(tempUrl)
        const aTag = document.createElement("a");
        aTag.href = tempUrl;
        aTag.download = "Report";
        document.body.appendChild(aTag);
        aTag.click();
        URL.revokeObjectURL(tempUrl);
        aTag.remove();
    }).catch(()=>{
        toast("Failed to download");
    })
}