document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    if (userInput) {
        addMessageToChat('You', userInput);
        sendPromptToAPI(userInput);
    }
});

function addMessageToChat(sender, message) {
    const chatWindow = document.getElementById('chat-window');
    const messageElement = document.createElement('div');
    messageElement.textContent = `${sender}: ${message}`;
    chatWindow.appendChild(messageElement);
}

function sendPromptToAPI(prompt) {
    fetch('/api/prompt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: prompt }),
    })
    .then(response => response.json())
    .then(data => {
        addMessageToChat('OMNI', data.response);
    });
}
