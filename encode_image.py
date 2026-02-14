#!/usr/bin/env python3
import base64
import sys

try:
    # Read the new Charlie headshot image
    with open('/app/.shared/8510702019/photo_1771085609.jpg', 'rb') as f:
        image_data = f.read()
    
    # Convert to base64
    base64_data = base64.b64encode(image_data).decode('utf-8')
    
    print("SUCCESS: Image converted to base64")
    print(f"Data length: {len(base64_data)} characters")
    print(f"First 50 chars: {base64_data[:50]}")
    
    # Save to file
    with open('charlie_base64.txt', 'w') as f:
        f.write(base64_data)
    
    print("Base64 data saved to charlie_base64.txt")
    
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)