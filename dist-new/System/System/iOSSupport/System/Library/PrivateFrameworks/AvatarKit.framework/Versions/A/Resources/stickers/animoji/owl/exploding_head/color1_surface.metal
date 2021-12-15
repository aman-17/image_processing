_surface.diffuse = pow(float4(0.521, 0.402, 0.306, 1.0), 2.3);
_surface.emission = pow(float4(0.282, 0.197, 0.125, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.647, 0.473, 0.246, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.75, 2, 0, 0);
// SpecularColor
_surface.multiply = float4(1.0, 1.0, 1.0, 1.0);
// Wrap
_surface.specular = float4(0.5, 0.5, 0.0, 0.0);
