_surface.diffuse = pow(float4(0.619, 0.396, 0.153, 1.0), 2.3);
_surface.emission = pow(float4(0.502, 0.353, 0.180, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.663, 0.403, 0.172, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.8, 2.4, 0, 0);
// SpecularColor
_surface.multiply = float4(0.3, 0.3, 0.3, 1.0);
// Wrap
_surface.specular = float4(0.0, 0.1, -8, 0.4);
