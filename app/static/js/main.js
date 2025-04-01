document.addEventListener('DOMContentLoaded', function() {
    const promptInput = document.getElementById('prompt');
    const negativePromptInput = document.getElementById('negative-prompt');
    const widthInput = document.getElementById('width');
    const heightInput = document.getElementById('height');
    const stepsInput = document.getElementById('steps');
    const guidanceInput = document.getElementById('guidance');
    const generateBtn = document.getElementById('generate-btn');
    const loadingDiv = document.getElementById('loading');
    const resultDiv = document.getElementById('result');
    const errorDiv = document.getElementById('error');
    const generatedImage = document.getElementById('generated-image');
    const downloadBtn = document.getElementById('download-btn');
    const newGenerationBtn = document.getElementById('new-generation-btn');
    const advancedOptionsToggle = document.querySelector('.advanced-options-toggle');
    const advancedOptions = document.querySelector('.advanced-options');
    const toggleIcon = document.querySelector('.toggle-icon');

    // Toggle advanced options
    advancedOptionsToggle.addEventListener('click', function() {
        advancedOptions.classList.toggle('show');
        toggleIcon.textContent = advancedOptions.classList.contains('show') ? '▲' : '▼';
    });

    // Generate image
    generateBtn.addEventListener('click', function() {
        const prompt = promptInput.value.trim();
        if (!prompt) {
            alert('Please enter a text prompt');
            return;
        }

        // Show loading, hide result and error
        loadingDiv.classList.remove('hidden');
        resultDiv.classList.add('hidden');
        errorDiv.classList.add('hidden');

        // Prepare request data
        const requestData = {
            prompt: prompt,
            negative_prompt: negativePromptInput.value.trim(),
            width: parseInt(widthInput.value),
            height: parseInt(heightInput.value),
            num_inference_steps: parseInt(stepsInput.value),
            guidance_scale: parseFloat(guidanceInput.value)
        };

        // Send API request
        fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestData)
        })
        .then(response => response.json())
        .then(data => {
            loadingDiv.classList.add('hidden');
            
            if (data.success) {
                // Display the image
                generatedImage.src = `data:image/png;base64,${data.image}`;
                generatedImage.setAttribute('data-filename', data.filename);
                resultDiv.classList.remove('hidden');
            } else {
                // Show error
                errorDiv.querySelector('.error-message').textContent = data.error || 'An error occurred';
                errorDiv.classList.remove('hidden');
            }
        })
        .catch(error => {
            loadingDiv.classList.add('hidden');
            errorDiv.querySelector('.error-message').textContent = 'Network error: ' + error.message;
            errorDiv.classList.remove('hidden');
            console.error('Error:', error);
        });
    });

    // Download image functionality
    downloadBtn.addEventListener('click', function() {
        const imageData = generatedImage.src;
        const filename = generatedImage.getAttribute('data-filename') || 'generated-image.png';
        
        const link = document.createElement('a');
        link.href = imageData;
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });

    // Create new image button
    newGenerationBtn.addEventListener('click', function() {
        resultDiv.classList.add('hidden');
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});
