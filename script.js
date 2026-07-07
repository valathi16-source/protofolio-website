// HTML-ல இருக்குற mainForm ஐடியை இங்க கரெக்டா பிடிக்கிறோம்
const contactForm = document.getElementById("mainForm");

if (contactForm) {
    contactForm.addEventListener("submit", function(event) {
        // பட்டன் அமுத்தும்போது பேஜ் ரீஃப்ரெஷ் ஆகாமல் தடுக்கும்
        event.preventDefault(); 

        // ஃபார்ம்ல இருக்குற டேட்டாவை எடுக்கும் (HTML name attributes-ஐ வச்சு)
        const formData = {
            name: contactForm.querySelector('input[name="name"]').value,
            email: contactForm.querySelector('input[name="email"]').value,
            message: contactForm.querySelector('textarea[name="message"]').value
        };

        function downloadResume() {
        window.open("Valathi_Resume.pdf");

        // FastAPI சர்வர் (Port 8080)-க்கு டேட்டாவை அனுப்புகிறது
        fetch("http://127.0.0.1:8080/contact", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error("Network response was not ok.");
        })
        .then(data => {
            // மெசேஜ் சக்சஸ்ஃபுல்லா போயிட்டா இந்த அலர்ட் வரும்
            alert("Message Sent Successfully, Bro! 🔥");
            contactForm.reset(); // ஃபார்ம் பாக்ஸ்களை காலியாக்கும்
        })
        .catch(error => {
            console.error("Error:", error);
            alert("Error sending message. Please try again.");
        });
    });
}


fetch("http://127.0.0.1:8000/contact", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name: name,
        email: email,
        message: message
    })
})
.then(res => res.json())
.then(data => {
    if (data.success) {
        alert("Message sent successfully!");
    } else {
        alert(data.message);
    }
})
.catch(err => {
    console.error(err);
    alert("Error sending message.");
});


const text = [
    "Full Stack Developer",
    "Python Developer",
    "Web Developer",
    "FastAPI Developer"
];

let textIndex = 0;
let charIndex = 0;

function typeEffect() {
    const typing = document.getElementById("typing");

    if (charIndex < text[textIndex].length) {
        typing.textContent += text[textIndex].charAt(charIndex);
        charIndex++;
        setTimeout(typeEffect, 100);
    } else {
        setTimeout(eraseEffect, 1500);
    }
}

function eraseEffect() {
    const typing = document.getElementById("typing");

    if (charIndex > 0) {
        typing.textContent = text[textIndex].substring(0, charIndex - 1);
        charIndex--;
        setTimeout(eraseEffect, 50);
    } else {
        textIndex = (textIndex + 1) % text.length;
        setTimeout(typeEffect, 300);
    }
}

typeEffect();