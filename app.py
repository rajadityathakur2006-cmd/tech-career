from flask import Flask, request, jsonify
import random
import datetime

app = Flask(__name__)

# ── Jokes ────────────────────────────────────────────────────────
JOKES = [
    "Why did Modi ji carry an umbrella? Because even the clouds wanted his autograph! ☁️😄",
    "Someone asked Modi ji: 'What is your favourite app?' He said: 'Mann Ki Baat — no Wi-Fi needed, it comes from the heart!' 📻😂",
    "Modi ji went to space. NASA asked: 'Do you need oxygen?' He said: 'No, I run on the energy of 140 crore Indians!' 🚀😄",
    "Teacher: 'What is the capital of India?' Student: 'New Delhi!' Teacher: 'Correct!' Modi ji from the back: 'And I keep it very clean thanks to Swachh Bharat!' 🧹😂",
    "Why does Modi ji never get lost? Because wherever he goes, India follows! 🇮🇳😄",
    "Modi ji's phone battery never dies. It runs on solar power — inspired by PM Suryaghar Yojana! ☀️📱",
    "What do you call Modi ji doing yoga at 5 AM? An early morning 'Viksit' exercise! 🧘‍♂️😂",
    "Modi ji asked Google Maps for directions. Google Maps said: 'You ARE the destination, sir!' 🗺️😄",
]

# ── Fun Facts ────────────────────────────────────────────────────
FUN_FACTS = [
    "🌟 Modi ji was born on September 17, 1950, in Vadnagar, a small town in Gujarat.",
    "📚 Modi ji sold tea (chai) at a railway station as a child. From chai seller to PM — what a journey!",
    "🧘 Modi ji wakes up at 5 AM every day and practises yoga religiously.",
    "✍️ He has written over 12 books on topics ranging from politics to climate change.",
    "🌍 Modi ji has visited over 60 countries as Prime Minister — the most well-travelled Indian PM!",
    "🏆 Time Magazine named Modi ji among the 100 most influential people in the world multiple times.",
    "📻 Mann Ki Baat is broadcast on 500+ radio channels and has been running since 2014.",
    "🚀 Under his leadership, India became only the 4th country to land on the moon and the FIRST on the south pole!",
]

# ── Motivational Quotes ──────────────────────────────────────────
QUOTES = [
    "\"Once we decide something, we ensure it gets done.\" — Narendra Modi",
    "\"India is not just a country, it is an emotion.\" — Narendra Modi",
    "\"Corruption and poverty are the two biggest enemies of our nation.\" — Narendra Modi",
    "\"The future belongs to those who believe in the beauty of their dreams.\" — Narendra Modi",
    "\"Sabka Saath, Sabka Vikas, Sabka Vishwas, Sabka Prayas.\" — Narendra Modi",
    "\"If we are united, no force in the world can stop India from becoming a superpower.\" — Narendra Modi",
    "\"Technology is the biggest equaliser. It can turn every challenge into an opportunity.\" — Narendra Modi",
    "\"A mother is a nation's greatest strength. Empower her, empower India.\" — Narendra Modi",
]

# ── Knowledge base ───────────────────────────────────────────────
RESPONSES = {
    "greetings": {
        "triggers": ["hello", "hey", "hi", "namaste", "namaskar", "good morning", "good evening", "good afternoon", "sup", "howdy"],
        "replies": [
            "Namaste! Mitron, it is wonderful to see your enthusiasm. Ask me anything!",
            "Jai Hind! Welcome to my press conference. What is on your mind today?",
            "Namaste! I, Narendra Modi, am here to answer your questions. Please proceed!",
            "Arre wah! You came to my press conference! Ask me anything, I am all ears! 🙏"
        ]
    },
    "how_are_you": {
        "triggers": ["how are you", "how are you doing", "kaisa hai", "how do you feel", "you ok"],
        "replies": [
            "I am absolutely fine, mitron! Serving 1.4 billion Indians keeps me very energetic!",
            "With the blessings of 140 crore Indians, I am always in high spirits!",
            "I am great! Working for Viksit Bharat 2047 gives me tremendous energy every day.",
            "Ekdum first class! When India grows, I grow with it! 💪"
        ]
    },
    "joke": {
        "triggers": ["joke", "funny", "laugh", "comedy", "make me laugh", "tell me a joke", "jokes"],
        "replies": ["__JOKE__"]
    },
    "fact": {
        "triggers": ["fact", "fun fact", "did you know", "tell me something", "interesting", "trivia"],
        "replies": ["__FACT__"]
    },
    "quote": {
        "triggers": ["quote", "motivation", "inspire", "motivate", "wisdom", "saying"],
        "replies": ["__QUOTE__"]
    },
    "time": {
        "triggers": ["time", "date", "today", "what day", "current time"],
        "replies": ["__TIME__"]
    },
    "development": {
        "triggers": ["development", "india progress", "growth", "economy", "gdp", "infrastructure", "roads", "highways"],
        "replies": [
            "Mitron, India is now the 5th largest economy in the world and we are aiming for the 3rd position!",
            "We have built more highways, airports, and railways in 10 years than in the previous 60! This is New India!",
            "Digital India, Make in India, Startup India — these are transformations happening on the ground every day!",
        ]
    },
    "digital": {
        "triggers": ["digital india", "technology", "tech", "upi", "internet", "startup", "app", "software"],
        "replies": [
            "India's UPI processes more digital transactions than the entire EU combined! This is the power of Digital India!",
            "We have given broadband to 6 lakh villages. From Gujarat to Kerala — everyone is connected!",
            "India has the world's 3rd largest startup ecosystem. Our young innovators are changing the world, mitron!",
        ]
    },
    "foreign": {
        "triggers": ["foreign policy", "china", "pakistan", "usa", "america", "relations", "neighbours", "war", "military"],
        "replies": [
            "India's foreign policy — neighbourhood first, act east, think global. We are friends with everyone but bow to no one!",
            "When I speak at the UN or G20, it is the voice of 1.4 billion Indians speaking!",
            "We stand for peace, but we will NEVER compromise on sovereignty. Not one inch of Indian land will ever be touched! 💪",
        ]
    },
    "education": {
        "triggers": ["education", "school", "college", "university", "student", "nep", "study", "learning"],
        "replies": [
            "NEP 2020 is the biggest education reform in 34 years! Modern, relevant, in the mother tongue of students.",
            "From IITs to new medical colleges — we have doubled higher education capacity. Your future is our priority!",
            "PM SHRI schools, free textbooks, mid-day meals — no child will be left behind due to poverty.",
        ]
    },
    "agriculture": {
        "triggers": ["farmer", "agriculture", "kisan", "crop", "msp", "farm", "wheat", "rice", "food"],
        "replies": [
            "Mitron, farmers are the backbone of India! PM Kisan Samman Nidhi has put money directly in 11 crore farmers' hands!",
            "We doubled MSP, built warehouses, cold chains — we are fighting for every kisan!",
            "Soil health cards, micro-irrigation — we are making farming both profitable and sustainable.",
        ]
    },
    "health": {
        "triggers": ["health", "hospital", "doctor", "medicine", "covid", "ayushman", "wellness", "sick"],
        "replies": [
            "Ayushman Bharat gives ₹5 lakh health insurance to 50 crore poor Indians. No one should die due to cost!",
            "We vaccinated 200 crore Indians in record time. India showed the world how to fight a pandemic!",
            "New AIIMS in every state, Jan Aushadhi stores with cheap medicines — health for all is our mission.",
        ]
    },
    "achievements": {
        "triggers": ["achievement", "what have you done", "accomplishment", "success", "best thing", "proud"],
        "replies": [
            "Swachh Bharat ended open defecation, electricity to every village, crores of homes under PM Awas — just the beginning!",
            "Chandrayaan-3 landed on the moon's south pole — India became the FIRST nation to do so! We are a space power! 🚀",
            "25 crore people lifted out of poverty in 9 years. Not just statistics — these are changed lives, mitron!",
        ]
    },
    "yoga": {
        "triggers": ["yoga", "fitness", "exercise", "health tip", "meditation", "wellness"],
        "replies": [
            "Yoga is India's gift to the world! I wake up at 5 AM every day to practice yoga. It gives me the energy to serve 1.4 billion people! 🧘‍♂️",
            "International Yoga Day on June 21 — India made the whole world bend and stretch! Even the UN agreed! 😄🧘",
            "Mitron, a healthy body leads to a healthy nation. Yoga, pranayama, meditation — these are our ancient secrets!",
        ]
    },
    "space": {
        "triggers": ["space", "moon", "isro", "chandrayaan", "rocket", "satellite", "mars", "mangalyaan"],
        "replies": [
            "Chandrayaan-3 made India the FIRST country to land on the moon's south pole! Our scientists are the best in the world! 🚀🌕",
            "Mangalyaan reached Mars in the first attempt — at a cost cheaper than making a Hollywood film! This is India's genius!",
            "ISRO is our pride. From a bicycle-carried satellite to landing on the moon — what a journey, mitron!",
        ]
    },
    "farewell": {
        "triggers": ["bye", "goodbye", "see you", "take care", "ok thanks", "thank you", "thanks", "tataa", "ciao"],
        "replies": [
            "Jai Hind! Remember — together we will build a Viksit Bharat by 2047. Namaste! 🙏🇮🇳",
            "Thank you for attending my press conference! Jai Hind, Jai Bharat! 🎙️",
            "Namaste! Come back anytime. The doors of this press conference are always open! 🇮🇳",
        ]
    },
    "identity": {
        "triggers": ["who are you", "your name", "introduce yourself", "aap kaun hain", "tell me about yourself"],
        "replies": [
            "I am Narendra Damodardas Modi — Prime Minister of India, former CM of Gujarat, and a sevak of 140 crore Indians!",
            "Born in Vadnagar, Gujarat. From selling chai to leading the world's largest democracy — this is every common Indian's story!created by aditya 🍵",
        ]
    },
}

def get_bot_response(user_input):
    text = user_input.lower().strip()

    for category, data in RESPONSES.items():
        for trigger in data["triggers"]:
            if trigger in text:
                reply = random.choice(data["replies"])
                if reply == "__JOKE__":
                    return "😄 " + random.choice(JOKES)
                if reply == "__FACT__":
                    return "🌟 Fun Fact: " + random.choice(FUN_FACTS)
                if reply == "__QUOTE__":
                    return "💬 " + random.choice(QUOTES)
                if reply == "__TIME__":
                    now = datetime.datetime.now()
                    return f"🕐 Mitron, the current date and time is: {now.strftime('%A, %d %B %Y — %I:%M %p')}. Time waits for no one — let us keep working!"
                return reply

    fallbacks = [
        "Mitron, that is a very deep question! In New India, every challenge is an opportunity. Could you elaborate? 🤔",
        "As I always say — 'Sabka Saath, Sabka Vikas'. Whatever the issue, our intention is clear and direction is right!",
        "I have noted your question. Try asking me about: jokes 😄, fun facts 🌟, quotes 💬, Digital India, Economy, or Health!",
        "Interesting question! You can also ask me to tell a joke 😂, share a quote 💬, or reveal a fun fact 🌟 about me!",
    ]
    return random.choice(fallbacks)

# ── Routes ────────────────────────────────────────────────────────

@app.route("/")
def home():
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Narendra Modi Press Conference</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Playfair+Display:wght@700;900&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg:        #050508;
  --surface:   #0d0d14;
  --surface2:  #111118;
  --surface3:  #16161f;
  --saffron:   #ff6b00;
  --saffron2:  #ff8c38;
  --green:     #00c853;
  --blue:      #2979ff;
  --gold:      #ffd54f;
  --text:      #e8e8f0;
  --muted:     #6b6b88;
  --border:    rgba(255,107,0,0.15);
  --glow:      rgba(255,107,0,0.08);
}

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'Space Grotesk', sans-serif;
  min-height: 100vh;
  overflow-x: hidden;
}

/* Ambient background blobs */
body::before {
  content: '';
  position: fixed;
  top: -200px; left: -200px;
  width: 600px; height: 600px;
  background: radial-gradient(circle, rgba(255,107,0,0.06) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}
body::after {
  content: '';
  position: fixed;
  bottom: -200px; right: -200px;
  width: 500px; height: 500px;
  background: radial-gradient(circle, rgba(0,200,83,0.04) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

/* Tricolour bar */
.tribar {
  height: 4px;
  background: linear-gradient(to right, #ff6b00 33.3%, #fff 33.3% 66.6%, #138808 66.6%);
  position: relative; z-index: 10;
}

/* Header */
header {
  background: rgba(13,13,20,0.95);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  padding: 14px 24px;
  display: flex;
  align-items: center;
  gap: 14px;
  position: sticky; top: 0; z-index: 100;
}
.hlogo {
  width: 40px; height: 40px;
  border-radius: 10px;
  background: linear-gradient(135deg, #ff6b00, #e85d00);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.2rem;
  box-shadow: 0 0 16px rgba(255,107,0,0.35);
  flex-shrink: 0;
}
.htitle h1 {
  font-family: 'Playfair Display', serif;
  font-size: 1.05rem;
  color: var(--saffron);
  line-height: 1.2;
}
.htitle p {
  font-size: 0.65rem;
  color: var(--muted);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-top: 2px;
}
.hright {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 10px;
}
.live-dot {
  display: flex; align-items: center; gap: 5px;
  background: rgba(200,0,0,0.18);
  border: 1px solid rgba(200,0,0,0.4);
  color: #ff4444;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  padding: 4px 10px;
  border-radius: 20px;
}
.live-dot::before {
  content: '';
  width: 6px; height: 6px;
  background: #ff4444;
  border-radius: 50%;
  animation: livepulse 1.4s infinite;
}
@keyframes livepulse { 0%,100%{opacity:1} 50%{opacity:0.3} }

/* Main */
.main { max-width: 820px; margin: 0 auto; padding: 24px 16px 120px; position: relative; z-index: 1; }

/* Welcome card */
.welcome {
  background: linear-gradient(135deg, rgba(255,107,0,0.08), rgba(19,136,8,0.06));
  border: 1px solid rgba(255,107,0,0.22);
  border-radius: 16px;
  padding: 20px 22px;
  margin-bottom: 22px;
  display: flex; gap: 16px; align-items: flex-start;
}
.w-avatar {
  width: 52px; height: 52px; border-radius: 14px; flex-shrink: 0;
  background: linear-gradient(135deg, var(--saffron), #c04800);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.5rem;
  box-shadow: 0 0 24px rgba(255,107,0,0.3);
}
.w-text h2 {
  font-family: 'Playfair Display', serif;
  font-size: 1rem; color: var(--saffron); margin-bottom: 6px;
}
.w-text p { font-size: 0.84rem; line-height: 1.65; color: #c0c0d4; }

/* Feature cards row */
.feature-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 10px;
  margin-bottom: 22px;
}
.feat-card {
  background: var(--surface2);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 14px 12px;
  cursor: pointer;
  transition: all 0.2s;
  text-align: center;
}
.feat-card:hover {
  background: rgba(255,107,0,0.1);
  border-color: rgba(255,107,0,0.45);
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(255,107,0,0.15);
}
.feat-card .fc-icon { font-size: 1.6rem; display: block; margin-bottom: 6px; }
.feat-card .fc-label { font-size: 0.72rem; font-weight: 600; color: #c0c0d4; letter-spacing: 0.05em; }

/* Topic chips */
.section-label {
  font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.12em;
  color: var(--muted); margin-bottom: 10px;
}
.chips { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 22px; }
.chip {
  background: var(--surface3);
  border: 1px solid rgba(255,255,255,0.07);
  color: #b0b0c8;
  font-size: 0.75rem; font-family: 'Space Grotesk', sans-serif;
  padding: 6px 13px; border-radius: 20px;
  cursor: pointer; transition: all 0.18s;
}
.chip:hover {
  background: rgba(255,107,0,0.12);
  border-color: rgba(255,107,0,0.5);
  color: var(--saffron2);
  transform: translateY(-1px);
}

/* Chatbox */
#chatbox {
  background: var(--surface);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 18px;
  padding: 18px;
  min-height: 340px;
  max-height: 460px;
  overflow-y: auto;
  display: flex; flex-direction: column; gap: 12px;
  margin-bottom: 14px;
  scroll-behavior: smooth;
}
#chatbox::-webkit-scrollbar { width: 3px; }
#chatbox::-webkit-scrollbar-thumb { background: rgba(255,107,0,0.25); border-radius: 3px; }

.msg {
  max-width: 78%;
  padding: 11px 14px;
  border-radius: 14px;
  font-size: 0.85rem;
  line-height: 1.6;
  animation: fadeUp 0.22s ease;
}
@keyframes fadeUp { from{opacity:0;transform:translateY(8px)} to{opacity:1;transform:translateY(0)} }

.msg.user {
  background: linear-gradient(135deg, #0e2240, #0a1a30);
  border: 1px solid rgba(41,121,255,0.25);
  align-self: flex-end;
  border-bottom-right-radius: 4px;
}
.msg.bot {
  background: linear-gradient(135deg, #1a0d00, #120800);
  border: 1px solid rgba(255,107,0,0.2);
  align-self: flex-start;
  border-bottom-left-radius: 4px;
}
.msg-meta {
  font-size: 0.62rem; font-weight: 700; letter-spacing: 0.1em;
  text-transform: uppercase; margin-bottom: 4px; display: flex;
  align-items: center; gap: 5px;
}
.msg.user .msg-meta { color: #5c9aff; justify-content: flex-end; }
.msg.bot  .msg-meta { color: var(--saffron); }

/* Typing */
.typing {
  align-self: flex-start;
  background: linear-gradient(135deg, #1a0d00, #120800);
  border: 1px solid rgba(255,107,0,0.2);
  border-radius: 14px; border-bottom-left-radius: 4px;
  padding: 12px 18px;
  display: flex; gap: 5px; align-items: center;
}
.typing span {
  width: 6px; height: 6px;
  background: var(--saffron);
  border-radius: 50%;
  animation: tdot 1.1s infinite;
}
.typing span:nth-child(2){animation-delay:.2s}
.typing span:nth-child(3){animation-delay:.4s}
@keyframes tdot{0%,80%,100%{transform:translateY(0)}40%{transform:translateY(-7px)}}

/* Input bar */
.input-bar {
  display: flex; gap: 10px;
  background: var(--surface2);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;
  padding: 6px 6px 6px 16px;
  align-items: center;
  transition: border-color 0.2s;
}
.input-bar:focus-within { border-color: rgba(255,107,0,0.5); }
#userInput {
  flex: 1;
  background: transparent; border: none; outline: none;
  color: var(--text);
  font-family: 'Space Grotesk', sans-serif;
  font-size: 0.88rem;
}
#userInput::placeholder { color: var(--muted); }
#sendBtn {
  background: linear-gradient(135deg, var(--saffron), #c04800);
  border: none; border-radius: 10px;
  color: white; font-family: 'Space Grotesk', sans-serif;
  font-size: 0.82rem; font-weight: 700;
  padding: 10px 18px; cursor: pointer;
  transition: transform 0.15s, box-shadow 0.15s;
  display: flex; align-items: center; gap: 6px;
  white-space: nowrap;
}
#sendBtn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 18px rgba(255,107,0,0.4);
}

/* Footer */
footer {
  text-align: center;
  margin-top: 20px;
  font-size: 0.7rem;
  color: var(--muted);
  line-height: 1.8;
}
footer .brand { color: var(--saffron); font-weight: 600; }
footer .designer { color: #7c7cff; font-weight: 600; }
footer .heart { color: #ff4466; }

/* Particle canvas */
#particles { position: fixed; inset: 0; pointer-events: none; z-index: 0; opacity: 0.4; }

@media(max-width:580px){
  .feature-row{grid-template-columns:repeat(3,1fr)}
  .htitle h1{font-size:0.88rem}
  .welcome{flex-direction:column}
  .msg{max-width:90%}
}
</style>
</head>
<body>

<canvas id="particles"></canvas>
<div class="tribar"></div>

<header>
  <div class="hlogo">🎙️</div>
  <div class="htitle">
    <h1>Narendra Modi Press Conference</h1>
    <p>Official Interactive Q&amp;A · Powered by desh ki jnta</p>
  </div>
  <div class="hright">
    <div class="live-dot">LIVE</div>
  </div>
</header>

<div class="main">

  <div class="welcome">
    <div class="w-avatar">🇮🇳</div>
    <div class="w-text">
      <h2>Namaste, Mitron! 🙏</h2>
      <p>Hey, I'm <strong style="color:var(--saffron)">Narendra Modi</strong> and I will answer any questions you have for me.
      Whether it's about India's development, foreign policy, space, education, or anything else — I am here.
      You can also ask me for a <strong>joke 😄</strong>, <strong>fun fact 🌟</strong>, <strong>quote 💬</strong>, or the current <strong>time 🕐</strong>.
      Still, you can ask me <em>whatever you want!</em> Jai Hind! 🇮🇳</p>
    </div>
  </div>

  <!-- Feature shortcut cards -->
  <div class="section-label">Quick Actions</div>
  <div class="feature-row">
    <div class="feat-card" onclick="sendChip('Tell me a joke')">
      <span class="fc-icon">😄</span>
      <span class="fc-label">Joke</span>
    </div>
    <div class="feat-card" onclick="sendChip('Tell me a fun fact')">
      <span class="fc-icon">🌟</span>
      <span class="fc-label">Fun Fact</span>
    </div>
    <div class="feat-card" onclick="sendChip('Give me a quote')">
      <span class="fc-icon">💬</span>
      <span class="fc-label">Quote</span>
    </div>
    <div class="feat-card" onclick="sendChip('What is the time and date today')">
      <span class="fc-icon">🕐</span>
      <span class="fc-label">Date &amp; Time</span>
    </div>
    <div class="feat-card" onclick="sendChip('Tell me about space and ISRO')">
      <span class="fc-icon">🚀</span>
      <span class="fc-label">Space</span>
    </div>
    <div class="feat-card" onclick="sendChip('Tell me about yoga')">
      <span class="fc-icon">🧘</span>
      <span class="fc-label">Yoga</span>
    </div>
  </div>

  <div class="section-label">Topic Shortcuts</div>
  <div class="chips">
    <div class="chip" onclick="sendChip('Tell me about Digital India')">💻 Digital India</div>
    <div class="chip" onclick="sendChip('India economy and development')">📈 Economy</div>
    <div class="chip" onclick="sendChip('Tell me about farmers and agriculture')">🌾 Agriculture</div>
    <div class="chip" onclick="sendChip('India foreign policy')">🌍 Foreign Policy</div>
    <div class="chip" onclick="sendChip('Tell me about education in India')">🎓 Education</div>
    <div class="chip" onclick="sendChip('What about health and hospitals')">🏥 Health</div>
    <div class="chip" onclick="sendChip('What are your achievements')">🏆 Achievements</div>
    <div class="chip" onclick="sendChip('Who are you')">🙋 Who Are You?</div>
  </div>

  <div id="chatbox"></div>

  <div class="input-bar">
    <input id="userInput" type="text" placeholder="Ask Modi ji anything..." autocomplete="off" />
    <button id="sendBtn" onclick="sendMessage()">Send ✈️</button>
  </div>

  <footer>
    <div>🎙️ <span class="brand">Modi Ji AI</span> · Inspired by Viksit Bharat 2047 🇮🇳</div>
    <div>Designed with <span class="heart">♥</span> by <span class="designer">Aditya</span></div>
  </footer>

</div>

<script>
// ── Particle canvas ──────────────────────────────────────────────
(function(){
  const canvas = document.getElementById('particles');
  const ctx = canvas.getContext('2d');
  let W, H, dots = [];
  function resize(){ W = canvas.width = innerWidth; H = canvas.height = innerHeight; }
  resize(); window.addEventListener('resize', resize);
  const colours = ['rgba(255,107,0,', 'rgba(255,200,80,', 'rgba(0,200,83,', 'rgba(255,255,255,'];
  for(let i=0;i<55;i++){
    dots.push({
      x: Math.random()*2000, y: Math.random()*1000,
      r: Math.random()*1.5+0.4,
      vx:(Math.random()-.5)*0.25, vy:(Math.random()-.5)*0.15,
      c: colours[Math.floor(Math.random()*colours.length)]
    });
  }
  function draw(){
    ctx.clearRect(0,0,W,H);
    dots.forEach(d=>{
      d.x+=d.vx; d.y+=d.vy;
      if(d.x<0)d.x=W; if(d.x>W)d.x=0;
      if(d.y<0)d.y=H; if(d.y>H)d.y=0;
      ctx.beginPath();
      ctx.arc(d.x,d.y,d.r,0,Math.PI*2);
      ctx.fillStyle=d.c+'0.7)';
      ctx.fill();
    });
    requestAnimationFrame(draw);
  }
  draw();
})();

// ── Chat logic ───────────────────────────────────────────────────
const chatbox = document.getElementById('chatbox');
const input   = document.getElementById('userInput');

function getTime(){ return new Date().toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'}); }

function appendMsg(text, role){
  const wrap = document.createElement('div');
  wrap.className = 'msg ' + role;
  const meta = document.createElement('div');
  meta.className = 'msg-meta';
  meta.innerHTML = role==='user'
    ? `<span>🙋 You</span><span style="opacity:.45;font-weight:400">${getTime()}</span>`
    : `<span>🎙️ Modi Ji</span><span style="opacity:.45;font-weight:400">${getTime()}</span>`;
  const body = document.createElement('div');
  body.textContent = text;
  wrap.appendChild(meta); wrap.appendChild(body);
  chatbox.appendChild(wrap);
  chatbox.scrollTop = chatbox.scrollHeight;
}

function showTyping(){
  const t = document.createElement('div');
  t.className = 'typing'; t.id = 'typing';
  t.innerHTML = '<span></span><span></span><span></span>';
  chatbox.appendChild(t);
  chatbox.scrollTop = chatbox.scrollHeight;
}
function removeTyping(){ const t=document.getElementById('typing'); if(t)t.remove(); }

async function sendMessage(){
  const msg = input.value.trim();
  if(!msg) return;
  input.value = '';
  appendMsg(msg, 'user');
  showTyping();
  try {
    const res = await fetch('/chat',{
      method:'POST',
      headers:{'Content-Type':'application/json','Accept':'application/json'},
      body: JSON.stringify({message:msg})
    });
    if(!res.ok) throw new Error('status '+res.status);
    const data = await res.json();
    removeTyping();
    appendMsg(data.reply, 'bot');
  } catch(e){
    removeTyping();
    try {
      const r2 = await fetch('/chat?message='+encodeURIComponent(msg));
      const d2 = await r2.json();
      appendMsg(d2.reply,'bot');
    } catch(e2){
      appendMsg('Connection issue. Please restart Flask and refresh the page.','bot');
    }
  }
}

function sendChip(text){ input.value=text; sendMessage(); }
input.addEventListener('keydown', e=>{ if(e.key==='Enter') sendMessage(); });
</script>
</body>
</html>"""

@app.route("/chat", methods=["POST","GET"])
def chat():
    try:
        data = request.get_json(force=True, silent=True)
        if data and "message" in data:
            user_message = data["message"]
        else:
            user_message = request.form.get("message") or request.args.get("message","")
    except Exception:
        user_message = request.args.get("message","")
    if not user_message:
        return jsonify({"reply":"Please ask me a question, mitron! 🙏"})
    reply = get_bot_response(user_message)
    resp  = jsonify({"reply": reply})
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

if __name__ == "__main__":
    app.run(debug=True, port=5001)

