_surface.diffuse = pow(float4(0.831, 0.820, 0.784, 1.0), 2.3);
_surface.emission = pow(float4(0.521, 0.510, 0.478, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.139, 0.140, 0.135, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.8, 2, 0, 0);
// SpecularColor
_surface.multiply = float4(1.0, 1.0, 1.0, 1.0);
// Wrap
_surface.specular = float4(0.5, 0.5, 0.0, 0.0);
