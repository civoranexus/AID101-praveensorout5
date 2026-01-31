/**
 * AgriAssist AI - Crop Health Upload Script
 * Phase 2: Farmer Dashboard Integration
 *
 * Handles crop health image uploads and displays inference results.
 */

document.addEventListener("DOMContentLoaded", () => {
    const cropHealthForm = document.getElementById("cropHealthForm");
    const resultContainer = document.getElementById("cropHealthResult");

    if (cropHealthForm) {
        cropHealthForm.addEventListener("submit", async (e) => {
            e.preventDefault();

            const farmId = document.getElementById("farmId").value;
            const fileInput = document.getElementById("cropImage");
            const file = fileInput.files[0];

            if (!file) {
                resultContainer.innerHTML = "<p class='error'>Please select an image file.</p>";
                return;
            }

            // Prepare form data
            const formData = new FormData();
            formData.append("farm_id", farmId);
            formData.append("crop_image", file);

            resultContainer.innerHTML = "<p>Uploading crop image...</p>";

            try {
                // Upload image to backend
                const response = await fetch("/api/crop-health/upload", {
                    method: "POST",
                    body: formData
                });

                if (!response.ok) throw new Error("Failed to upload crop health data");
                const result = await response.json();

                resultContainer.innerHTML = `<p>${result.message}</p>`;

                // Call inference endpoint
                const inferenceResponse = await fetch("/api/crop-health/infer", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ farm_id: farmId, file_name: file.name })
                });

                if (inferenceResponse.ok) {
                    const inference = await inferenceResponse.json();
                    resultContainer.innerHTML += `
                        <div class="advisory-card">
                            <strong>Status:</strong> ${inference.status}<br>
                            <strong>Confidence:</strong> ${(inference.confidence * 100).toFixed(2)}%
                        </div>
                    `;
                } else {
                    resultContainer.innerHTML += "<p class='error'>Inference service unavailable.</p>";
                }
            } catch (err) {
                resultContainer.innerHTML = `<p class='error'>Error: ${err.message}</p>`;
            }
        });
    }
});
