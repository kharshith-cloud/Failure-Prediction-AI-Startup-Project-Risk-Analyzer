import urllib.request
import urllib.parse

url = 'http://127.0.0.1:5000/submit'
data = urllib.parse.urlencode({
    'project_name': 'Online College Food Delivery',
    'project_description': 'A platform for students to order food from nearby food providers.',
    'target_market': 'College students',
    'budget': '50000',
    'competition': 'Existing food delivery platforms',
    'resources': 'Student development team',
    'objectives': 'Provide convenient food ordering for students'
}).encode('utf-8')

req = urllib.request.Request(url, data=data)
try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
