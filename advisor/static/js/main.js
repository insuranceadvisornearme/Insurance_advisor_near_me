document.addEventListener('DOMContentLoaded', function() {
    // Plan selection handler
    document.getElementById('plan_interest').addEventListener('change', function() {
        const selectedPlan = this.value;
        if (selectedPlan) {
            // Here you can add logic to show plan details
            // For example, redirect to a plan details page or show a modal
            console.log("Selected plan:", selectedPlan);
            
            // Example of showing plan details in a modal
            showPlanDetails(selectedPlan);
        }
    });

    // Form submission handler
    document.getElementById('inquiryForm').addEventListener('submit', function(e) {
        e.preventDefault();
        const form = e.target;
        const formData = new FormData(form);
        
        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Thank you! We will contact you shortly.');
                form.reset();
            }
        })
        .catch(error => console.error('Error:', error));
    });

    // Initialize any other functionality
    initSmoothScrolling();
});

function showPlanDetails(planName) {
    // This is a placeholder - you would typically fetch plan details from your backend
    const planDetails = {
        name: planName,
        description: "This is a comprehensive life insurance plan that provides both protection and savings benefits.",
        features: [
            "Life cover for the entire policy term",
            "Guaranteed maturity benefit",
            "Bonus additions",
            "Loan facility available",
            "Tax benefits under Section 80C & 10(10D)"
        ],
        eligibility: "Minimum age: 18 years, Maximum age: 60 years"
    };

    // Create modal HTML
    const modalHtml = `
        <div class="modal-overlay">
            <div class="modal-content">
                <button class="close-modal">&times;</button>
                <h3>${planDetails.name}</h3>
                <p><strong>Description:</strong> ${planDetails.description}</p>
                <h4>Key Features:</h4>
                <ul>
                    ${planDetails.features.map(feature => `<li>${feature}</li>`).join('')}
                </ul>
                <p><strong>Eligibility:</strong> ${planDetails.eligibility}</p>
                <div class="modal-actions">
                    <a href="tel:+917620485529" class="btn btn-primary">Call to Enroll</a>
                    <button class="btn btn-outline-primary close-modal-btn">Close</button>
                </div>
            </div>
        </div>
    `;
    
    // Add modal to DOM
    document.body.insertAdjacentHTML('beforeend', modalHtml);
    
    // Add event listeners for modal
    document.querySelector('.close-modal').addEventListener('click', closeModal);
    document.querySelector('.close-modal-btn').addEventListener('click', closeModal);
    document.querySelector('.modal-overlay').addEventListener('click', function(e) {
        if (e.target === this) closeModal();
    });
}

function closeModal() {
    const modal = document.querySelector('.modal-overlay');
    if (modal) modal.remove();
}

function initSmoothScrolling() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
}

// Additional utility functions can be added here