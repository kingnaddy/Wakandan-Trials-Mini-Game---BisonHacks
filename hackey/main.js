// Main JavaScript file for the Wakandan Training Simulator

document.addEventListener('DOMContentLoaded', function() {
    // Add visual feedback for button clicks
    const menuButtons = document.querySelectorAll('.menu-button:not(.disabled)');
    
    menuButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Add a ripple effect
            const ripple = document.createElement('span');
            ripple.classList.add('ripple-effect');
            
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            
            this.appendChild(ripple);
            
            // Remove ripple after animation
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
    
    // Initialize any notifications
    initNotifications();
    
    // Set up vibranium counter animation
    animateVibraniumCounter();
});

function initNotifications() {
    // Check URL parameters for notifications
    const urlParams = new URLSearchParams(window.location.search);
    const notification = urlParams.get('notification');
    
    if (notification) {
        showNotification(decodeURIComponent(notification));
    }
}

function showNotification(message) {
    // Create notification element
    const notification = document.createElement('div');
    notification.classList.add('notification');
    notification.textContent = message;
    
    // Add to DOM
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.classList.add('show');
    }, 100);
    
    // Remove after timeout
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}

function animateVibraniumCounter() {
    const vibraniumCount = document.getElementById('vibranium-count');
    
    if (vibraniumCount) {
        const finalValue = parseInt(vibraniumCount.textContent);
        let currentValue = 0;
        
        // If value is 0, don't animate
        if (finalValue === 0) return;
        
        // Reset display value
        vibraniumCount.textContent = '0';
        
        // Animate counting up
        const interval = setInterval(() => {
            currentValue += Math.ceil(finalValue / 20);
            
            if (currentValue >= finalValue) {
                vibraniumCount.textContent = finalValue;
                clearInterval(interval);
            } else {
                vibraniumCount.textContent = currentValue;
            }
        }, 50);
    }
}

// Update settings in real-time
function updateTextSpeed(speed) {
    // Store setting locally
    localStorage.setItem('textSpeed', speed);
    
    // Apply to any active text animations
    document.documentElement.style.setProperty('--text-animation-speed', getTextAnimationDuration(speed));
}

function getTextAnimationDuration(speed) {
    switch(speed) {
        case 'slow': return '60ms';
        case 'medium': return '30ms';
        case 'fast': return '15ms';
        default: return '30ms';
    }
}

// Use this function to create typewriter text effect based on settings
function typewriterEffect(element, text) {
    // Check stored setting
    const textSpeed = localStorage.getItem('textSpeed') || 'medium';
    const charDelay = textSpeed === 'slow' ? 60 : textSpeed === 'medium' ? 30 : 15;
    
    element.textContent = ''; // Clear existing text
    
    let i = 0;
    const typing = setInterval(() => {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
        } else {
            clearInterval(typing);
        }
    }, charDelay);
}