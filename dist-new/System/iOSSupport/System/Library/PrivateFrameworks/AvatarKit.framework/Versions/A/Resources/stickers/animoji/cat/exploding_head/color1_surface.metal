_surface.diffuse = pow(float4(0.972, 0.828, 0.310, 1.0), 2.3);
_surface.emission = pow(float4(0.333, 0.204, 0.051, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.634, 0.359, 0.004, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.3, 2, 0, 0);
// SpecularColor
_surface.multiply = float4(0.8, 0.8, 1.4, 1.0);
// Wrap
_surface.specular = float4(0.0, 0.0, -5.0, 0.0);
