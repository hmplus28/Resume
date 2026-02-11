

const CONFIG = {
  showContactInfo: true, 
  contact: {
    phone: 'در دسترس نیست',
    email: 'hmplus28@gmail.com'
  }
};


function setupContactInfo() {
    const phoneElement = document.getElementById('dynamic-phone');
    const emailLinkElement = document.getElementById('dynamic-email-link');

    if (CONFIG.showContactInfo) {
        if (phoneElement) {
            phoneElement.textContent = CONFIG.contact.phone;
        }
        if (emailLinkElement) {
            emailLinkElement.textContent = CONFIG.contact.email;
            emailLinkElement.href = `mailto:${CONFIG.contact.email}`;
        }
    } else {
        if (phoneElement) {
            phoneElement.textContent = '[در دسترس نیست]';
            phoneElement.style.color = 'var(--light-text)';
        }
        if (emailLinkElement) {
            emailLinkElement.textContent = '[در دسترس نیست]';
            emailLinkElement.href = '#';
            emailLinkElement.style.color = 'var(--light-text)';
        }
    }
}

function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = "block";
        document.body.style.overflow = "hidden";
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = "none";
        document.body.style.overflow = "auto";
    }
}

function openImageModal(event, element) {
    event.preventDefault();
    const imageSrc = element.getAttribute('href');
    const imageAlt = element.querySelector('img').getAttribute('alt');
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImage');

    modalImg.src = imageSrc;
    modalImg.alt = imageAlt;
    modal.style.display = 'block';
   
    document.body.style.overflow = "hidden";
}

function closeImageModal() {
    const modal = document.getElementById('imageModal');
    if (modal) {
        modal.style.display = "none";
        document.body.style.overflow = "auto";
    }
}


document.addEventListener('DOMContentLoaded', () => {
    setupContactInfo();

    const modalButtons = document.querySelectorAll('[data-modal-target]');
    modalButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modalId = button.getAttribute('data-modal-target');
            openModal(modalId);
        });
    });

    const closeButtons = document.querySelectorAll('.modal .close');
    closeButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.stopPropagation();
            const modal = button.closest('.modal');
            if (modal) {
                closeModal(modal.id);
            }
        });
    });
});

window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        closeModal(event.target.id);
    }
}

const imageModal = document.getElementById('imageModal');
const imageModalCloseBtn = document.querySelector('.image-modal-close');
if (imageModal) {
    imageModal.addEventListener('click', (e) => {
        if (e.target === imageModal) {
            closeImageModal();
        }
    });
    if (imageModalCloseBtn) {
        imageModalCloseBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            closeImageModal();
        });
    }
}

window.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
        const openModal = document.querySelector('.modal[style*="block"]');
        if (openModal) {
            closeModal(openModal.id);
        }
        if (imageModal && imageModal.style.display === 'block') {
            closeImageModal();
        }
    }
});

window.addEventListener('resize', () => {
    if (imageModal && imageModal.style.display === 'block') {
        closeImageModal();
    }
});
window.addEventListener('orientationchange', () => {
    if (imageModal && imageModal.style.display === 'block') {
        closeImageModal();
    }
});