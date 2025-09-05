#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')


try:
    from lib.main import cli
    print("✓ Main CLI imported successfully")
    
    # Test if we can list categories
    from lib.crud import get_all_categories
    categories = get_all_categories()
    print(f"✓ Found {len(categories)} categories")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
