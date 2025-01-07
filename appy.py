<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Language Translator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      padding: 20px;
      background-color: #f4f4f9;
    }

    .container {
      max-width: 600px;
      margin: auto;
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    textarea {
      width: 100%;
      height: 100px;
      margin: 10px 0;
      padding: 10px;
      border-radius: 5px;
      border: 1px solid #ccc;
    }

    button {
      padding: 10px 20px;
      border: none;
      background: #4CAF50;
      color: white;
      border-radius: 5px;
      cursor: pointer;
    }

    button:hover {
      background: #45a049;
    }

    select {
      width: 100%;
      padding: 10px;
      margin: 10px 0;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Language Translator</h1>
    <textarea id="inputText" placeholder="Type text here..."></textarea>

    <select id="languageSelector">
      <option value="es">Spanish</option>
      <option value="fr">French</option>
      <option value="de">German</option>
      <option value="hi">Hindi</option>
      <!-- Add more languages as needed -->
    </select>

    <button id="translateBtn">Translate</button>
    <textarea id="outputText" placeholder="Translation will appear here..." readonly></textarea>
  </div>

  <script>
    document.getElementById('translateBtn').addEventListener('click', async () => {
      const inputText = document.getElementById('inputText').value;
      const language = document.getElementById('languageSelector').value;

      if (!inputText.trim()) {
        alert('Please enter text to translate!');
        return;
      }

      try {
        const response = await fetch('https://libretranslate.com/translate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            q: inputText,
            source: 'en',
            target: language,
            format: 'text'
          }),
        });

        const data = await response.json();
        document.getElementById('outputText').value = data.translatedText;
      } catch (error) {
        console.error('Error:', error);
        alert('Failed to translate. Please try again later.');
      }
    });
  </script>
</body>
</html>
