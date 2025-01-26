document.addEventListener('DOMContentLoaded', function() {
    // Mobile Navigation Toggle
    const navToggle = document.querySelector('.nav-toggle');
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            const nav = document.querySelector('nav');
            nav.classList.toggle('active');
            this.classList.toggle('active');
        });
    }

    // Delete Confirmation
    document.querySelectorAll('.btn-danger').forEach(button => {
        button.addEventListener('click', (e) => {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });

    // Form Validation
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            let isValid = true;
            const requiredFields = this.querySelectorAll('[required]');

            requiredFields.forEach(field => {
                field.classList.remove('error');
                const existingError = field.parentNode.querySelector('.error-message');
                if (existingError) existingError.remove();

                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                    const errorMsg = document.createElement('div');
                    errorMsg.className = 'error-message';
                    errorMsg.textContent = 'This field is required';
                    field.parentNode.insertBefore(errorMsg, field.nextSibling);
                }
            });

            if (!isValid) {
                e.preventDefault();
                this.querySelector('.error').focus();
            }
        });
    });

    // Dynamic Date Input for Payments
    const paymentDateFields = document.querySelectorAll('input[type="date"]');
    paymentDateFields.forEach(field => {
        if (!field.value) {
            const today = new Date().toISOString().split('T')[0];
            field.value = today;
        }
    });

    // Auto-format Currency Inputs
    const currencyFields = document.querySelectorAll('input[data-type="currency"]');
    currencyFields.forEach(field => {
        field.addEventListener('input', function(e) {
            let value = this.value.replace(/[^0-9.]/g, '');
            if (value) {
                value = parseFloat(value).toFixed(2);
                this.value = `$${value}`;
            }
        });
    });
});

// Error Message Styling
const style = document.createElement('style');
style.textContent = `
    .error {
        border-color: #e74c3c !important;
        background-color: #fceae9;
    }
    .error-message {
        color: #e74c3c;
        font-size: 0.875rem;
        margin-top: 0.25rem;
    }
`;
document.head.appendChild(style);