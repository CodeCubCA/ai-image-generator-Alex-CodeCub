import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv()

# Configuration
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
MODEL_NAME = "black-forest-labs/FLUX.1-schnell"

# Initialize InferenceClient
client = InferenceClient(token=HUGGINGFACE_TOKEN)

# Page configuration
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="centered"
)

def generate_image(prompt):
    """
    Generate an image using HuggingFace InferenceClient

    Args:
        prompt (str): Text description of the image to generate

    Returns:
        PIL.Image: Generated image or None if failed
    """
    try:
        # Use InferenceClient's text_to_image method
        image = client.text_to_image(prompt, model=MODEL_NAME)
        return image
    except Exception as e:
        error_msg = str(e)

        # Handle specific error cases
        if "503" in error_msg or "loading" in error_msg.lower():
            st.error("⏳ Model is currently loading. Please wait a moment and try again.")
        elif "429" in error_msg or "rate limit" in error_msg.lower():
            st.error("⚠️ Rate limit reached. Please wait a few minutes before trying again.")
        elif "401" in error_msg or "unauthorized" in error_msg.lower():
            st.error("🔒 Authentication failed. Please check your HuggingFace token has 'Write' permissions.")
        else:
            st.error(f"❌ An error occurred: {error_msg}")

        return None

def main():
    # Header
    st.title("🎨 AI Image Generator")
    st.markdown("Generate stunning images from text using AI powered by FLUX.1-schnell")

    # Check if API token is configured
    if not HUGGINGFACE_TOKEN:
        st.error("⚠️ HuggingFace API token not found!")
        st.info("""
        **Setup Instructions:**
        1. Go to https://huggingface.co/settings/tokens
        2. Create a new token with 'Write' permissions
        3. Add it to the `.env` file as: `HUGGINGFACE_TOKEN=your_token_here`
        """)
        st.stop()

    # Sidebar with information
    with st.sidebar:
        st.header("ℹ️ About")
        st.write(f"**Model:** {MODEL_NAME}")
        st.write("FLUX.1-schnell is a fast, high-quality image generation model by Black Forest Labs.")

        st.markdown("---")

        st.header("💡 Tips for Better Results")
        st.write("- Be specific and descriptive")
        st.write("- Include style, mood, and details")
        st.write("- Mention lighting and colors")
        st.write("- Specify art style if desired")

        st.markdown("---")

        st.header("📝 Example Prompts")
        st.code("A serene lake at sunset, oil painting style, warm colors")
        st.code("A futuristic city at night, cyberpunk style, neon lights")
        st.code("A cute cat wearing a wizard hat, digital art, detailed")
        st.code("Mountain landscape with aurora borealis, photorealistic")

        st.markdown("---")

        st.info("**Note:** Free tier has rate limits. If you encounter errors, wait a few minutes.")

    # Main content area
    st.markdown("---")

    # Input section
    prompt = st.text_area(
        "✍️ Enter your image description:",
        placeholder="Example: A magical forest with glowing mushrooms, fantasy art style, vibrant colors",
        height=120,
        help="Describe the image you want to generate. Be as detailed as possible!"
    )

    # Generate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_button = st.button("🚀 Generate Image", use_container_width=True, type="primary")

    # Generation logic
    if generate_button:
        if not prompt.strip():
            st.warning("⚠️ Please enter a description for your image.")
        else:
            with st.spinner("🎨 Creating your image... This may take 10-30 seconds..."):
                image = generate_image(prompt)

                if image:
                    st.success("✅ Image generated successfully!")

                    # Display the generated image
                    st.image(image, caption=f"Generated: {prompt}", use_container_width=True)

                    # Download button
                    buf = BytesIO()
                    image.save(buf, format="PNG")
                    byte_im = buf.getvalue()

                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col2:
                        st.download_button(
                            label="⬇️ Download Image",
                            data=byte_im,
                            file_name=f"ai_generated_{prompt[:30].replace(' ', '_')}.png",
                            mime="image/png",
                            use_container_width=True
                        )

    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>Built with ❤️ using Streamlit & HuggingFace FLUX.1-schnell</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
