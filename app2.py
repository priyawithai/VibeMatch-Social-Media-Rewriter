from flask import Flask, request, jsonify
from flask_cors import CORS
import urllib.parse

app = Flask(__name__)
CORS(app, origins="https://preview--wise-post-flow.lovable.app")  # Replace with your actual frontend domain

# --- Tone Converters ---
def convert_to_instagram_tone(text):
    text = text.replace("!", " ✨").replace("great", "amazing").replace("good", "awesome")
    sentences = text.split('.')
    instagram_text = ''.join(f"{s.strip()} 💫\n" for s in sentences if s.strip())
    instagram_text += "\n👆 Double tap if you agree!\n#motivation #inspiration #success"
    return instagram_text

def convert_to_facebook_tone(text):
    text = text.replace("you", "we").replace("I think", "What do you think")
    return f"Hey friends! 👋\n\n{text}\n\nWhat's your experience with this? Let me know in the comments! 💭"

def convert_to_linkedin_tone(text):
    text = text.replace("awesome", "valuable").replace("amazing", "significant").replace("!", ".")
    return (
        "Professional insight: 💼\n\n" + text +
        "\n\nWhat are your thoughts on this approach? I'd love to hear from fellow professionals in the comments."
        "\n\n#Leadership #BusinessStrategy #ProfessionalDevelopment"
    )

def convert_to_whatsapp_tone(text):
    return f"Hey! 👋\n\n{text.replace('Hello', 'Hey').replace('.', ' 😊')}\n\nLet me know what you think! 💭"

def convert_to_twitter_tone(text):
    if len(text) > 240:
        truncated = ' '.join(text.split()[:30]) + "..."
        return f"{truncated}\n\n🧵 Thread below 👇\n#TwitterThread"
    return text + "\n\n#SocialMedia #ContentCreation"

# --- Link Generator (Optional) ---
def generate_links(platform, content):
    encoded = urllib.parse.quote(content)
    priya_accounts = {
        'instagram': 'https://www.instagram.com/learn_ai_with_priya/',
        'facebook': 'https://www.facebook.com/profile.php?id=61578258155366',
        'linkedin': 'https://www.linkedin.com/in/priyawithai/',
        'whatsapp': 'https://wa.me/message/TXE74MCSDJTUO1'
    }

    links = {}
    if platform == 'Facebook':
        links['Post'] = f"https://www.facebook.com/sharer/sharer.php?quote={encoded}"
        links['Profile'] = priya_accounts['facebook']
    elif platform == 'Instagram':
        links['App'] = "https://www.instagram.com/"
        links['Profile'] = priya_accounts['instagram']
    elif platform == 'LinkedIn':
        links['Post'] = f"https://www.linkedin.com/feed/?shareActive=true&text={encoded}"
        links['Profile'] = priya_accounts['linkedin']
    elif platform == 'Twitter/X':
        links['Tweet'] = f"https://twitter.com/intent/tweet?text={encoded}"
    elif platform == 'WhatsApp':
        links['Send'] = f"https://wa.me/?text={encoded}"
        links['Message Priya'] = priya_accounts['whatsapp']

    return links

# --- Main Conversion Route ---
@app.route('/', methods=['POST', 'OPTIONS'])
def convert_content():
    if request.method == 'OPTIONS':
        return '', 200

    try:
        if not request.is_json:
            return jsonify({'error': 'Request must be in JSON format'}), 400

        data = request.get_json()
        content = data.get('content', '').strip()

        if not content:
            return jsonify({'error': 'No content provided'}), 400

        converted = {
            'Instagram': convert_to_instagram_tone(content),
            'Facebook': convert_to_facebook_tone(content),
            'LinkedIn': convert_to_linkedin_tone(content),
            'WhatsApp': convert_to_whatsapp_tone(content),
            'Twitter/X': convert_to_twitter_tone(content)
        }

        return jsonify({'original': content, 'converted': converted}), 200

    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({'error': str(e)}), 500

# --- Optional Link Generator Endpoint ---
@app.route('/links/<platform>', methods=['POST'])
def platform_links(platform):
    try:
        if not request.is_json:
            return jsonify({'error': 'Request must be in JSON format'}), 400

        data = request.get_json()
        content = data.get('content', '').strip()

        if not content:
            return jsonify({'error': 'No content provided'}), 400

        links = generate_links(platform, content)
        return jsonify({'platform': platform, 'links': links}), 200

    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({'error': str(e)}), 500

# --- Run App ---
if __name__ == '__main__':
    app.run(debug=True)
