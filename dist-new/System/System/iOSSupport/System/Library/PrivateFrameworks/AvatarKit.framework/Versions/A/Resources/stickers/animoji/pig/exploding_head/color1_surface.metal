_surface.diffuse = pow(float4(0.944, 0.750, 0.698, 1.0), 2.3);
_surface.emission = pow(float4(0.470, 0.252, 0.220, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.715, 0.328, 0.348, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.1, 2.5, 0, 0);
// SpecularColor
_surface.multiply = float4(1.0, 1.0, 1.0, 1.0);
// Wrap
_surface.specular = float4(0.0, 0.2, -8, 0.0);
