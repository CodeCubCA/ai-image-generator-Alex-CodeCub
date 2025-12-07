[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zrsH8x_3)

# AI Image Generator

A web-based AI image generator powered by HuggingFace's FLUX.1-schnell model and built with Streamlit.

## Features

- Generate stunning images from text descriptions
- Fast image generation using FLUX.1-schnell model
- Clean and intuitive user interface
- Download generated images
- Comprehensive error handling
- Built-in usage tips and example prompts

## Prerequisites

- Python 3.8 or higher
- HuggingFace account with API token (with Write permissions)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/CodeCubCA/ai-image-generator-Alex-CodeCub.git
cd ai-image-generator
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your HuggingFace API token:
   - Go to https://huggingface.co/settings/tokens
   - Create a new token with **Write** permissions
   - Copy the `.env.example` file to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your token:
     ```
     HUGGINGFACE_TOKEN=your_token_here
     ```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to:
   - Local: http://localhost:8501
   - Network: http://192.168.1.92:8501

3. Enter a description of the image you want to generate

4. Click "Generate Image" and wait for the AI to create your image

5. Download your generated image using the download button

## Example Prompts

- "A serene lake at sunset, oil painting style, warm colors"
- "A futuristic city at night, cyberpunk style, neon lights"
- "A cute cat wearing a wizard hat, digital art, detailed"
- "Mountain landscape with aurora borealis, photorealistic"

## Tips for Better Results

- Be specific and descriptive in your prompts
- Include style, mood, and details
- Mention lighting and colors
- Specify the desired art style (e.g., oil painting, digital art, photorealistic)

## Project Structure

```
ai-image-generator/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in git)
├── .env.example          # Example environment file
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Dependencies

- `streamlit` - Web framework for the UI
- `huggingface_hub` - Official HuggingFace API client
- `python-dotenv` - Environment variable management
- `Pillow` - Image processing library

## Technical Details

### Model
- **FLUX.1-schnell** by Black Forest Labs
- Fast, high-quality image generation
- Publicly accessible via HuggingFace Inference API

### API
- Uses HuggingFace's `InferenceClient` from `huggingface_hub`
- Serverless inference for zero infrastructure management
- Automatic endpoint routing and error handling

## Limitations

- Free tier has rate limits
- Image generation may take 10-30 seconds
- Model needs to load on first request (cold start)

## Troubleshooting

### Authentication Error (401)
- Ensure your HuggingFace token has **Write** permissions
- Check that the token is correctly set in the `.env` file

### Rate Limit Error (429)
- Wait a few minutes before trying again
- Consider upgrading to HuggingFace PRO for higher limits

### Model Loading Error (503)
- Wait a moment and try again
- The model may be loading (cold start)

## License

This project is created for educational purposes.

## Acknowledgments

- HuggingFace for providing the Inference API
- Black Forest Labs for the FLUX.1-schnell model
- Streamlit for the web framework

## Author

Created as part of CodeCub's AI/ML course assignment.
