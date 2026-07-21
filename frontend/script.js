document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chatForm');
    const messageInput = document.getElementById('messageInput');
    const chatMessages = document.getElementById('chatMessages');
    const typingIndicator = document.getElementById('typingIndicator');

    // Hardcoded simple responses for the mock UI
    const botResponses = [
        "That's hilarious! 🤖😂",
        "Did you know I was built using Mistral AI? Well, technically this is just the frontend, but let's pretend!",
        "I'm feeling very byte-sized today. 🤓",
        "Interesting! Tell me more about that.",
        "Error 404: Sarcasm module not found. Just kidding! 😉",
        "If I had hands, I would be clapping right now.",
        "Let me compute that... Beep boop... The answer is 42."
    ];

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const message = messageInput.value.trim();
        if (!message) return;
        
        // Add user message
        appendMessage(message, 'user');
        
        // Clear input
        messageInput.value = '';
        
        // Show typing indicator
        typingIndicator.classList.add('active');
        scrollToBottom();
        
        try {
            const modeSelect = document.getElementById('modeSelect');
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message, mode: modeSelect.value })
            });
            
            const data = await response.json();
            
            typingIndicator.classList.remove('active');
            appendMessage(data.reply, 'bot');
        } catch (error) {
            console.error('Error:', error);
            typingIndicator.classList.remove('active');
            appendMessage('Sorry, I encountered an error. Is the server running?', 'bot');
        }
    });

    function appendMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);
        
        const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        
        let avatarIcon = sender === 'user' ? '<i class="fa-solid fa-user"></i>' : '<i class="fa-solid fa-robot"></i>';
        
        messageDiv.innerHTML = `
            <div class="avatar">${avatarIcon}</div>
            <div class="message-content">
                <p>${escapeHTML(text)}</p>
                <span class="timestamp">${time}</span>
            </div>
        `;
        
        chatMessages.appendChild(messageDiv);
        scrollToBottom();
    }

    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    function escapeHTML(str) {
        return str
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }
    
    // Focus input on load
    messageInput.focus();
});
