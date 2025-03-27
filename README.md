<h1>Tublian Login Button Detector</h1>
<p>
    This project automates the detection of the login button on 
    <a href="https://tublian.com" target="_blank">Tublian</a>.  
    It captures a screenshot of the website, detects the login button dynamically using 
    <strong>Selenium</strong>, highlights it in a live browser session, and visualizes 
    the detected coordinates using <strong>OpenCV</strong>.
</p>

<h2>✨ Features</h2>
<ul>
    <li><strong>Opens a live browser</strong> (not headless) to dynamically detect the login button.</li>
    <li><strong>Captures a screenshot</strong> before and after highlighting the login button.</li>
    <li><strong>Detects login buttons</strong> by searching for "login", "log in", or "sign in" in button and link text.</li>
    <li><strong>Highlights the detected login button</strong> in real-time.</li>
    <li><strong>Clicks the login button</strong> and opens the login page in a <strong>new tab</strong>.</li>
    <li><strong>Visualizes button detection</strong> with red dots on the saved screenshot.</li>
</ul>

<h2>📂 Project Structure</h2>
<pre>
tublian_login_detector/
│── detect_login_button.py    # Captures screenshot, detects & clicks login button
│── visualize_detection.py    # Visualizes detected coordinates
│── test_detection.py         # Unit tests for button detection
│── README.md                 # Documentation
│── requirements.txt          # Dependencies
│── screenshot_before.png     # (Generated) Screenshot before detection
│── highlighted_screenshot.png # (Generated) Screenshot after detection
│── detected_login_button.png # (Generated) Image with detected button
</pre>

<h2>📥 Installation</h2>

<h3>1️⃣ Clone the repository</h3>
<pre><code>git clone https://github.com/yourusername/detect_login_button.git
cd detect_login_button</code></pre>

<h3>2️⃣ Set up a virtual environment (optional)</h3>
<pre><code>uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate</code></pre>

<h3>3️⃣ Install dependencies</h3>
<pre><code>uv pip install -r requirements.txt</code></pre>

<h2>▶️ Running the Program</h2>

<h3>1️⃣ Capture a screenshot, detect, highlight, and click the login button</h3>
<pre><code>python3 detect_login_button.py https://tublian.com</code></pre>
<p><strong>The program will:</strong></p>
<ul>
    <li>Open the browser and navigate to the provided URL.</li>
    <li>Highlight the detected login button.</li>
    <li>Click the login button (opens in a new tab).</li>
    <li>Save before/after screenshots.</li>
</ul>

<h3>2️⃣ Visualize detected coordinates</h3>
<pre><code>python3 visualize_detection.py</code></pre>
<p>This will display the detected button location with a <strong>red dot</strong>.</p>

<h3>3️⃣ Run unit tests</h3>
<pre><code>python3 test_detection.py</code></pre>

<h2>🛠️ How It Works</h2>
<ol>
    <li><strong>Opens a live browser session</strong> instead of a headless mode.</li>
    <li><strong>Searches for buttons and links</strong> with "login", "log in", or "sign in" text.</li>
    <li><strong>Highlights the detected button</strong> in the browser.</li>
    <li><strong>Takes two screenshots</strong> (before & after highlighting the button).</li>
    <li><strong>Clicks the login button</strong> to open the login page in a new tab.</li>
    <li><strong>Visualizes detection results</strong> with red dots using OpenCV.</li>
</ol>

<h2>🔗 Dependencies</h2>
<ul>
    <li>Python 3.8+</li>
    <li>Selenium</li>
    <li>OpenCV</li>
    <li>NumPy</li>
    <li>Matplotlib</li>
    <li>WebDriver Manager</li>
</ul>

<h2>🚀 Updates</h2>
<ul>
    <li>✅ <strong>Live browser mode</strong> (no <code>--headless</code> flag).</li>
    <li>✅ <strong>Detects & highlights login buttons dynamically</strong> in real-time.</li>
    <li>✅ <strong>Clicks login button and opens the login page in a new tab.</strong></li>
    <li>✅ <strong>Saves two screenshots</strong> (before & after detection).</li>
    <li>✅ <strong>Visualizes detected login button with OpenCV red dots.</strong></li>
</ul>
