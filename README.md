<h1>Tublian Login Button Detector</h1>
<p>This project automates the detection of the login button on <a href="https://tublian.com" target="_blank">Tublian</a>. It captures a screenshot of the website, detects the login button using OpenCV, and visualizes the detected coordinates.</p>

<h2>Features</h2>
    <ul>
        <li>Captures a <strong>screenshot</strong> of Tublian’s homepage using Selenium.</li>
        <li>Detects the <strong>login button</strong> based on color and shape filtering.</li>
        <li>Marks the detected button position and displays it.</li>
    </ul>

<h2>📂 Project Structure</h2>
<pre>
tublian_login_detector/
│── detect_login_button.py   # Captures screenshot & detects button
│── visualize_detection.py   # Visualizes detected coordinates
│── test_detection.py        # Unit tests for button detection
│── README.html              # Documentation
│── requirements.txt         # Dependencies
│── tublian_screenshot.png   # (Generated) Screenshot of Tublian
│── detected_login_button.png # (Generated) Image with detected button
</pre>

<h2>Installation</h2>
    
<h3>1️⃣ Clone the repository</h3>
<pre><code>git clone https://github.com/yourusername/tublian_login_detector.git
cd tublian_login_detector</code></pre>

<h3>2️⃣ Set up a virtual environment (optional)</h3>
<pre><code>uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate</code></pre>

<h3>3️⃣ Install dependencies</h3>
<pre><code>uv pip install -r requirements.txt</code></pre>

<h2>▶️ Running the Program</h2>
    
<h3>1️⃣ Capture a screenshot & detect the login button</h3>
<pre><code>python3 detect_login_button.py</code></pre>

<h3>2️⃣ Visualize detected coordinates</h3>
<pre><code>python3 visualize_detection.py</code></pre>

<h3>3️⃣ Run unit tests</h3>
<pre><code>python3 test_detection.py</code></pre>

<h2>🛠️ How It Works</h2>
<ol>
<li>The program launches a headless browser to take a screenshot of <strong>Tublian</strong>.</li>
<li>It processes the image using <strong>OpenCV</strong> to detect the login button by filtering for its color and shape.</li>
<li>Coordinates of the detected button are printed and visualized on the image.</li>
</ol>

<h2>🔗 Dependencies</h2>
    <ul>
        <li>Python 3.8+</li>
        <li>OpenCV</li>
        <li>NumPy</li>
        <li>Matplotlib</li>
        <li>Selenium</li>
        <li>WebDriver Manager</li>
    </ul>