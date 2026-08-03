import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from predictor import predict_lead

if "prediction" not in st.session_state:
    st.session_state.prediction = None

if "occupation" not in st.session_state:
    st.session_state.occupation = ""    

if "website_visits" not in st.session_state:
    st.session_state.website_visits = 0

if "print_media_type2" not in st.session_state:
    st.session_state.print_media_type2 = 0    

if "print_media_type1" not in st.session_state:
    st.session_state.print_media_type1 = 0

if "digital_media" not in st.session_state:
    st.session_state.digital_media = 0

if "referral" not in st.session_state:
    st.session_state.referral = 0

if "educational" not in st.session_state:
    st.session_state.educational = 0  

if "time_spent" not in st.session_state:
    st.session_state.time_spent = 0

if "page_views" not in st.session_state:
    st.session_state.page_views = 0    

if "priority_message" not in st.session_state:
    st.session_state.priority_message = "Not Generated"    

if "probability" not in st.session_state:
    st.session_state.probability = 0

if "confidence" not in st.session_state:
    st.session_state.confidence = 0

if "label" not in st.session_state:
    st.session_state.label = ""

if "lead_quality" not in st.session_state:
    st.session_state.lead_quality = "Not Generated"

if "priority" not in st.session_state:
    st.session_state.priority = "Not Generated"

if "action" not in st.session_state:
    st.session_state.action = "Not Generated"

if "last_activity" not in st.session_state:
    st.session_state.last_activity = ""    

if "first_interaction" not in st.session_state:
    st.session_state.first_interaction = ""    

st.set_page_config(
    page_title="Lead Conversion Intelligence System",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

:root{

--primary:#2563EB;
--secondary:#7C3AED;
--accent:#38BDF8;

--success:#22C55E;
--warning:#F59E0B;
--danger:#EF4444;

--background:#020617;
--surface:#0F172A;
--surface-2:#111827;

--text:#FFFFFF;
--text-secondary:#FFFFFF;
--text-muted:#E2E8F0;

--border:rgba(255,255,255,.08);

--shadow-sm:0 8px 20px rgba(0,0,0,.25);
--shadow-md:0 18px 45px rgba(0,0,0,.35);
--shadow-lg:0 30px 70px rgba(0,0,0,.45);

}

html,
body,
[class*="css"]{

font-family:'Inter',sans-serif;

background:var(--background);

color:var(--text);

}

.stApp{

background:

radial-gradient(circle at top right,#1D4ED8 0%,transparent 30%),

radial-gradient(circle at bottom left,#6D28D9 0%,transparent 25%),

linear-gradient(
135deg,
#020617,
#071226,
#0F172A
);

}

#MainMenu{

visibility:hidden;

}

header{

visibility:hidden;

}

footer{

visibility:hidden;

}

.block-container{

max-width:1500px;

padding-top:1.2rem;

padding-left:2rem;

padding-right:2rem;

padding-bottom:2rem;

}

section[data-testid="stSidebar"]{

background:#08111F;

border-right:1px solid rgba(255,255,255,.05);

}

section[data-testid="stSidebar"] *{

color:white;

}

h1{

font-size:48px;

font-weight:800;

letter-spacing:-1px;

margin-bottom:12px;

}

h2{

font-size:36px;

font-weight:700;

}

h3{

font-size:30px;

font-weight:700;

}

p{

color:#F1F5F9;

font-size:16px;

line-height:1.9;

}

.glass-card{

color:#FFFFFF;

background:rgba(17,24,39,.85);

backdrop-filter:blur(18px);

-webkit-backdrop-filter:blur(18px);

border:1px solid rgba(255,255,255,.08);

border-radius:24px;

padding:28px;

box-shadow:var(--shadow-md);

transition:.35s;

}

.glass-card:hover{

transform:translateY(-5px);

border-color:#38BDF8;

box-shadow:0 25px 55px rgba(56,189,248,.18);

}

.metric-card{

background:linear-gradient(
145deg,
#111827,
#1E293B
);

border:1px solid rgba(255,255,255,.06);

border-radius:22px;

padding:24px;

text-align:center;

transition:.35s;

box-shadow:var(--shadow-sm);

}

.metric-card:hover{

transform:translateY(-6px);

border-color:#38BDF8;

}

.metric-title{

font-size:16px;

font-weight:600;

color:#E2E8F0;

margin-bottom:12px;

}

.metric-value{

font-size:32px;

font-weight:800;

color:white;

}

.metric-line{

width:60px;

height:4px;

margin:auto;

margin-top:16px;

border-radius:20px;

background:

linear-gradient(
90deg,
#2563EB,
#7C3AED
);

}

.section-title{

font-size:38px;

font-weight:800;

color:white;

margin-bottom:8px;

}

.section-subtitle{

font-size:17px;

color:#CBD5E1;

margin-bottom:28px;

}

div[data-testid="stButton"]>button{

width:100%;

height:58px;

border:none;

border-radius:18px;

font-size:18px;

font-weight:700;

color:white;

background:

linear-gradient(
90deg,
#2563EB,
#7C3AED
);

box-shadow:

0 12px 30px rgba(37,99,235,.35);

transition:.3s;

}

div[data-testid="stButton"]>button:hover{

transform:translateY(-3px);

box-shadow:

0 20px 45px rgba(124,58,237,.45);

}

div[data-testid="stNumberInput"] input,
div[data-testid="stSelectbox"]>div,
div[data-testid="stTextInput"] input{

border-radius:12px;

}

.stAlert{

border-radius:18px;

}

hr{

border:none;

height:1px;

background:rgba(255,255,255,.08);

margin-top:28px;

margin-bottom:28px;

}

::-webkit-scrollbar{

width:8px;

}

::-webkit-scrollbar-thumb{

background:#334155;

border-radius:30px;

}

::-webkit-scrollbar-thumb:hover{

background:#475569;

}

.fade-in{

animation:fadeIn .7s ease;

}

@keyframes fadeIn{

0%{

opacity:0;

transform:translateY(20px);

}

100%{

opacity:1;

transform:translateY(0);

}

}

</style>
""",unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Prediction", "Analytics", "About"],
    icons=["cpu-fill", "bar-chart-fill", "info-circle-fill"],
    orientation="horizontal",
    default_index=0,
    styles={
        "container":{
            "padding":"8px",
            "background-color":"rgba(17,24,39,.70)",
            "border-radius":"18px",
            "border":"1px solid rgba(255,255,255,.08)"
        },
        "icon":{
            "color":"#38BDF8",
            "font-size":"20px"
        },
        "nav-link":{
            "font-size":"17px",
            "font-weight":"600",
            "color":"#CBD5E1",
            "text-align":"center",
            "--hover-color":"rgba(37,99,235,.18)"
        },
        "nav-link-selected":{
            "background":"linear-gradient(90deg,#2563EB,#7C3AED)",
            "color":"white"
        }
    }
)

st.markdown("""

<div style="
background:linear-gradient(135deg,#2563EB,#4F46E5,#7C3AED);
padding:45px;
border-radius:26px;
margin-top:20px;
margin-bottom:30px;
box-shadow:0 20px 50px rgba(0,0,0,.35);
">

<h1 style="
margin:0;
color:white;
font-size:52px;
font-weight:800;
">

🚀 Lead Conversion Intelligence System

</h1>

<p style="
font-size:20px;
margin-top:18px;
color:#E2E8F0;
line-height:1.8;
max-width:760px;
">

AI Powered Lead Scoring Platform using an Ensemble Machine Learning Model.
Analyze customer behaviour, identify high-value leads, improve conversion
rate and support smarter business decisions through Artificial Intelligence.

</p>

</div>

""", unsafe_allow_html=True)

st.markdown(
"""
<div class="section-title">

Business Overview

</div>

<div class="section-subtitle">

Real-time Lead Conversion Intelligence Dashboard

</div>
""",
unsafe_allow_html=True
)

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">
            Dataset
        </div>
        <div class="metric-value">
            4,612
        </div>
        <div class="metric-line"></div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">
            Features
        </div>
        <div class="metric-value">
            15
        </div>
        <div class="metric-line"></div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">
            Model
        </div>
        <div class="metric-value">
            STACK
        </div>
        <div class="metric-line"></div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">
            Status
        </div>
        <div class="metric-value">
            Ready
        </div>
        <div class="metric-line"></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if selected == "Prediction":

    st.markdown("""
    <div class="section-title">
        AI Lead Prediction Workspace
    </div>

    <div class="section-subtitle">
        Enter lead details to generate an AI-powered conversion prediction.
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([2, 1], gap="large")

    with left:

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)

        c1, c2 = st.columns(2)

        with c1:

            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=28
            )

            website_visits = st.number_input(
                "Website Visits",
                min_value=0,
                value=5
            )

            time_spent_on_website = st.number_input(
                "Time Spent On Website (Seconds)",
                min_value=0,
                value=450
            )

            page_views_per_visit = st.number_input(
                "Page Views Per Visit",
                min_value=0.0,
                value=4.0,
                step=0.1
            )

        with c2:

            occupation = st.selectbox(
                "Current Occupation",
                [
                    "Student",
                    "Unemployed",
                    "Working Professional"
                ]
            )

            first_interaction = st.selectbox(
                "First Interaction",
                [
                    "Website",
                    "Mobile App",
                    "Advertisement"
                ]
            )

            profile_completed = st.selectbox(
                "Profile Completed",
                [
                    "Low",
                    "Medium",
                    "High"
                ]
            )

            last_activity = st.selectbox(
                "Last Activity",
                [
                    "Website Activity",
                    "Phone Activity",
                    "Email Activity"
                ]
            )

        st.markdown("### Marketing Channels")

        m1, m2, m3 = st.columns(3)

        with m1:

            print_media_type1 = st.checkbox("Print Media Type 1")

            digital_media = st.checkbox("Digital Media")

        with m2:

            print_media_type2 = st.checkbox("Print Media Type 2")

            educational_channels = st.checkbox("Educational Channels")

        with m3:

            referral = st.checkbox("Referral")

        predict_button = st.button(
            "🚀 Generate AI Prediction",
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with right:

        st.markdown("""
        <div class="glass-card">

        <h3 style="margin-top:0;">
        📊 Prediction Summary
        </h3>

        <hr>

        <p>
        Fill all lead information and click
        <b>Generate AI Prediction</b>.
        </p>

        <p>
        The AI model evaluates customer behaviour,
        marketing channels and engagement level
        to estimate conversion probability.
        </p>

        <hr>

        <b>Model</b><br>
        Stacking Ensemble

        <br><br>

        <b>Business Domain</b><br>
        EdTech Lead Conversion

        <br><br>

        <b>Status</b><br>
        Ready for Prediction

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    summary1, summary2, summary3 = st.columns(3)

    with summary1:
        st.metric(
            label="Current Occupation",
            value=occupation
        )

    with summary2:
        st.metric(
            label="Website Visits",
            value=int(website_visits)
        )

    with summary3:
        st.metric(
            label="Profile Status",
            value=profile_completed
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.info(
        "Complete the lead information and click 'Generate AI Prediction' to evaluate the lead using the AI model."
    )

    st.markdown("---")

    st.subheader("Selected Lead Information")

    preview = {
        "Age": age,
        "Website Visits": website_visits,
        "Time Spent": time_spent_on_website,
        "Page Views / Visit": page_views_per_visit,
        "Occupation": occupation,
        "First Interaction": first_interaction,
        "Profile": profile_completed,
        "Last Activity": last_activity,
        "Print Media Type 1": print_media_type1,
        "Print Media Type 2": print_media_type2,
        "Digital Media": digital_media,
        "Educational Channels": educational_channels,
        "Referral": referral
        
    }

    st.json(preview)

    if predict_button:

        user_input = {

            "age": age,

            "website_visits": website_visits,

            "time_spent_on_website": time_spent_on_website,

            "page_views_per_visit": page_views_per_visit,


            "current_occupation_Student":
                1 if occupation == "Student" else 0,

            "current_occupation_Unemployed":
                1 if occupation == "Unemployed" else 0,


            "first_interaction_Website":
                1 if first_interaction == "Website" else 0,


            "profile_completed_Low":
                1 if profile_completed == "Low" else 0,

            "profile_completed_Medium":
                1 if profile_completed == "Medium" else 0,


            "last_activity_Phone Activity":
                1 if last_activity == "Phone Activity" else 0,

            "last_activity_Website Activity":
                1 if last_activity == "Website Activity" else 0,


            "print_media_type1_Yes":
                1 if print_media_type1 else 0,

            "print_media_type2_Yes":
                1 if print_media_type2 else 0,


            "digital_media_Yes":
                1 if digital_media else 0,


            "educational_channels_Yes":
                1 if educational_channels else 0,


            "referral_Yes":
                1 if referral else 0
        }


        with st.spinner(
            "Running AI Ensemble Prediction..."
        ):

            result = predict_lead(user_input)
            st.write(result)


        prediction = result["prediction"]

        probability = result["Conversion Probability"]

        confidence = result["Model Confidence"]

        label = result["label"]

        st.session_state.prediction = prediction
        st.session_state.probability = probability
        st.session_state.confidence = confidence
        st.session_state.first_interaction = first_interaction
        st.session_state.label = label
        st.session_state.website_visits = website_visits
        st.session_state.time_spent = time_spent_on_website
        st.session_state.page_views = page_views_per_visit
        st.session_state.print_media_type1 = print_media_type1
        st.session_state.print_media_type2 = print_media_type2
        st.session_state.digital_media = digital_media
        st.session_state.referral = referral
        st.session_state.educational = educational_channels
        st.session_state.last_activity = last_activity
        st.session_state.occupation = occupation

        if probability >= 80:

            lead_quality = "🔥 HOT LEAD"

            quality_text = (
                "High conversion probability. "
                "Immediate sales follow-up recommended."
            )


        elif probability >= 50:

            lead_quality = "⭐ WARM LEAD"

            quality_text = (
                "Good conversion potential. "
                "Follow-up within 24 hours is recommended."
            )


        else:

            lead_quality = "❄️ COLD LEAD"

            quality_text = (
                "Low conversion probability. "
                "Use nurturing campaigns."
            )

        st.session_state.lead_quality = lead_quality


        st.markdown("<br>", unsafe_allow_html=True)


        st.markdown(
        """
        <div class="section-title">
            AI Prediction Result
        </div>
        """,
        unsafe_allow_html=True
        )


        r1, r2, r3 = st.columns(3)


        with r1:

            st.markdown(
            f"""
            <div class="metric-card">

            <div class="metric-title">
            Prediction
            </div>

            <div class="metric-value">
            {st.session_state.get("label","")}
            </div>

            <div class="metric-line"></div>

            </div>
            """,
            unsafe_allow_html=True
            )


        with r2:

            st.markdown(
            f"""
            <div class="metric-card">

            <div class="metric-title">
            Conversion Probability
            </div>

            <div class="metric-value">
            {probability:.2f}%
            </div>

            <div class="metric-line"></div>

            </div>
            """,
            unsafe_allow_html=True
            )


        with r3:

            st.markdown(
            f"""
            <div class="metric-card">

            <div class="metric-title">
            Model Confidence
            </div>

            <div class="metric-value">
            {confidence}
            </div>

            <div class="metric-line"></div>

            </div>
            """,
            unsafe_allow_html=True
            )


        st.markdown("<br>", unsafe_allow_html=True)


        st.markdown(
        f"""
        <div class="glass-card">

        <h3>
        Lead Quality
        </h3>

        <h2>
        {st.session_state.get("lead_quality","")}
        </h2>

        <p>
        {quality_text}
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)


        st.markdown(
        """
        <div class="section-title">
            Conversion Intelligence
        </div>

        <div class="section-subtitle">
            AI generated conversion probability analysis
        </div>
        """,
        unsafe_allow_html=True
        )


        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=float(probability),
                number={
                    "suffix": "%",
                    "font":{
                        "size":40
                    }
                },
                title={
                    "text":"Conversion Probability",
                    "font":{
                        "size":22
                    }
                },
                gauge={
                    "axis":{
                        "range":[0,100],
                        "tickwidth":1
                    },
                    "bar":{
                        "color":"#38BDF8"
                    },
                    "bgcolor":"rgba(0,0,0,0)",
                    "borderwidth":0,
                    "steps":[
                        {
                            "range":[0,30],
                            "color":"#7F1D1D"
                        },
                        {
                            "range":[30,70],
                            "color":"#854D0E"
                        },
                        {
                            "range":[70,100],
                            "color":"#166534"
                        }
                    ]
                }
            )
        )


        gauge.update_layout(
            height=350,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={
                "color":"white"
            },
            margin={
                "l":20,
                "r":20,
                "t":60,
                "b":20
            }
        )


        st.plotly_chart(
            gauge,
            use_container_width=True
        )


        st.markdown("<br>", unsafe_allow_html=True)


        if label == "Converted":

            recommendation = """
            This lead has strong conversion potential.

            Recommended Actions:

            • Immediate sales follow-up

            • Schedule product/demo call

            • Assign priority sales executive

            • Start personalized communication
            """

        else:

            recommendation = """
            This lead currently has lower conversion probability.

            Recommended Actions:

            • Add into nurturing campaign

            • Send educational content

            • Improve engagement through follow-ups

            • Retarget using digital channels
            """


        st.markdown(
        f"""
        <div class="glass-card">

        <h3>
        🤖 AI Recommendation
        </h3>

        <p style="font-size:18px;">

        {recommendation}

        </p>

        </div>
        """,
        unsafe_allow_html=True
        )

        probability = st.session_state.probability

        confidence = st.session_state.confidence

        label = st.session_state.label

        st.markdown("<br>", unsafe_allow_html=True)


st.markdown(
"""
<div class="section-title">
    📊 Analytics Dashboard
</div>

<div class="section-subtitle">
    Business intelligence insights generated from lead prediction analysis.
</div>
""",
unsafe_allow_html=True
)


a1, a2, a3, a4 = st.columns(4)


with a1:

    st.markdown(
    """
    <div class="metric-card">

    <div class="metric-title">
    Conversion Score
    </div>

    <div class="metric-value">
    {:.2f}%
    </div>

    <div class="metric-line"></div>

    </div>
    """.format(st.session_state.probability),
    unsafe_allow_html=True
    )


with a2:

    st.markdown(
    """
    <div class="metric-card">

    <div class="metric-title">
    Prediction Status
    </div>

    <div class="metric-value">
    {}
    </div>

    <div class="metric-line"></div>

    </div>
    """.format(st.session_state.label),
    unsafe_allow_html=True
    )


with a3:

    st.markdown(
    """
    <div class="metric-card">

    <div class="metric-title">
    Model Confidence
    </div>

    <div class="metric-value">
    {}%
    </div>

    <div class="metric-line"></div>

    </div>
    """.format(st.session_state.confidence),
    unsafe_allow_html=True
    )


with a4:

    st.markdown(
    """
    <div class="metric-card">

    <div class="metric-title">
    Lead Category
    </div>

    <div class="metric-value">
    {}
    </div>

    <div class="metric-line"></div>

    </div>
    """.format(st.session_state.lead_quality),
    unsafe_allow_html=True
    )


st.markdown("<br>", unsafe_allow_html=True)


chart_col1, chart_col2 = st.columns(2)


with chart_col1:

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=[
                "Website Visits",
                "Time Spent",
                "Page Views"
            ],
            y=[
                st.session_state.website_visits,
                st.session_state.time_spent,
                st.session_state.page_views

            ]
        )
    )


    fig.update_layout(
        title="Lead Engagement Analysis",
        height=350,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
             color="#E5E7EB",
             size=16
        )
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


with chart_col2:

    channel_values = [
        int(st.session_state.print_media_type1),
        int(int(st.session_state.print_media_type2)),
        int(st.session_state.digital_media),
        int(st.session_state.educational),
        int(st.session_state.referral)
    ]


    fig2 = go.Figure()


    fig2.add_trace(
        go.Pie(
            labels=[
                "Print Media 1",
                "Print Media 2",
                "Digital Media",
                "Educational",
                "Referral"
            ],
            values=channel_values,
            hole=0.45
        )
    )


    fig2.update_layout(
        title="Marketing Channel Usage",
        height=350,
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(
           color="#E5E7EB",
           size=16
        )
    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)


st.markdown(
"""
<div class="section-title">
    🧠 AI Business Intelligence
</div>

<div class="section-subtitle">
    Automated recommendations based on machine learning prediction.
</div>
""",
unsafe_allow_html=True
)



if st.session_state.probability >= 75:

    priority = "🔥 HIGH PRIORITY"

    priority_message = (
        "This lead shows strong conversion potential. "
        "Sales team should contact immediately."
    )

    action = "Immediate Follow-up"


elif st.session_state.probability >= 40:

    priority = "⚡ MEDIUM PRIORITY"

    priority_message = (
        "This lead has moderate interest. "
        "Personalized engagement can improve conversion."
    )

    action = "Nurture & Engage"


else:

    priority = "❄️ LOW PRIORITY"

    priority_message = (
        "This lead requires nurturing before direct conversion efforts."
    )

    action = "Marketing Campaign"

st.session_state.priority = priority
st.session_state.action = action
st.session_state.priority_message = priority_message


b1, b2, b3 = st.columns(3)



with b1:

    st.markdown(
    f"""
    <div class="metric-card">

    <div class="metric-title">
    AI Score
    </div>

    <div class="metric-value">
    {st.session_state.confidence}
    </div>

    <div class="metric-line"></div>

    </div>
    """,
    unsafe_allow_html=True
    )



with b2:

    st.markdown(
    f"""
    <div class="metric-card">

    <div class="metric-title">
    Conversion Probability
    </div>

   <div class="metric-value">
   {float(st.session_state.probability):.2f}%
   </div>

    <div class="metric-line"></div>

    </div>
    """,
    unsafe_allow_html=True
    )



with b3:

    st.markdown(
    f"""
    <div class="metric-card">

    <div class="metric-title">
    Recommended Action
    </div>

    <div class="metric-value">
    {st.session_state.action}
    </div>

    <div class="metric-line"></div>

    </div>
    """,
    unsafe_allow_html=True
    )



st.markdown("<br>", unsafe_allow_html=True)



st.markdown(
f"""
<div class="glass-card">

<h3>
🚀 AI Decision Engine
</h3>

<p style="font-size:18px;">

<b>Priority:</b> {st.session_state.priority}

<br><br>

<b>Recommended Strategy:</b>

<br>

{st.session_state.priority_message}

<br><br>

<b>Next Best Action:</b>

<br>

{st.session_state.action}

</p>

</div>
""",
unsafe_allow_html=True
)


st.markdown("<br>", unsafe_allow_html=True)


st.markdown(
"""
<div class="section-title">
    🔍 Lead Feature Insights
</div>

<div class="section-subtitle">
    Understanding customer behaviour and factors influencing conversion.
</div>
""",
unsafe_allow_html=True
)



engagement_score = (
    st.session_state.website_visits * 0.35
    + st.session_state.time_spent * 0.40
    + st.session_state.page_views * 0.25
)


if engagement_score >= 50:

    engagement_level = "🔥 High Engagement"

elif engagement_score >= 20:

    engagement_level = "⚡ Medium Engagement"

else:

    engagement_level = "❄️ Low Engagement"



i1, i2, i3 = st.columns(3)



with i1:

    st.markdown(
    f"""
    <div class="metric-card">

    <div class="metric-title">
    Engagement Score
    </div>

    <div class="metric-value">
    {engagement_score:.1f}
    </div>

    <div class="metric-line"></div>

    </div>
    """,
    unsafe_allow_html=True
    )



with i2:

    st.markdown(
    f"""
    <div class="metric-card">

    <div class="metric-title">
    Engagement Level
    </div>

    <div class="metric-value">
    {engagement_level}
    </div>

    <div class="metric-line"></div>

    </div>
    """,
    unsafe_allow_html=True
    )



with i3:

    st.markdown(
    f"""
    <div class="metric-card">

    <div class="metric-title">
    Customer Profile
    </div>

    <div class="metric-value">
    {st.session_state.occupation}
    </div>

    <div class="metric-line"></div>

    </div>
    """,
    unsafe_allow_html=True
    )



st.markdown("<br>", unsafe_allow_html=True)



insight_col1, insight_col2 = st.columns(2)



with insight_col1:

    st.markdown(
    f"""
    <div class="glass-card">

    <h3>
    👤 Customer Behaviour Analysis
    </h3>


    <p>

    <b>Website Activity:</b>
    {st.session_state.get("last_activity","")}

    <br><br>

    <b>Profile Completion:</b>
    {st.session_state.get("profile_completed","")}

    <br><br>

    <b>First Interaction:</b>
    {st.session_state.get("first_interaction","")}

    <br><br>

    <b>Website Visits:</b>
    {st.session_state.get("website_visits",0)}

    </p>

    </div>
    """,
    unsafe_allow_html=True
    )



with insight_col2:

    st.markdown(
    f"""
    <div class="glass-card">

    <h3>
    📢 Marketing Influence
    </h3>


    <p>

    <b>Digital Media:</b>
    {"Active" if st.session_state.get("digital_media",0) else "Inactive"}

    <br><br>

    <b>Educational Channel:</b>
    {"Active" if st.session_state.get("educational",0) else "Inactive"}

    <br><br>

    <b>Referral:</b>
    {"Active" if st.session_state.get("referral",0) else "Inactive"}

    <br><br>

    <b>Print Media:</b>
    {"Used" if (st.session_state.print_media_type1 or st.session_state.print_media_type2) else "Not Used"}

    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)


st.markdown(
"""
<div class="section-title">
    🧩 Feature Importance Analysis
</div>

<div class="section-subtitle">
    Key factors influencing lead conversion prediction.
</div>
""",
unsafe_allow_html=True
)



feature_names = [
    "Age",
    "Website Visits",
    "Time Spent",
    "Page Views",
    "Student",
    "Unemployed",
    "Website Interaction",
    "Profile Low",
    "Profile Medium",
    "Phone Activity",
    "Website Activity",
    "Print Media 1",
    "Print Media 2",
    "Digital Media",
    "Educational Channel",
    "Referral"
]


feature_values = [
    st.session_state.get("age",0),
    st.session_state.get("website_visits",0),
    st.session_state.get("time_spent",0),
    st.session_state.get("page_views",0),
    int(st.session_state.get("occupation","") == "Student"),
    int(st.session_state.get("occupation","") == "Unemployed"),
    int(st.session_state.get("first_interaction","") == "Website"),
    int(st.session_state.get("profile_completed","") == "Low"),
    int(st.session_state.get("profile_completed","") == "Medium"),
    int(st.session_state.get("last_activity","") == "Phone Activity"),
    int(st.session_state.get("last_activity","") == "Website Activity"),
    int(st.session_state.get("print_media_type1",0)),
    int(st.session_state.get("print_media_type2",0)),
    int(st.session_state.get("digital_media",0)),
    int(st.session_state.get("educational",0)),
    int(st.session_state.get("referral",0))
]


importance_df = pd.DataFrame(
    {
        "Feature": feature_names,
        "Impact Score": feature_values
    }
)


importance_df = importance_df.sort_values(
    by="Impact Score",
    ascending=False
).head(8)



fig3 = go.Figure(
    go.Bar(
        x=importance_df["Impact Score"],
        y=importance_df["Feature"],
        orientation="h"
    )
)


fig3.update_layout(
    title=dict(
        text="Top Lead Conversion Drivers",
        font=dict(
            size=20,
            color="#FFFFFF"
        )
    ),
    height=450,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(
        color="#FFFFFF",
        size=16
    ),
    xaxis=dict(
        tickfont=dict(
            size=14,
            color="#E5E7EB"
        )
    ),
    yaxis=dict(
        tickfont=dict(
            size=14,
            color="#E5E7EB"
        )
    )
)


st.plotly_chart(
    fig3,
    use_container_width=True
)



st.markdown("<br>", unsafe_allow_html=True)



st.markdown(
"""
<div class="glass-card">

<h3>
🤖 AI Model Interpretation
</h3>

<p>

The model evaluates multiple customer behaviour signals
including website engagement, profile completion,
interaction history and marketing channels.

<br><br>

Higher engagement activities generally indicate stronger
conversion potential, while low activity leads require
additional nurturing strategies.

</p>

</div>
""",
unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)


st.markdown(
"""
<div class="section-title">
    📄 Lead Assessment Report
</div>

<div class="section-subtitle">
    Automated business report generated from AI prediction results.
</div>
""",
unsafe_allow_html=True
)



report_col1, report_col2 = st.columns(2)

label = st.session_state.label
probability = st.session_state.probability
confidence = st.session_state.confidence



with report_col1:

    st.markdown(
    f"""
    <div class="glass-card">

    <h3>
    📌 Lead Summary
    </h3>

    <p>

    <b>Prediction:</b>
    {st.session_state.get("label","")}

    <br><br>

    <b>Conversion Probability:</b>
    {probability:.2f}%

    <br><br>

    <b>Model Confidence:</b>
    {confidence}

    <br><br>

    <b>Lead Category:</b>
    {st.session_state.lead_quality}

    <br><br>

    <b>Customer Segment:</b>
    {st.session_state.get("occupation","")}

    </p>

    </div>
    """,
    unsafe_allow_html=True
    )



with report_col2:

    st.markdown(
    f"""
    <div class="glass-card">

    <h3>
    🎯 Business Recommendation
    </h3>

    <p>

    Based on AI analysis, this lead is classified as:

    <br><br>

    <b>{st.session_state.lead_quality}</b>

    <br><br>

    Recommended Business Action:

    <br><br>

    <b>{action}</b>

    <br><br>

    The recommendation is generated using
    customer engagement behaviour, interaction history
    and marketing channel activity.

    </p>

    </div>
    """,
    unsafe_allow_html=True
    )



st.markdown("<br>", unsafe_allow_html=True)



st.markdown(
"""
<div class="glass-card">

<h3>
📊 Executive Summary
</h3>

<p>

The Lead Conversion Intelligence System uses an ensemble
machine learning approach to estimate conversion probability.

<br><br>

The system evaluates customer engagement signals,
website activity, profile completion and marketing channels
to support data-driven sales decisions.

<br><br>

This report helps sales teams prioritize leads,
improve follow-up strategy and optimize conversion efforts.

</p>

</div>
""",
unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)


st.markdown(
"""
<div class="section-title">
    📥 Download Center
</div>

<div class="section-subtitle">
    Export AI prediction results for business reporting.
</div>
""",
unsafe_allow_html=True
)



report_data = {

    "Prediction": [
        st.session_state.get("label","")
    ],

    "Probability (%)": [
        round(float(st.session_state.get("Conversion Probability",0)),2)
    ],

    "Confidence (%)": [
        round(float(st.session_state.get("Model Confidence",0)),2)
    ],

    "Lead Quality": [
        st.session_state.get("lead_quality","")
    ],

    "Sales Priority": [
        st.session_state.get("priority","")
    ],

    "Recommended Action": [
        st.session_state.get("action","")
    ],

    "Age": [
        st.session_state.get("age",0)
    ],

    "Occupation": [
        st.session_state.get("occupation","")
    ],

    "Website Visits": [
        st.session_state.get("website_visits",0)
    ],

    "Time Spent On Website": [
        st.session_state.get("time_spent",0)
    ],

    "Page Views Per Visit": [
        st.session_state.get("page_views",0)
    ],

    "Profile Completed": [
        st.session_state.get("profile_completed","")
    ],

    "Last Activity": [
        st.session_state.get("last_activity","")
    ],

    "First Interaction": [
        st.session_state.get("first_interaction","")
    ],

    "Digital Media": [
        st.session_state.get("digital_media",0)
    ],

    "Referral": [
        st.session_state.get("referral",0)
    ],

    "Educational Channel": [
        st.session_state.get("educational",0)
    ],

    "Print Media 1": [
        st.session_state.get("print_media_type1",0)
    ],

    "Print Media 2": [
        st.session_state.get("print_media_type2",0)
    ]
}



report_df = pd.DataFrame(report_data)



csv_file = report_df.to_csv(
    index=False
).encode("utf-8")



download_col1, download_col2 = st.columns(2)



with download_col1:

    st.download_button(

        label="📄 Download Prediction Report",

        data=csv_file,

        file_name="Lead_Prediction_Report.csv",

        mime="text/csv"

    )



with download_col2:

    st.markdown(
    """
    <div class="glass-card">

    <h3>
    📊 Report Status
    </h3>

    <p>

    AI prediction report generated successfully.

    <br><br>

    Ready for sales analysis and business review.

    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)


st.markdown(
"""
<div class="section-title">
    🚀 AI Executive Overview
</div>

<div class="section-subtitle">
    Business summary generated from machine learning lead intelligence.
</div>
""",
unsafe_allow_html=True
)



e1, e2, e3, e4 = st.columns(4)



with e1:

    st.markdown(
    f"""
    <div class="metric-card">

    <div class="metric-title">
    Conversion Score
    </div>

    <div class="metric-value">
    {probability:.1f}%
    </div>

    <div class="metric-line"></div>

    </div>
    """,
    unsafe_allow_html=True
    )



with e2:

    st.markdown(
    f"""
    <div class="metric-card">

    <div class="metric-title">
    Lead Status
    </div>

    <div class="metric-value">
    {st.session_state.get("label","")}
    </div>

    <div class="metric-line"></div>

    </div>
    """,
    unsafe_allow_html=True
    )



with e3:

    st.markdown(
    f"""
    <div class="metric-card">

    <div class="metric-title">
    Lead Quality
    </div>

    <div class="metric-value">
    {st.session_state.get("lead_quality","")}
    </div>

    <div class="metric-line"></div>

    </div>
    """,
    unsafe_allow_html=True
    )



with e4:

    st.markdown(
    f"""
    <div class="metric-card">

    <div class="metric-title">
    Sales Action
    </div>

    <div class="metric-value">
    {action}
    </div>

    <div class="metric-line"></div>

    </div>
    """,
    unsafe_allow_html=True
    )



st.markdown("<br>", unsafe_allow_html=True)



if probability >= 70:

    ai_message = (
        "This lead demonstrates strong buying intent. "
        "Prioritize immediate sales engagement."
    )


elif probability >= 40:

    ai_message = (
        "This lead shows moderate engagement. "
        "Personalized communication can improve conversion chances."
    )


else:

    ai_message = (
        "This lead requires nurturing activities "
        "before aggressive sales outreach."
    )



st.markdown(
f"""
<div class="glass-card">

<h3>
🧠 AI Business Insight
</h3>

<p style="font-size:18px;">

The machine learning system analyzed customer behaviour,
website engagement, interaction history and marketing channels.

<br><br>

<b>AI Recommendation:</b>

<br>

{ai_message}

<br><br>

<b>Recommended Next Step:</b>

<br>

{action}

</p>

</div>
""",
unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)


st.markdown(
"""
<div class="section-title">
    🏗️ AI Model Architecture
</div>

<div class="section-subtitle">
    Machine learning pipeline powering the lead conversion intelligence system.
</div>
""",
unsafe_allow_html=True
)



st.markdown(
"""
<div class="glass-card">

<h3>
🤖 Stacking Ensemble Pipeline
</h3>

<p style="font-size:18px;">

The system uses a stacking ensemble approach combining
multiple machine learning models to improve prediction
performance and reliability.

</p>

</div>
""",
unsafe_allow_html=True
)



m1, m2, m3, m4 = st.columns(4)



with m1:

    st.markdown(
    """
    <div class="metric-card">

    <div class="metric-title">
    Base Model 1
    </div>

    <div class="metric-value">
    Random Forest
    </div>

    <div class="metric-line"></div>

    </div>
    """,
    unsafe_allow_html=True
    )



with m2:

    st.markdown(
    """
    <div class="metric-card">

    <div class="metric-title">
    Base Model 2
    </div>

    <div class="metric-value">
    XGBoost
    </div>

    <div class="metric-line"></div>

    </div>
    """,
    unsafe_allow_html=True
    )



with m3:

    st.markdown(
    """
    <div class="metric-card">

    <div class="metric-title">
    Base Model 3
    </div>

    <div class="metric-value">
    Logistic Regression
    </div>

    <div class="metric-line"></div>

    </div>
    """,
    unsafe_allow_html=True
    )



with m4:

    st.markdown(
    """
    <div class="metric-card">

    <div class="metric-title">
    Final Layer
    </div>

    <div class="metric-value">
    Meta Model
    </div>

    <div class="metric-line"></div>

    </div>
    """,
    unsafe_allow_html=True
    )



st.markdown("<br>", unsafe_allow_html=True)



st.markdown(
"""
<div class="glass-card">

<h3>
⚙️ Prediction Workflow
</h3>


<p style="font-size:18px;">

👤 User Lead Information

<br>
⬇️

<br>

🔧 Feature Engineering & Preprocessing

<br>
⬇️

<br>

🌲 Random Forest Probability

<br>

🚀 XGBoost Probability

<br>

📈 Logistic Regression Probability

<br>
⬇️

<br>

🧠 Meta Model Decision Layer

<br>
⬇️

<br>

🎯 Final Conversion Prediction

</p>


</div>
""",
unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)


st.markdown(
"""
<hr>

<div style="
text-align:center;
padding:25px;
color:#94A3B8;
font-size:14px;
">

<h3 style="
color:white;
">

🚀 Lead Conversion Intelligence System

</h3>


<p>

AI Powered Lead Scoring Platform

<br>

Built using Python • Machine Learning • Streamlit

</p>


<p>

© 2026 Alin Kumar | Data Science Portfolio Project

</p>


</div>

""",
unsafe_allow_html=True
)





    