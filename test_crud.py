#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')


try:
    from lib.crud import create_category, create_habit, get_all_categories
    print("✓ CRUD functions imported successfully")
    
    # Test creating a category
    category = create_category("Test Category from CRUD")
    print(f"✓ Category created via CRUD: {category.name} (ID: {category.id})")
    
    # Test listing categories
    categories = get_all_categories()
    print(f"✓ Found {len(categories)} categories")
    for cat in categories:
        print(f"  - {cat.name} (ID: {cat.id})")
        
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
