_surface.diffuse = pow(float4(1.0, 1.0, 1.0, 1.0), 2.3);
_surface.emission = pow(float4(0.259, 0.259, 0.259, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.394, 0.615, 0.734, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.8, 4, 0, 8);
// SpecularColor
_surface.multiply = float4(1.0, 1.0, 1.0, 1.0);
// Wrap
_surface.specular = float4(0.1, -0.05, 0.0, 0.0);
