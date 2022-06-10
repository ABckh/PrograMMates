const slug = JSON.parse(document.getElementById('json-username').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);


window.scrollTo(0, document.body.scrollHeight);

const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + slug
    + '/'
);

socket.onopen = function(e){
    console.log("CONNECTION ESTABLISHED");
}

socket.onclose = function(e){
    console.log("CONNECTION LOST");
}

socket.onerror = function(e){
    console.log("ERROR OCCURED");
}


socket.onmessage = function(e){
    const data = JSON.parse(e.data);
    if(data.username == message_username){
        document.querySelector('#chat-body').innerHTML += `
            <div class="center" style="width:100%">
        <div class="card" style="float: right; background:#0a94fc; margin-top: 15px">
        ${data.message}
        </div>
        </div >

        `
    }else{
        document.querySelector('#chat-body').innerHTML += `
            <div class="center" style="width:100%">
        <div class="card" style="float: left; background: grey; margin-top: 15px">
        ${data.message}
        </div>
        </div>

        `
    }
    window.scrollTo(0, document.body.scrollHeight);
};

document.querySelector('#chat-message-submit').onclick = function(e){
    const message_input = document.querySelector('#message_input');
    const message = message_input.value;

    socket.send(JSON.stringify({
        'message':message,
        'username':message_username
    }));

    message_input.value = '';
}

