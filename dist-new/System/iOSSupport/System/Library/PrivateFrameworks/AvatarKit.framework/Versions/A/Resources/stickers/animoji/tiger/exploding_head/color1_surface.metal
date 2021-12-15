_surface.diffuse = pow(float4(0.928, 0.762, 0.263, 1.0), 2.3);
_surface.emission = pow(float4(0.458, 0.225, 0.074, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.543, 0.305, 0.008, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(1.0, 2.5, 0, 0);
// SpecularColor
_surface.multiply = float4(1.0, 1.0, 1.0, 1.0);
// Wrap
_surface.specular = float4(0.458, 0.684, 0.0, 0.0);
