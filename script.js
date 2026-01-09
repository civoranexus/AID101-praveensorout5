// Smooth scroll for navigation
document.querySelector("nav").addEventListener("click", e => {
  if (e.target.tagName === "A") {
    e.preventDefault();
    const targetId = e.target.getAttribute("href").slice(1);
    document.getElementById(targetId)?.scrollIntoView({ behavior: "smooth" });
  }
});

// Feature click alert
document.addEventListener("click", e => {
  const feature = e.target.closest(".feature");
  if (feature) {
    alert(`You clicked on: ${feature.querySelector("h3").innerText}`);
  }
});

// Dynamic footer year
const footerText = document.querySelector("footer p");
if (footerText) {
  footerText.textContent = `© ${new Date().getFullYear()} Agri Assist. All rights reserved.`;
}

// Toggle contact info
const contactSection = document.getElementById("contact");
if (contactSection) {
  const toggleBtn = Object.assign(document.createElement("button"), {
    textContent: "Toggle Contact Info",
    className: "toggle-btn"
  });
  contactSection.appendChild(toggleBtn);

  toggleBtn.addEventListener("click", () => {
    contactSection.querySelectorAll("p").forEach(p => {
      p.hidden = !p.hidden;
    });
  });
}

// Crop Advisory Form Logic
const advisoryForm = document.getElementById("advisoryForm");
if (advisoryForm) {
  advisoryForm.addEventListener("submit", e => {
    e.preventDefault();
    const crop = advisoryForm.crop.value.trim().toLowerCase();
    const output = document.getElementById("adviceOutput");

    const adviceMap = {
      wheat: "🌾 Wheat grows best in cool climates. Ensure timely irrigation during critical growth stages.",
      rice: "🍚 Rice requires standing water. Monitor rainfall and consider alternate wetting and drying for sustainability.",
      maize: "🌽 Maize needs well-drained soil. Apply nitrogen fertilizer in split doses for better yield.",
      cotton: "🧵 Cotton thrives in warm climates. Watch for pests like bollworms and use integrated pest management."
    };

    output.textContent = adviceMap[crop] || "❓ No specific advice found. Please consult local experts or extension services.";
    Object.assign(output.style, { marginTop: "1rem", fontWeight: "500", color: "#2e7d32" });
  });
}
