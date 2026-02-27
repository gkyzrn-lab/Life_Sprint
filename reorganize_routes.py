#!/usr/bin/env python3
"""
Script to reorganize router_curriculum.py routes in the correct order for FastAPI.
FastAPI matches routes in registration order, so static routes must come before parameterized ones.
"""

import re

# Read the original file
with open('api/router_curriculum.py', 'r') as f:
    content = f.read()

# Extract imports (everything before router = APIRouter)
imports_match = re.search(r'(.*?)(router = APIRouter.*?\n)', content, re.DOTALL)
if not imports_match:
    print("ERROR: Could not find router definition")
    exit(1)

imports = imports_match.group(1)
router_def = imports_match.group(2)

# Extract all route definitions
route_pattern = r'(@router\.(get|post|put|delete|patch)\(["\'].*?["\'].*?\)\s*(?:async\s+)?def\s+\w+\(.*?\):.*?(?=\n@router\.|$))'
routes = re.findall(route_pattern, content, re.DOTALL)

# Categorize routes
static_routes = []
single_param_routes = []
multi_param_routes = []
catch_all_routes = []

for route_tuple in routes:
    route_text = route_tuple[0]
    
    # Extract the route path
    path_match = re.search(r'@router\.\w+\(["\']([^"\']+)["\']', route_text)
    if not path_match:
        continue
    
    path = path_match.group(1)
    
    # Count parameters
    param_count = path.count('{')
    
    # Categorize based on path structure
    if param_count == 0:
        static_routes.append(route_text)
    elif param_count == 1:
        single_param_routes.append(route_text)
    elif path == '/{college_id}/{major_id}':
        # This is the catch-all
        catch_all_routes.append(route_text)
    else:
        multi_param_routes.append(route_text)

# Build the new file content
new_content = imports + router_def + """
# ================================================================================
# CRITICAL: ROUTE ORDERING FOR FASTAPI
# ================================================================================
# FastAPI matches routes in the order they are registered.
# Routes with path parameters will match before static routes if defined first.
# 
# ORDER:
# 1. Static paths (no parameters): /resources/study-tips, /achievements, etc.
# 2. Single parameter routes: /enhanced/{major_id}, /achievements/{id}, etc.
# 3. Multiple parameter routes: /{college_id}/{major_id}, etc.
# 4. Catch-all routes: MUST BE LAST
# ================================================================================


# ================================================================================
# SECTION 1: STATIC PATH ROUTES (NO PATH PARAMETERS)
# ================================================================================

"""

new_content += '\n\n'.join(static_routes)

new_content += """


# ================================================================================
# SECTION 2: SINGLE PATH PARAMETER ROUTES
# ================================================================================

"""

new_content += '\n\n'.join(single_param_routes)

new_content += """


# ================================================================================
# SECTION 3: MULTIPLE PATH PARAMETER ROUTES
# ================================================================================

"""

new_content += '\n\n'.join(multi_param_routes)

new_content += """


# ================================================================================
# SECTION 4: CATCH-ALL ROUTES (MUST BE LAST)
# ================================================================================

"""

new_content += '\n\n'.join(catch_all_routes)

# Write the new file
with open('api/router_curriculum.py', 'w') as f:
    f.write(new_content)

print(f"✅ Reorganized router_curriculum.py")
print(f"   - Static routes: {len(static_routes)}")
print(f"   - Single parameter routes: {len(single_param_routes)}")
print(f"   - Multiple parameter routes: {len(multi_param_routes)}")
print(f"   - Catch-all routes: {len(catch_all_routes)}")
print(f"   - Total routes: {len(static_routes) + len(single_param_routes) + len(multi_param_routes) + len(catch_all_routes)}")
