from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Sample data for tools
TOOLS = [
    {
        'id': 1,
        'name': 'Oral History Digitization Guide',
        'category': 'Documentation',
        'description': 'Step-by-step guide for recording and preserving oral histories',
        'link': '#'
    },
    {
        'id': 2,
        'name': '3D Scanning Best Practices',
        'category': 'Documentation',
        'description': 'Recommendations for 3D scanning of artifacts and monuments',
        'link': '#'
    },
    {
        'id': 3,
        'name': 'Community Engagement Toolkit',
        'category': 'Engagement',
        'description': 'Methods for involving local communities in preservation efforts',
        'link': '#'
    },
    {
        'id': 4,
        'name': 'Metadata Standards Handbook',
        'category': 'Standards',
        'description': 'UNESCO-approved metadata standards for heritage documentation',
        'link': '#'
    }
]

# Sample case studies
CASE_STUDIES = [
    {
        'title': 'Immersive Digital Preservation of Mustang Architectural Caves',
        'location': 'Nepal',
        'description': 'This initiative proposes a scalable AR/VR platform to digitally preserve and showcase over 10,000 architectural caves in Mustang, Nepal, starting with 3D virtual tours using drone photogrammetry and LiDAR. It supports future expansions like AR apps, VR modules for education, and integration with global heritage platforms. By enabling continuous updates and open collaboration, the project ensures long-term conservation while positioning Nepal as a leader in digital heritage innovation.',
        'image': 'cave.jpg'
    },
    {
        'title': '3D Documentation of Angkor Wat',
        'location': 'Cambodia',
        'description': 'Using laser scanning to create detailed records of the temple complex',
        'image': '3d.jpg'
    },
    {
        'title': 'Community Archives of Intangible Heritage',
        'location': 'Brazil',
        'description': 'Empowering local communities to document their cultural practices',
        'image': 'brazil.jpg'
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tools')
def tools():
    return render_template('tools.html', tools=TOOLS)

@app.route('/best-practices')
def best_practices():
    return render_template('best-practices.html')

@app.route('/case-studies')
def case_studies():
    return render_template('case-studies.html', case_studies=CASE_STUDIES)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Here you would typically save this data or send an email
        return render_template('contact.html', success=True)
    return render_template('contact.html', success=False)

@app.route('/api/tools')
def api_tools():
    return jsonify(TOOLS)

@app.route('/api/tools/<int:tool_id>')
def api_tool(tool_id):
    tool = next((t for t in TOOLS if t['id'] == tool_id), None)
    return jsonify(tool) if tool else ('', 404)

if __name__ == '__main__':
    app.run(debug=True)