async function sendMessage() {

    const inputField = document.getElementById("message-input");
    const message = inputField.value;

    if (!message) return;

    const chatBox = document.getElementById("chat-box");

    // Show user message
    chatBox.innerHTML += `<div class="user-message">${message}</div>`;

    inputField.value = "";

    try {
        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        chatBox.innerHTML += `<div class="bot-message">${data.answer}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
        chatBox.innerHTML += `<div class="bot-message">Error connecting to server.</div>`;
    }
}