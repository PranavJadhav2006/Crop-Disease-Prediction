import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Crop Disease Prediction", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
        .main-title {
            font-size: 36px !important;
            color: #2E8B57;
            text-align: center;
            font-weight: bold;
        }
        .sub-title {                            
            font-size: 24px;
            color: #4682B4;
            text-align: center;
        }
        .sidebar .sidebar-content {
            background-color: #DFF6DD;
        }
        .uploaded-img {
            display: block;
            margin: 0 auto;
            border-radius: 10px;
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
        }
        .predict-button {
            background-color: #FF4500 !important;
            color: white !important;
            font-size: 18px !important;
            border-radius: 10px !important;
            padding: 10px !important;
        }
        .stApp {
            background: linear-gradient(to right, #f3ffe3, #c3ebc3, #7ecb7e);
        }
    </style>
""", unsafe_allow_html=True)

# Function to set background image for Home Page
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.3)), 
                        url("data:image/jpg;base64,{encoded_string}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Sidebar Navigation
st.sidebar.title("🌿 Dashboard")
app_mode = st.sidebar.radio("📌 Select a Page", ["Home", "About", "Disease Prediction", "Feedback", "Settings"])

# 📌 Useful Links Section
st.sidebar.markdown("---")
st.sidebar.subheader("🌍 Useful Links")
st.sidebar.markdown("""
🔗 [Agricultural Research Papers](https://www.sciencedirect.com)  
📖 [Plant Disease Database](https://plantvillage.psu.edu/)  
📊 [Weather & Crop Data](https://www.fao.org/giews/en/)  
""")

# 📢 Latest Updates
st.sidebar.markdown("---")
st.sidebar.subheader("📢 Latest Updates")
st.sidebar.markdown("""
✅ Added new AI model for **higher accuracy**.  
✅ Improved **UI & Background styling**.  
✅ Faster **image processing & prediction**.  
""")

#  Feedback Section
if app_mode == "Feedback":
    st.markdown("<h1 class ='Feedback' style='color : blue ; text-align:center ; margin-top:2rem' > Share Your Feedback</h1>",unsafe_allow_html=True)
    st.markdown("<p class='Feedback_txt' style='font-size:20px; color:#FF5733;'>Write Your Feedback Here ✍️</p>", unsafe_allow_html=True)
    feedback_text = st.text_area("")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback! 😊")

#  Settings Section
if app_mode == "Settings":
    st.markdown("<h1 class ='Feedback' style='color :#064420 ; text-align:center ; margin-top:2rem' >⚙️ User Settings</h1>",unsafe_allow_html=True)
    # # theme = st.radio("🎨 Select Theme:", ["Light", "Dark", "Green"])
    st.markdown(""" 
      <label style = 'font-size:1.5rem;'>
        <input type="checkbox" id="myCheckbox" style='cursor:pointer; transform: scale(1.5);accent-color: #4CAF50; margin-right: 10px;'>
        Enable Notifications 🔔
        </label>
        <hr>
       <label style="font-size: 1.2rem; color: #333; margin-top: 0.5rem; display: block;font-size:1.5rem">
    🌍 Select Language:
        </label>
        <select style="padding: 10px; font-size: 1rem; border: 2px solid #4CAF50; border-radius: 8px; background: #f9f9f9; 
               color: #333; cursor: pointer; outline: none; transition: 0.3s; width: 100%; max-width: 250px; display: block;">
    <option value="en">🇺🇸 English</option>
    <option value="es">🇪🇸 Spanish</option>
    <option value="hi">🇮🇳 Hindi</option>
    </select>
    <hr>
    <label style="font-size: 1.5rem; color: #333; margin-top: 1rem; display: block;">
    👤 Profile Visibility:
</label>
<select style="padding: 10px; font-size: 1rem; border: 2px solid #FF4500; border-radius: 8px; background: #f9f9f9; 
               color: #333; cursor: pointer; outline: none; transition: 0.3s; width: 100%; max-width: 250px;">
    <option value="public">🌍 Public</option>
    <option value="private">🔒 Private</option>
</select>
<hr>
                
<button style="margin-top: 1.5rem; padding: 12px 20px; font-size: 1.2rem; font-weight: bold; background-color: #008CBA; 
               color: white; border: none; border-radius: 8px; cursor: pointer; transition: 0.3s;">
    💾 Save Settings
</button>
        <hr>
    """,unsafe_allow_html=True)

crop_data = {
    "Wheat": {
        "image": "wheat.jpg",
        "info": "🌾 Wheat is a staple crop rich in carbohydrates and essential nutrients. It requires well-drained soil and moderate temperatures."
    },
    "Rice": {
        "image": "rice.jpg",
        "info": "🌿 Rice is a major food crop that grows well in flooded fields. It requires warm temperatures and ample water."
    },
    "Corn": {
        "image": "corn.jpg",
        "info": "🌽 Corn is used for food and industrial purposes. It grows best in warm climates with full sunlight."
    }
}

# Initialize session state for selected crop
if "selected_crop" not in st.session_state:
    st.session_state.selected_crop = None


# 🌱 Home Page
if app_mode == "Home":
    set_background("home_page.jpg")  

    st.markdown("<h1 class='main-title' style=' font-size:10rem !important; color: #064420; text-align: center; font-weight: bold;'>🌱 Crop Disease Prediction System</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <h2 class='sub-title' style = ' font-size: 24px; color: #D32F2F; text-align: center;'>Welcome to the Crop Disease Prediction System! 🚜🌾</h2>
    <p style='text-align: center; color: #333;'>Our system helps farmers and agricultural experts detect plant diseases early.</p>
    <ul style='color: #F5F5DC; font-size: 18px;'>
        <li><b>🌿 Upload an image of a plant leaf.</b></li>
        <li><b>🔍 Get instant disease predictions.</b></li>
        <li><b>💡 Receive recommendations for treatment.</b></li>
    </ul>
    <p style='text-align: center; color: #8B0000; font-size: 20px;'><b>🔍 Get started by selecting 'Disease Prediction' from the sidebar!</b></p>
            <br><hr style='font-weight:bold'>
               <h2 style="color:#064420">Select a Crop to Learn More</h2>
                 """, unsafe_allow_html=True)
   
    
    # Create a layout with columns for crops
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🌾 Wheat"):
            st.session_state.selected_crop = "Wheat"

    with col2:
        if st.button("🌿 Rice"):
            st.session_state.selected_crop = "Rice"

    with col3:
        if st.button("🌽 Corn"):
            st.session_state.selected_crop = "Corn"

 # Display crop information if a crop is selected
if st.session_state.selected_crop:
    crop = st.session_state.selected_crop
    st.image(crop_data[crop]["image"], width=1000) 
    st.markdown(f"### {crop}")
    st.write(crop_data[crop]['info'])


#  About Page
elif app_mode == "About":
    st.markdown("<h1 class='main-title' style='color: #DC143C;'>📌 About the Project</h1>", unsafe_allow_html=True)
    st.markdown("""
    <h2 style='color: #8A2BE2;'>📊 Dataset Overview</h2>
    <ul style='color: #483D8B;'>
        <li>The dataset contains images of <b>healthy and diseased crop leaves</b>.</li>
        <li>It is categorized into <b>multiple plant disease classes</b>.</li>
        <li>The images are preprocessed for better accuracy in disease detection.</li>
    </ul>
    
    <h2 style='color: #FF8C00;'>🎯 Objective</h2>
    <p style='color: #A52A2A;'>Our goal is to assist farmers by providing an <b>AI-powered plant disease detection tool</b> that is fast, accurate, and easy to use.</p>
    """, unsafe_allow_html=True)

#  Disease Prediction Page
elif app_mode == "Disease Prediction":
    st.markdown("<h1 class='main-title' style='color: #4682B4;'>🦠 Plant Disease Prediction</h1>", unsafe_allow_html=True)
    uploaded_image = st.file_uploader("📤 Upload a plant leaf image:", type=["jpg", "png", "jpeg"])
    
    if uploaded_image is not None:
        st.image(uploaded_image, use_column_width=True, caption='Uploaded Image')

        if st.button("Predict Disease", key="predict", help="Click to analyze the image", use_container_width=True):
            st.snow()
            st.write("Analyzing the image...")
            st.success("Prediction result will be displayed here after model processing.")

