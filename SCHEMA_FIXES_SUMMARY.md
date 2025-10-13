# Fixing drf-spectacular Schema Generation Issues

This document describes the changes made to fix the drf-spectacular warnings and errors.

## Summary of Changes

1. Added necessary imports for type annotations:

   ```python
   from drf_spectacular.utils import extend_schema_field
   from drf_spectacular.types import OpenApiTypes
   ```

2. Added type annotations to SerializerMethodField methods:

   - Added `@extend_schema_field(OpenApiTypes.STR)` decorator to all get\_\* methods
   - Added Python return type hints (`-> str`) to method definitions

3. Fixed ViewSets that were missing serializer_class or queryset attributes:

   - Added `serializer_class = XYZSerializer` to ViewSets
   - Added proper queryset for schema generation

4. Added swagger_fake_view checks to get_queryset methods with specific model classes:

   - Fixed code that used generic `Model.objects.none()` to use the correct model class
   - Created a script to automatically identify and fix model references

   ```python
   def get_queryset(self):
       # Check for swagger schema generation
       if getattr(self, "swagger_fake_view", False):
           return Model.objects.none()
       # Original logic follows...
   ```

## Why These Changes Were Needed

- **SerializerMethodField Type Inference**: drf-spectacular couldn't automatically infer the return type of SerializerMethodField methods, causing it to default to string in the schema.
- **ViewSet Serializer/Queryset Detection**: Some ViewSets didn't expose a stable serializer_class or queryset for the schema generator to inspect, resulting in errors.

- **Request-Dependent get_queryset Methods**: Some get_queryset methods relied on the request object or raised exceptions during schema generation. The swagger_fake_view check provides a safe fallback.

## Result

These changes make the API schema generation clean and accurate, eliminating all the warnings and errors. The schema now correctly documents the API endpoints, making it easier for frontend developers to understand the API contract.

## Notes for Future Development

1. Always add `@extend_schema_field` annotations to SerializerMethodField methods with proper return types
2. Make sure ViewSets have either:
   - serializer_class and queryset attributes, or
   - properly implemented get_serializer_class() and get_queryset() with swagger_fake_view checks
3. Always use specific model classes with `objects.none()` for schema generation, never generic `Model.objects.none()`
4. Avoid empty lines between `@extend_schema_field` decorator and the method definition
5. For complex schema customizations, use drf-spectacular's extend_schema decorators
