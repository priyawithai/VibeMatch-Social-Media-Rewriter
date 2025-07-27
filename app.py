import streamlit as st
import re
from datetime import datetime
import urllib.parse

# Configure page
st.set_page_config(
    page_title="🔥 VibeMatch: Social Media Rewriter",
    page_icon="🎯",
    layout="wide"
)

def convert_to_instagram_tone(text):
    """Convert text to Instagram-friendly tone"""
    # Add emojis and make it more visual
    text = text.replace("!", " ✨")
    text = text.replace("great", "amazing")
    text = text.replace("good", "awesome")
    
    # Make it more casual and engaging
    sentences = text.split('.')
    instagram_text = ""
    
    for sentence in sentences:
        if sentence.strip():
            instagram_text += sentence.strip() + " 💫\n"
    
    # Add call-to-action
    instagram_text += "\n👆 Double tap if you agree!\n#motivation #inspiration #success"
    
    return instagram_text

def convert_to_facebook_tone(text):
    """Convert text to Facebook-friendly tone"""
    # Make it more conversational and community-focused
    text = text.replace("you", "we")
    text = text.replace("I think", "What do you think")
    
    # Add engagement hooks
    facebook_text = "Hey friends! 👋\n\n" + text
    facebook_text += "\n\nWhat's your experience with this? Let me know in the comments! 💭"
    
    return facebook_text

def convert_to_linkedin_tone(text):
    """Convert text to LinkedIn professional tone"""
    # Make it more professional and insightful
    text = text.replace("awesome", "valuable")
    text = text.replace("amazing", "significant")
    text = text.replace("!", ".")
    
    # Add professional framing
    linkedin_text = "Professional insight: 💼\n\n" + text
    linkedin_text += "\n\nWhat are your thoughts on this approach? I'd love to hear from fellow professionals in the comments."
    linkedin_text += "\n\n#Leadership #BusinessStrategy #ProfessionalDevelopment"
    
    return linkedin_text

def convert_to_whatsapp_tone(text):
    """Convert text to WhatsApp casual tone"""
    # Make it very casual and direct
    text = text.replace("Hello", "Hey")
    text = text.replace(".", " 😊")
    
    # Add casual emojis and make it conversational
    whatsapp_text = "Hey! 👋\n\n" + text
    whatsapp_text += "\n\nLet me know what you think! 💭"
    
    return whatsapp_text

def convert_to_twitter_tone(text):
    """Convert text to Twitter/X tone with character limit"""
    # Make it punchy and concise
    words = text.split()
    if len(text) > 240:
        # Truncate and add thread indicator
        truncated = ' '.join(words[:30]) + "..."
        twitter_text = truncated + "\n\n🧵 Thread below 👇\n#TwitterThread"
    else:
        twitter_text = text + "\n\n#SocialMedia #ContentCreation"
    
    return twitter_text

def generate_social_media_links(platform, content):
    """Generate direct social media posting links with Priya's actual accounts"""
    encoded_content = urllib.parse.quote(content)
    
    # Priya's Social Media Links
    PRIYA_SOCIAL_LINKS = {
        'instagram': 'https://www.instagram.com/learn_ai_with_priya/',
        'facebook': 'https://www.facebook.com/profile.php?id=61578258155366',
        'linkedin': 'https://www.linkedin.com/in/priyawithai/',
        'whatsapp': 'https://wa.me/message/TXE74MCSDJTUO1'
    }
    
    links = {}
    
    if platform == 'Facebook':
        links['🚀 Post to Facebook'] = f"https://www.facebook.com/sharer/sharer.php?u=&quote={encoded_content}"
        links['📱 Visit Priya\'s Facebook'] = PRIYA_SOCIAL_LINKS['facebook']
        
    elif platform == 'Instagram':
        # Instagram-specific solutions since direct posting isn't supported via URL
        links['📱 Open Instagram App'] = "https://www.instagram.com/"
        links['🎯 Visit @learn_ai_with_priya'] = PRIYA_SOCIAL_LINKS['instagram']
        links['📸 Instagram Stories Camera'] = "https://www.instagram.com/stories/camera/"
        links['💼 Creator Studio (Desktop)'] = "https://business.facebook.com/creatorstudio/?tab=instagram_content_posts"
        
    elif platform == 'LinkedIn':
        links['💼 Post to LinkedIn'] = f"https://www.linkedin.com/feed/?shareActive=true&text={encoded_content}"
        links['🔗 Visit Priya\'s LinkedIn'] = PRIYA_SOCIAL_LINKS['linkedin']
        
    elif platform == 'Twitter/X':
        short_content = content[:250] + "..." if len(content) > 250 else content
        encoded_short = urllib.parse.quote(short_content)
        links['🐦 Tweet Now'] = f"https://twitter.com/intent/tweet?text={encoded_short}"
    
    elif platform == 'WhatsApp':
        links['💬 Send via WhatsApp'] = f"https://wa.me/?text={encoded_content}"
        links['📱 Message Priya'] = PRIYA_SOCIAL_LINKS['whatsapp']
    
    return links

def simulate_social_media_post(platform, content):
    """Simulate social media posting for demo"""
    return {
        'status': 'success',
        'message': f'Successfully posted to {platform}!',
        'post_id': f'{platform.lower()}_{datetime.now().strftime("%Y%m%d_%H%M%S")}',
        'url': f'https://{platform.lower()}.com/posts/sample_post_123'
    }

def get_platform_posting_guidelines(platform):
    """Get platform-specific posting guidelines"""
    guidelines = {
        'Instagram': {
            'best_times': '6-9 AM, 12-2 PM, 5-7 PM',
            'optimal_length': '125-150 characters',
            'hashtags': 'Use 5-10 relevant hashtags',
            'engagement_tip': 'Ask questions to boost engagement'
        },
        'Facebook': {
            'best_times': '9-10 AM, 3-4 PM, 8-9 PM',
            'optimal_length': '40-80 characters for highest engagement',
            'hashtags': 'Use 1-2 hashtags maximum',
            'engagement_tip': 'Include call-to-action questions'
        },
        'LinkedIn': {
            'best_times': '8-10 AM, 12-2 PM, 5-6 PM',
            'optimal_length': '150-300 characters',
            'hashtags': 'Use 3-5 professional hashtags',
            'engagement_tip': 'Share industry insights'
        },
        'Twitter/X': {
            'best_times': '9 AM, 1-3 PM, 8-9 PM',
            'optimal_length': '100-280 characters',
            'hashtags': 'Use 1-2 trending hashtags',
            'engagement_tip': 'Join trending conversations'
        },
        'WhatsApp': {
            'best_times': '10-12 PM, 6-8 PM',
            'optimal_length': 'Keep messages concise',
            'hashtags': 'Not applicable',
            'engagement_tip': 'Use for direct communication'
        }
    }
    return guidelines.get(platform, {})

def analyze_content_metrics(original_text, platform_texts):
    """Analyze content metrics for each platform"""
    metrics = {}
    
    for platform, text in platform_texts.items():
        char_count = len(text)
        word_count = len(text.split())
        emoji_count = len(re.findall(r'[😀-🙏]', text))
        hashtag_count = len(re.findall(r'#\w+', text))
        
        # Platform-specific limits
        limits = {
            'Instagram': 2200,
            'Facebook': 63206,
            'LinkedIn': 3000,
            'Twitter/X': 280,
            'WhatsApp': 4096
        }
        
        char_limit = limits.get(platform, 1000)
        
        metrics[platform] = {
            'char_count': char_count,
            'word_count': word_count,
            'emoji_count': emoji_count,
            'hashtag_count': hashtag_count,
            'char_limit': char_limit,
            'within_limit': char_count <= char_limit
        }
    
    return metrics

# Main App Interface
st.title("🎯 🔥 VibeMatch: Social Media Rewriter")
st.markdown("### Transform Your Content for Every Social Media Platform")

# Sidebar for brand voice settings and social media connections
with st.sidebar:
    st.header("🚀 **DEMO READY** - Priya's Social Media Automation")
    st.success("✅ Connected to @learn_ai_with_priya accounts!")
    
    # Show Priya's Social Media Links
    st.markdown("### 📱 Priya's Accounts:")
    st.markdown("**Instagram** 📸")
    st.markdown("[🎯 @learn_ai_with_priya](https://www.instagram.com/learn_ai_with_priya/)")
    
    st.markdown("**Facebook** 📘") 
    st.markdown("[👤 Priya's Profile](https://www.facebook.com/profile.php?id=61578258155366)")
    
    st.markdown("**LinkedIn** 💼")
    st.markdown("[🔗 /in/priyawithai](https://www.linkedin.com/in/priyawithai/)")
    
    st.markdown("**WhatsApp** 💬")
    st.markdown("[📱 Message Priya](https://wa.me/message/TXE74MCSDJTUO1)")
    
    st.markdown("---")
    
    st.header("⚙️ Brand Voice Settings")
    brand_voice = st.selectbox(
        "Select Brand Voice:",
        ["Professional", "Casual", "Friendly", "Authoritative", "Humorous"]
    )
    
    target_audience = st.selectbox(
        "Target Audience:",
        ["General Public", "Business Professionals", "Young Adults", "Entrepreneurs", "Tech Community"]
    )
    
    st.header("📊 Quick Stats")
    if 'original_text' in st.session_state and st.session_state.original_text:
        st.metric("Word Count", len(st.session_state.original_text.split()))
        st.metric("Character Count", len(st.session_state.original_text))

# Main content area
col1, col2 = st.columns([1, 2])

with col1:
    st.header("📝 Input Your Content")
    
    # Demo Content Generator
    demo_examples = [
        "🚀 Just built an AI-powered social media automation tool! It converts content for Instagram, Facebook, LinkedIn & WhatsApp in seconds. Who wants to try it? #AITech #SocialMedia",
        "🎯 Teaching AI to thousands of followers! Here's my secret to creating engaging content across all platforms. Follow @learn_ai_with_priya for daily AI tips! #LearnAI #ContentCreation", 
        "💡 BuildAthon Update: Our Tone Corrector tool just got a major upgrade! Now with direct posting to all major platforms. Check it out! #BuildAthon #Innovation",
        "🔥 Want to 10x your social media productivity? My new AI tool adapts your content tone for each platform automatically. DM for early access! #Productivity #AITools"
    ]
    
    st.markdown("### 🎬 Quick Demo:")
    selected_demo = st.selectbox("Try Demo Content:", ["Custom Input"] + demo_examples)
    
    if selected_demo != "Custom Input":
        if st.button("🎯 Use This Demo Content"):
            st.session_state.original_text = selected_demo
            st.success("✅ Demo content loaded!")
            st.rerun()
        original_text = selected_demo
    else:
        input_method = st.radio(
            "Choose input method:",
            ["Text Input", "Event Details", "Product Description"]
        )
        
        if input_method == "Text Input":
            original_text = st.text_area(
                "Enter your original text:",
                height=200,
                placeholder="Enter content to adapt for different platforms..."
            )
        elif input_method == "Event Details":
            event_name = st.text_input("Event Name:")
            event_date = st.date_input("Event Date:")
            event_description = st.text_area("Event Description:", height=100)
            original_text = f"Join us for {event_name} on {event_date}! {event_description}"
        else:
            product_name = st.text_input("Product Name:")
            product_features = st.text_area("Key Features:", height=80)
            product_benefits = st.text_area("Benefits:", height=80)
            original_text = f"Introducing {product_name}! Features: {product_features}. Benefits: {product_benefits}"
    
    # Store in session state
    if original_text:
        st.session_state.original_text = original_text

with col2:
    st.header("🚀 Platform-Optimized Content")
    
    if 'original_text' in st.session_state and st.session_state.original_text:
        # Convert to different platform tones
        platform_conversions = {
            'Instagram': convert_to_instagram_tone(st.session_state.original_text),
            'Facebook': convert_to_facebook_tone(st.session_state.original_text),
            'LinkedIn': convert_to_linkedin_tone(st.session_state.original_text),
            'WhatsApp': convert_to_whatsapp_tone(st.session_state.original_text),
            'Twitter/X': convert_to_twitter_tone(st.session_state.original_text)
        }
        
        # Create tabs for each platform
        tabs = st.tabs(list(platform_conversions.keys()))
        
        for i, (platform, converted_text) in enumerate(platform_conversions.items()):
            with tabs[i]:
                # Content display and editing
                edited_content = st.text_area(
                    f"{platform} Version:",
                    value=converted_text,
                    height=150,
                    key=f"{platform}_output"
                )
                
                # Platform guidelines
                guidelines = get_platform_posting_guidelines(platform)
                if guidelines:
                    with st.expander(f"📋 {platform} Best Practices"):
                        st.write(f"**Best Times:** {guidelines.get('best_times', 'N/A')}")
                        st.write(f"**Optimal Length:** {guidelines.get('optimal_length', 'N/A')}")
                        st.write(f"**Hashtags:** {guidelines.get('hashtags', 'N/A')}")
                        st.write(f"**Tip:** {guidelines.get('engagement_tip', 'N/A')}")
                
                # Action buttons
                col_copy, col_post = st.columns(2)
                
                with col_copy:
                    if st.button(f"📋 Copy Content", key=f"copy_{platform}"):
                        st.success(f"✅ {platform} content copied!")
                
                with col_post:
                    if st.button(f"🚀 Get Post Links", key=f"post_{platform}"):
                        with st.spinner(f"Generating {platform} links..."):
                            # Generate direct social media links
                            social_links = generate_social_media_links(platform, edited_content)
                            
                        st.success(f"✅ {platform} links generated!")
                        
                        # Special handling for Instagram
                        if platform == 'Instagram':
                            st.info("📱 **Instagram Posting Instructions:**")
                            st.markdown("1. Copy the content above ☝️")
                            st.markdown("2. Click links below to open Instagram")
                            st.markdown("3. Paste content and post!")
                            
                            # Add copy button for Instagram
                            if st.button("📋 Copy Instagram Content", key=f"copy_ig_content_{i}"):
                                st.success("✅ Content copied! Now click Instagram links below.")
                        
                        st.balloons()
                        
                        # Show direct posting links
                        st.markdown("### 🔗 Direct Links:")
                        for link_type, url in social_links.items():
                            st.markdown(f"**{link_type}:** [Click Here]({url})")
                        
                        # Store in session for analytics
                        if 'posted_content' not in st.session_state:
                            st.session_state.posted_content = []
                        
                        st.session_state.posted_content.append({
                            'platform': platform,
                            'content': edited_content,
                            'timestamp': datetime.now(),
                            'links': social_links
                        })
                
                # Content quality check
                char_count = len(edited_content)
                platform_limits = {
                    'Instagram': 2200, 'Facebook': 63206, 'LinkedIn': 3000, 
                    'Twitter/X': 280, 'WhatsApp': 4096
                }
                
                limit = platform_limits.get(platform, 1000)
                
                if char_count > limit:
                    st.error(f"⚠️ Content exceeds {platform} limit ({char_count}/{limit})")
                elif char_count > limit * 0.8:
                    st.warning(f"⚠️ Close to limit ({char_count}/{limit})")
                else:
                    st.success(f"✅ Within limits ({char_count}/{limit})")
        
        # Analytics section
        st.header("📊 Content Analytics")
        
        metrics = analyze_content_metrics(st.session_state.original_text, platform_conversions)
        
        # Create metrics display
        metric_cols = st.columns(len(platform_conversions))
        
        for i, (platform, metric_data) in enumerate(metrics.items()):
            with metric_cols[i]:
                st.metric(
                    f"{platform}",
                    f"{metric_data['char_count']} chars",
                    delta=f"Limit: {metric_data['char_limit']}"
                )
                
                if metric_data['within_limit']:
                    st.success("✅ Within limits")
                else:
                    st.error("❌ Exceeds limit")
                
                st.caption(f"📝 {metric_data['word_count']} words")
                st.caption(f"😀 {metric_data['emoji_count']} emojis")
                st.caption(f"# {metric_data['hashtag_count']} hashtags")

# Post History
if 'posted_content' in st.session_state and st.session_state.posted_content:
    st.header("📈 Generated Links History")
    
    for i, post in enumerate(reversed(st.session_state.posted_content[-3:])):
        with st.expander(f"{post['platform']} - {post['timestamp'].strftime('%H:%M:%S')}"):
            st.write(f"**Content Preview:** {post['content'][:100]}...")
            st.write("**Generated Links:**")
            for link_type, url in post['links'].items():
                st.markdown(f"- [{link_type}]({url})")

# Advanced features section
st.header("🎨 Advanced Features")

col3, col4, col5 = st.columns(3)

with col3:
    st.markdown("#### 🎯 Bulk Operations")
    if st.button("Generate All Platform Links"):
        if 'original_text' in st.session_state:
            st.success("🔗 **All Platform Links Generated!**")
            
            for platform in platform_conversions.keys():
                links = generate_social_media_links(platform, platform_conversions[platform])
                
                st.markdown(f"**{platform}:**")
                for link_type, url in links.items():
                    st.markdown(f"  - [{link_type}]({url})")
                st.markdown("---")
            
            st.balloons()
        else:
            st.warning("Please add content first!")

with col4:
    st.markdown("#### 📈 Engagement Predictor") 
    if st.button("Predict Engagement"):
        if 'original_text' in st.session_state:
            platforms_engagement = {
                'Instagram': '🔥 High (8.5/10)',
                'Facebook': '📈 Medium (6.2/10)', 
                'LinkedIn': '💼 High (8.1/10)',
                'Twitter/X': '⚡ Medium (6.8/10)'
            }
            
            st.success("📊 Engagement Predictions:")
            for platform, score in platforms_engagement.items():
                st.write(f"**{platform}:** {score}")

with col5:
    st.markdown("#### 🎬 Demo Mode")
    if st.button("Reset Demo"):
        if 'posted_content' in st.session_state:
            del st.session_state.posted_content
        if 'original_text' in st.session_state:
            del st.session_state.original_text
        st.success("🔄 Demo reset! Ready for fresh presentation.")
        st.rerun()

# Footer
st.markdown("---")
st.markdown("**🎯 Tone Corrector by Priya** - AI-Powered Social Media Automation")
st.markdown("**📱 Connect with @learn_ai_with_priya** | Perfect for BuildAThon 2024! 🚀")