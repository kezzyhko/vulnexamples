var socket;
function startWebsocket() {
    socket = new WebSocket('ws://' + window.location.host + '/chat/');

    socket.onmessage = function(e) {
        var response = JSON.parse(e.data);
        var li = document.createElement("li");
        li.classList.add(response.type);
        switch (response.type) {
            case 'connected':
                li.innerHTML = '<span class="username">' + response['username'] + '</span> has connected';
            break;
            case 'error':
                li.innerHTML = response['error'];
            break;
            case 'message':
                li.innerHTML = '<span class="username">' + response['username'] + ': </span>';
                li.append(response['message']);
            break;
        }
        chat.insertBefore(li, chat.children[0])
    };

    socket.onclose = function(e) {
        var li = document.createElement("li");
        li.classList.add('error');
        li.innerText = 'Disconnected. Trying to reconnect...';
        chat.insertBefore(li, chat.children[0])

        socket = null;
        setTimeout(startWebsocket, 5000);
    };
}
startWebsocket();


chatform = document.getElementById('chatform');
if (chatform) {
    chatform.onsubmit = function(e) {
    	e.preventDefault();
        var messageEl = document.getElementById('message');
        socket.send(JSON.stringify({'message': messageEl.value}));
        messageEl.value = '';
        messageEl.focus();
    };
}