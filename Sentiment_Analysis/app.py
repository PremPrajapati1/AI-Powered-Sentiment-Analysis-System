
import streamlit as st
import joblib

# Page Config
st.set_page_config(
    page_title="SentimentAI | Review Analyzer",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="collapsed"
)



# CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ===== GLOBAL STYLING ===== */
.stApp {
    background: linear-gradient(
        135deg,
        #EFF6FF 0%,
        #DBEAFE 50%,
        #F0F9FF 100%
    );
    font-family: 'Inter', sans-serif;
    color: #1E3A8A;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

#MainMenu,
footer,
header {
    visibility: hidden;
}

/* ===== HERO HEADER ===== */
.hero {
    background: linear-gradient(
        120deg,
        #1D4ED8,
        #2563EB,
        #0EA5E9
    );
    padding: 38px 35px;
    border-radius: 24px;
    color: #ffffff;
    box-shadow: 0 14px 35px rgba(37, 99, 235, 0.22);
    margin-bottom: 25px;
}

.hero h1 {
    color: #ffffff !important;
    font-size: 39px !important;
    font-weight: 800 !important;
    margin: 0 0 12px 0;
}

.hero p {
    color: #DBEAFE !important;
    font-size: 16px !important;
    margin: 0;
    line-height: 1.7;
}

.eyebrow {
    color: #BFDBFE !important;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

/* ===== SECTION HEADINGS ===== */
.section-title {
    color: #1E40AF !important;
    font-size: 24px !important;
    font-weight: 800 !important;
    margin: 22px 0 16px 0 !important;
    line-height: 1.5 !important;
}

/* ===== FEATURE TITLES ===== */
.feature-title {
    color: #2563EB !important;
    font-size: 20px !important;
    font-weight: 800 !important;
    line-height: 1.5 !important;
    margin: 8px 0 10px 0 !important;
    display: block;
}

.feature-description {
    color: #334155 !important;
    font-size: 15px !important;
    font-weight: 400 !important;
    line-height: 1.7 !important;
    margin: 0 0 14px 0 !important;
    display: block;
}

/* ===== CARDS / CONTAINERS ===== */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff !important;
    color: #1E3A8A !important;
    border: 1px solid #BFDBFE !important;
    border-radius: 20px !important;
    box-shadow: 0 8px 24px rgba(30, 64, 175, 0.07);
}

/* Markdown headings inside cards */
div[data-testid="stVerticalBlockBorderWrapper"] h1,
div[data-testid="stVerticalBlockBorderWrapper"] h2,
div[data-testid="stVerticalBlockBorderWrapper"] h3,
div[data-testid="stVerticalBlockBorderWrapper"] h4 {
    color: #2563EB !important;
    font-weight: 800 !important;
}

/* Text inside cards */
div[data-testid="stVerticalBlockBorderWrapper"] p,
div[data-testid="stVerticalBlockBorderWrapper"] label {
    color: #334155 !important;
}

/* Dividers */
div[data-testid="stVerticalBlockBorderWrapper"] hr {
    border: none !important;
    border-top: 1px solid #BFDBFE !important;
    margin: 16px 0 !important;
}

/* ===== REVIEW TEXT AREA ===== */
.stTextArea textarea {
    background: #F8FBFF !important;
    border: 1px solid #BFDBFE !important;
    border-radius: 14px !important;
    color: #1E3A8A !important;
    font-size: 15px !important;
    padding: 15px !important;
}

.stTextArea textarea::placeholder {
    color: #94A3B8 !important;
}

.stTextArea textarea:focus {
    border-color: #2563EB !important;
    box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.15) !important;
}

/* ===== BUTTONS ===== */
.stButton > button {
    background: linear-gradient(
        100deg,
        #2563EB,
        #1D4ED8,
        #0284C7
    ) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    min-height: 48px;
    transition: 0.2s ease;
    box-shadow: 0 6px 16px rgba(37, 99, 235, 0.20);
}

.stButton > button:hover {
    color: #ffffff !important;
    border: none !important;
    transform: translateY(-2px);
    box-shadow: 0 10px 22px rgba(37, 99, 235, 0.30);
}

/* ===== RESULT CARDS ===== */
.result-card {
    background: #ffffff !important;
    border-radius: 18px;
    padding: 24px;
    text-align: center;
    border: 1px solid #BFDBFE;
    box-shadow: 0 8px 24px rgba(30, 64, 175, 0.07);
    min-height: 155px;
}

.result-label {
    color: #64748B !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.result-value {
    color: #2563EB !important;
    font-size: 30px !important;
    font-weight: 800 !important;
    margin-top: 12px;
}

/* ===== PROBABILITY BARS ===== */
.stProgress > div > div {
    background-color: #DBEAFE !important;
    border-radius: 20px !important;
}

.stProgress > div > div > div {
    background: linear-gradient(
        90deg,
        #2563EB,
        #0EA5E9
    ) !important;
    border-radius: 20px !important;
}

/* ===== CAPTIONS ===== */
.stCaption,
[data-testid="stCaptionContainer"] {
    color: #64748B !important;
    font-size: 13px !important;
}

/* ===== FOOTER ===== */
.footer {
    text-align: center;
    color: #64748B !important;
    font-size: 12px;
    padding-top: 28px;
}

/* ===== RESPONSIVE ADJUSTMENTS ===== */
@media (max-width: 768px) {
    .hero {
        padding: 26px 22px;
    }

    .hero h1 {
        font-size: 30px !important;
    }

    .section-title {
        font-size: 21px !important;
    }

    .feature-title {
        font-size: 18px !important;
    }
}
</style>
""", unsafe_allow_html=True)




# Load-data
@st.cache_resource
def load_model():
    return joblib.load("M:\Collage And Internship Project Files\AIML 3Month Project 2\Sentiment_Analysis\models\save_model\sentiment_pipeline.pkl")


try:
    model = load_model()
except Exception as e:
    st.error(
        "Could not load the trained model. "
        "Check that models/sentiment_pipeline.pkl exists."
    )
    st.stop()


# header
st.markdown("""
<div class="hero">
    <div class="eyebrow">✦ Artificial Intelligence · NLP</div>
    <h1>💬 SentimentAnalysis</h1>
    <p>
        Turn customer feedback into meaningful insights.
        Analyze reviews instantly with your machine learning model.
    </p>
</div>
""", unsafe_allow_html=True)

# Input-Section
left, right = st.columns([1.15, 0.85], gap="large")

with left:
    st.markdown(
        '<div class="section-title">✍️ Analyze a Review</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):
        st.write("**Enter your customer feedback**")

        review = st.text_area(
            "Customer review",
            placeholder=(
                "Example: The product is excellent, "
                "easy to use, and worth every penny!"
            ),
            height=170,
            label_visibility="collapsed"
        )

        st.caption("💡 Tip: Write a complete review for a more useful prediction.")

        analyze = st.button(
            "✨  Analyze Sentiment",
            type="primary",
            use_container_width=True
        )


with right:
    st.markdown(
        '<div class="section-title">🚀 What You Get</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):
        st.markdown("""
            <div class="feature-title">🎯 Instant Prediction</div>
            <div class="feature-description">
                Identify the sentiment expressed in a customer review.
            </div>

            <hr>

            <div class="feature-title">📊 Confidence Score</div>
            <div class="feature-description">
                See the model's estimated confidence in its prediction.
            </div>

            <hr>

            <div class="feature-title">🌈 Class Probabilities</div>
            <div class="feature-description">
                Compare the model's estimates for each sentiment class.
            </div>
        """, unsafe_allow_html=True)


# Prediction
if analyze:
    if not review.strip():
        st.warning("Please enter a review before analyzing.")
    else:
        try:
            prediction = model.predict([review.strip()])[0]
            probabilities = model.predict_proba([review.strip()])[0]
            classes = model.classes_

            confidence = max(probabilities) * 100

            sentiment_styles = {
                "Positive": ("😊", "#059669", "#d1fae5"),
                "Negative": ("😞", "#dc2626", "#fee2e2"),
                "Neutral": ("😐", "#d97706", "#fef3c7")
            }

            emoji, color, bg = sentiment_styles.get(
                str(prediction),
                ("💬", "#4f46e5", "#e0e7ff")
            )

            st.markdown(
                '<div class="section-title">📌 Analysis Results</div>',
                unsafe_allow_html=True
            )

            # Main result cards
            c1, c2 = st.columns(2, gap="large")

            with c1:
                st.markdown(f"""
                <div class="result-card">
                    <div class="result-label">Predicted Sentiment</div>
                    <div style="font-size:38px; margin-top:8px;">{emoji}</div>
                    <div style="color:{color}; font-size:28px;
                                font-weight:800; margin-top:4px;">
                        {prediction}
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with c2:
                st.markdown(f"""
                <div class="result-card">
                    <div class="result-label">Model Confidence</div>
                    <div class="result-value">{confidence:.2f}%</div>
                    <div style="color:#64748b; font-size:13px;
                                margin-top:10px;">
                        Highest predicted class probability
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # Probability breakdown
            st.markdown(
                '<div class="section-title">📊 Class Probability Breakdown</div>',
                unsafe_allow_html=True
            )

            with st.container(border=True):
                for label, probability in zip(classes, probabilities):
                    label = str(label)
                    percentage = float(probability) * 100

                    emoji_label, label_color, label_bg = sentiment_styles.get(
                        label,
                        ("💬", "#4f46e5", "#e0e7ff")
                    )

                    st.markdown(
                        f"<div style='display:flex; justify-content:space-between;"
                        f"align-items:center; margin-top:12px; margin-bottom:5px;'>"
                        f"<span style='font-weight:700;color:{label_color};'>"
                        f"{emoji_label} {label}</span>"
                        f"<span style='font-weight:700;color:#312e81;'>"
                        f"{percentage:.2f}%</span></div>",
                        unsafe_allow_html=True
                    )

                    st.progress(float(probability))

            st.caption(
                "Note: These probabilities are model estimates, not guarantees "
                "of correctness. Performance depends on the training data."
            )

        except Exception as e:
            st.error(f"Prediction failed: {e}")


# Footer
st.markdown("""
<div class="footer">
    ✨ SentimentAI · Powered by Machine Learning & Natural Language Processing
</div>
""", unsafe_allow_html=True)
